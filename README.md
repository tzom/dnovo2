# dnovo2
de novo sequencing

> python mgf_results_tf_dataset.py 

```
Model: "model"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
input_1 (InputLayer)            [(None, 200)]        0                                            
__________________________________________________________________________________________________
input_2 (InputLayer)            [(None, 200)]        0                                            
__________________________________________________________________________________________________
embedding (Embedding)           (None, 200, 16)      320000      input_1[0][0]                    
__________________________________________________________________________________________________
embedding_1 (Embedding)         (None, 200, 16)      16000       input_2[0][0]                    
__________________________________________________________________________________________________
tf_op_layer_AddV2 (TensorFlowOp [(None, 200, 16)]    0           embedding[0][0]                  
                                                                 embedding_1[0][0]                
__________________________________________________________________________________________________
flatten (Flatten)               (None, 3200)         0           tf_op_layer_AddV2[0][0]          
__________________________________________________________________________________________________
dense (Dense)                   (None, 504)          1613304     flatten[0][0]                    
__________________________________________________________________________________________________
tf_op_layer_Reshape (TensorFlow [(None, 24, 21)]     0           dense[0][0]                      
__________________________________________________________________________________________________
tf_op_layer_Max (TensorFlowOpLa [(None, 24, 1)]      0           tf_op_layer_Reshape[0][0]        
__________________________________________________________________________________________________
tf_op_layer_Sub (TensorFlowOpLa [(None, 24, 21)]     0           tf_op_layer_Reshape[0][0]        
                                                                 tf_op_layer_Max[0][0]            
__________________________________________________________________________________________________
tf_op_layer_Exp (TensorFlowOpLa [(None, 24, 21)]     0           tf_op_layer_Sub[0][0]            
__________________________________________________________________________________________________
tf_op_layer_Sum (TensorFlowOpLa [(None, 24, 1)]      0           tf_op_layer_Exp[0][0]            
__________________________________________________________________________________________________
tf_op_layer_RealDiv (TensorFlow [(None, 24, 21)]     0           tf_op_layer_Exp[0][0]            
                                                                 tf_op_layer_Sum[0][0]            
==================================================================================================
Total params: 1,949,304
Trainable params: 1,949,304
Non-trainable params: 0
__________________________________________________________________________________________________
Epoch 1/10


Epoch 1/10
2020-12-19 10:24:20.109013: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcublas.so.10
10/10 [==============================] - 1s 77ms/step - loss: 2.7028
Epoch 2/10
10/10 [==============================] - 1s 74ms/step - loss: 1.8288
Epoch 3/10
10/10 [==============================] - 1s 73ms/step - loss: 1.4833
Epoch 4/10
10/10 [==============================] - 1s 73ms/step - loss: 1.2432
Epoch 5/10
10/10 [==============================] - 1s 70ms/step - loss: 0.9651
Epoch 6/10
10/10 [==============================] - 1s 71ms/step - loss: 0.7222
Epoch 7/10
10/10 [==============================] - 0s 48ms/step - loss: 0.5216
Epoch 8/10
10/10 [==============================] - 1s 72ms/step - loss: 0.3650
Epoch 9/10
10/10 [==============================] - 1s 70ms/step - loss: 0.2511
Epoch 10/10
10/10 [==============================] - 1s 73ms/step - loss: 0.1735
predicted peptide / true peptide
[['AAAGEEETAAAGSPGRK_______' 'AAAGEEETAAAGSPGRK_______']
 ['AAALASGCTVEIK___________' 'AAALASGCTVEIK___________']
 ['AAAVLRDSTSVPVTAEAK______' 'AAAVLRDSTSVPVTAEAK______']
 ['AADFLFSCDASHPDTLR_______' 'AADFLFSCDASHPDTLR_______']
 ['AADSSAPEDSEKLVGDTVSYSK__' 'AADSSAPEDSEKLVGDTVSYSK__']
 ['AAGHQADEILVPLDSK________' 'AAGHQADEILVPLDSK________']
 ['AAGLAGSDLITALISPTTR_____' 'AAGLAGSDLITALISPTTR_____']
 ['AAKEPEAVAVK_____________' 'AAKEPEAVAVK_____________']
 ['AAKIVTDVLLR_____________' 'AAKIVTDVLLR_____________']
 ['AALEQLLK________________' 'AALEQLLK________________']]

```