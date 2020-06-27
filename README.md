# MACHINE TRANSLATION SYSTEM

## machine translation system is a machine learing model in which machine learning is used and text in one language is conevrted into text to another language

In this repository,
    English language has been converted to its corresponding french language. The machine learning model uses encoder-decoder sequence to sequence 
model to perform predictions.
The fra.txt file contains the dataset for the model training .

essential.pkl is a pkl file which stores the important variables and items required to preform predictions

index.html is the basic web page for taking english sentence input and sending it to server .

the server.py is the server file built using flask which contains the model , recieves the input text and performs prediction and returns it to redirected page

model.h5 contains the weights of the trained machine learing model
load_model.py and enc_dec_construct.py file contain necessary functions and file to run predictions

To preform prediction,
1. clone the repository
2. download all the required python libraries
3. open terminal in the folder and run " python server.py "
4. then open the index.html page file and input text and hit submit button
5. you will recieve the predictions for your input