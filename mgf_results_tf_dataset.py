from pyteomics import parser,mgf
import numpy as np # TODO: get rid of numpy! ... replace by tensorflow
import tensorflow as tf
import re 

aa = parser.std_amino_acids
pad = '_'
aa_with_pad = np.concatenate([[pad],aa])    
len_aa = len(aa_with_pad)

MAX_PEPTIDE_LENGTH=24
MAX_N_PEAKS=200
MZ_MIN,MZ_MAX=100,2000+100
MZ_ERROR = 0.1
MZ_RESOLUTION=int((MZ_MAX-MZ_MIN)/MZ_ERROR)
MAX_DYNAMIC_RANGE=1000# TODO: this has to be replaced! Bin/Embed intensities? ...feels weird
MAX_INTENSITY=10e-7# TODO: this has to be replaced! Bin/Embed intensities? ...feels weird
BATCH_SIZE=64

mz_bins = np.linspace(MZ_MIN,MZ_MAX,MZ_RESOLUTION-1)
intensity_bins = np.linspace(0,MAX_INTENSITY,MAX_DYNAMIC_RANGE-1) # TODO: this has to be replaced! Bin/Embed intensities? ...feels weird

def get_sequence_of_indices(sequence: str, aa_list: list=list(aa_with_pad)):
    return np.array([aa_list.index(aa) for aa in sequence])

def trim_sequence(indices):
    if len(indices)<=MAX_PEPTIDE_LENGTH:
        indices = np.pad(indices,((0,MAX_PEPTIDE_LENGTH-(indices.shape[0]))), 'constant', constant_values=0)
        return indices
    else:
        return indices[:MAX_PEPTIDE_LENGTH] #TODO: this has to be replaced! Longer Peptides should be discarded or increase MAX_PEPTIDE_LENGTH

def trim_peaks_list(mz,intensities,MAX_N_PEAKS=MAX_N_PEAKS,pad=True):
    if mz.shape[0]<=MAX_N_PEAKS and pad:
        mz = np.pad(mz,((0,MAX_N_PEAKS-(mz.shape[0]))), 'constant', constant_values=0)
        intensities = np.pad(intensities,((0,MAX_N_PEAKS-(intensities.shape[0]))), 'constant', constant_values=0)    
        return mz,intensities
    else:
        indices = np.argsort(intensities)[-MAX_N_PEAKS:][::-1] # take only highest=MAX_N_PEAKS peaks
        return mz[indices],intensities[indices]

def get_features(entry):
    sequence = entry['params']['seq']
    sequence = re.sub(r"[^A-Z]",'',sequence) #TODO: this has to be replaced! at least fixed Modifications should be properly implemented
    mz = entry['m/z array']
    intensities = entry['intensity array']
    return sequence,np.array(mz),np.array(intensities) 

def ion_current_normalize(intensities):
    total_sum = np.sum(intensities**2)
    normalized = intensities/total_sum
    return normalized

def iterate(mgf_file):     
    def iterate_():        
        with mgf.read(mgf_file) as reader:              
            for entry in reader:
                sequence, mz, intensities = get_features(entry)
                indices = get_sequence_of_indices(sequence)
                indices = trim_sequence(indices)
                intensities = ion_current_normalize(intensities)
                mz,intensities = trim_peaks_list(mz,intensities,pad=True)
                mz = np.digitize(mz,bins=mz_bins)
                intensities = np.digitize(intensities,bins=intensity_bins) # TODO: this has to be replaced! Bin/Embed intensities? ...feels weird
                yield (mz,intensities),indices
    return iterate_

def create_ds(iterator):
    ds = tf.data.Dataset.from_generator(iterator,((tf.int32,tf.int32),tf.int32))
    ds = ds.batch(BATCH_SIZE).repeat()
    return ds

if __name__ == "__main__": 

    mgf_file="./proteometools/small.mgf"
    ds = create_ds(iterate(mgf_file))

    inputs_mz = tf.keras.layers.Input(shape=(MAX_N_PEAKS,))
    inputs_intensities = tf.keras.layers.Input(shape=(MAX_N_PEAKS,))
    emb_1 = tf.keras.layers.Embedding(input_dim=MZ_RESOLUTION,output_dim=16)(inputs_mz)
    emb_2 = tf.keras.layers.Embedding(input_dim=MAX_DYNAMIC_RANGE,output_dim=16)(inputs_intensities)
    x = emb_1+emb_2

    x = tf.keras.layers.Flatten()(x)
    x = tf.keras.layers.Dense(MAX_PEPTIDE_LENGTH*len_aa)(x) #TODO: this has to be replaced!
    x = tf.reshape(x,(-1,MAX_PEPTIDE_LENGTH,len_aa))

    x = tf.keras.activations.softmax(x)
    model = tf.keras.Model([inputs_mz,inputs_intensities],x)
    model.compile(optimizer=tf.keras.optimizers.Adam(),
                  loss=tf.keras.losses.SparseCategoricalCrossentropy())
    model.summary()
    
    model.fit(ds,steps_per_epoch=10,epochs=10)

    y = model.predict(ds,steps=1)

    def decode(indices,aa=aa_with_pad,predicted=True):
        if predicted:
            indices = np.argmax(indices,axis=-1)
        sequence = np.apply_along_axis(lambda x: aa[x],axis=-1,arr=indices)
        sequence = np.apply_along_axis(lambda x: ''.join(x),axis=-1,arr=sequence)
        return sequence
   
    ground_truth = np.array([x[1] for x in ds.take(1)])
    ground_truth = decode(ground_truth,predicted=False)
    ground_truth = list(ground_truth[0])

    y = list(decode(y))

    print("predicted peptide / true peptide")
    print(np.array(list(zip(y,ground_truth))[:10]))