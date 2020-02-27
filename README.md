# NLP Coursework
In this coursework we predict the quality of machine translated sentences for English to Chinese language pairs. 

## The coursework code
Our code for the coursework is in NLP_cw.ipynb, where we developed BERT pre-processing and 5 regression models. We keep the output for each cell. Note that if you run the code, the SVM and Random Forest may take a long training time. In addition, the LSTM and FFNN share the training(), testing() and regression() function, currently these functions are set for LSTM, if you want to switch to FFNN, please follow the comments in these 3 functions to do comment/uncomment operations for some statements.

## Other code (low quality models)
The Baseline.ipynb contains our attempt to use pre-trained embedding, if you want to run this file, please first upload stopwords_ch.txt, which is our self-made Chinese stop words list.

