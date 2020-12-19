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
2020-12-19 09:24:26.244862: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcublas.so.10
10/10 [==============================] - 1s 76ms/step - loss: 2.7299
Epoch 2/10
10/10 [==============================] - 1s 74ms/step - loss: 1.8542
Epoch 3/10
10/10 [==============================] - 1s 73ms/step - loss: 1.4939
Epoch 4/10
10/10 [==============================] - 1s 69ms/step - loss: 1.2622
Epoch 5/10
10/10 [==============================] - 1s 71ms/step - loss: 0.9860
Epoch 6/10
10/10 [==============================] - 1s 72ms/step - loss: 0.7406
Epoch 7/10
10/10 [==============================] - 1s 73ms/step - loss: 0.5358
Epoch 8/10
10/10 [==============================] - 1s 73ms/step - loss: 0.3759
Epoch 9/10
10/10 [==============================] - 1s 69ms/step - loss: 0.2596
Epoch 10/10
10/10 [==============================] - 1s 59ms/step - loss: 0.1800

['AAAGEEETAAAGSPGRK_______' 'AAALASGCTVEIK___________'
 'AAAVLRDSTSVPVTAEAK______' 'AADFLFSCDASHPDTLR_______'
 'AADSSAPEDSEKLVGDTVSYSK__' 'AAGHQADEILVPLDSK________'
 'AAGLAGSDLITALISPTTR_____' 'AAKEPEAVAVK_____________'
 'AAKIVTDVLLR_____________' 'AALEQLLK________________'
 'AAPAPATAASTTSSSSTSLSSSSK' 'AAPLAPLPAP_P____________'
 'AAPLIVEVFNK_____________' 'AAQSTGAWILTSALR_________'
 'AASEELLEK_______________' 'AASSSSSSAGGVSGSSVTGSGFSV'
 'AAVEFNK_________________' 'AAVLQELATHLHPAEPEEGDSNVA'
 'AAVPLPPR________________' 'ACDGNVDHAATHITNR________'
 'ACIDSNEDGDLSK___________' 'ACLEEHIR________________'
 'ACQLPSEWRPLS_GCR________' 'ADDDYKDYGVNCDK__________'
 'ADEAALALQPGGSPSAAGADR___' 'ADLEWLR_________________'
 'ADLIKQDFYYFPSVSK________' 'ADLNKPLYIDTK____________'
 'ADLVISHAGAGSCLETLEK_____' 'ADVLSSFLDEK_____________'
 'AEALAAVDIVSHGKNHPFK_____' 'AEGATAPIK_______________'
 'AEIQDQHDEYIR____________' 'AENYDIPSADR_____________'
 'AEPLSCALDDSSDSQDPTKEIR__' 'AEQVLLEQLDEDGGCRR_______'
 'AERPEDLNLPNAVITR________' 'AESVEREIQYVK____________'
 'AETRCEPFTMK_____________' 'AEVRPRSALGSSR___________'
 'AFASATNYK_______________' 'AFEEAYARADK_____________'
 'AFGLLDARVTWALR__________' 'AFIQMSNLVR______________'
 'AFIWPSTLTKHK____________' 'AFIWSSVLTRHK____________'
 'AFLLSLAALR______________' 'AFLSPPTLLEGPL___________'
 'AFNRSTDLTTHK____________' 'AFRFSASPGCGRPSSNK_______'
 'AFRQSATLNK______________' 'AFRSSNYIR_______________'
 'AFSLASSLR_______________' 'AFSQRSGLFQHQR___________'
 'AFTFSSTLNTHK____________' 'AFTQYSGLSMHVRSHSGDK_____'
 'AFYCSSNLIQNNIVHAEEKHYK__' 'AGAAGTAEATAR____________'
 'AGDNILAVLK______________' 'AGFLSLPK________________'
 'AGGALCHILGAAYK__________' 'AGGLLVIDHR______________'
 'AGIMPFLK________________' 'AGLHPPDSQASGQGVPLISVTTLR']

```