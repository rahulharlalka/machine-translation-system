from __future__ import print_function
from flask import Flask,request,url_for,redirect
import numpy as np
import pickle
import load_model 
import enc_dec_construct
app=Flask(__name__)



essentials,model = load_model.load_vars()    
encoder_model,decoder_model = enc_dec_construct.construct(model)
num_encoder_tokens=essentials['num_encoder_tokens']
num_decoder_tokens=essentials['num_decoder_tokens']
max_encoder_seq_length=essentials['max_encoder_seq_length']
max_decoder_seq_length=essentials['max_decoder_seq_length']
input_token_index=essentials['input_token_index']
target_token_index=essentials['target_token_index']
reverse_input_char_index=essentials['reverse_input_char_index']
reverse_target_char_index=essentials['reverse_target_char_index']
    

def decode_sequence(input_seq):
    states_value = encoder_model.predict(input_seq)

    target_seq = np.zeros((1, 1, num_decoder_tokens))
    target_seq[0, 0, target_token_index['\t']] = 1.
    
    stop_condition = False
    decoded_sentence = ''
    while not stop_condition:
        output_tokens, h, c = decoder_model.predict([target_seq] + states_value)

        sampled_token_index = np.argmax(output_tokens[0, -1, :])
        sampled_char = reverse_target_char_index[sampled_token_index]
        decoded_sentence += sampled_char

        if (sampled_char == '\n' or
           len(decoded_sentence) > max_decoder_seq_length):
            stop_condition = True

        # Update the target sequence (of length 1).
        target_seq = np.zeros((1, 1, num_decoder_tokens))
        target_seq[0, 0, sampled_token_index] = 1.

        # Update states
        states_value = [h, c]

    return decoded_sentence

def get_encoder_input_data(input_texts):
    #print(input_texts[0])
    encoder_input_data = np.zeros((len(input_texts), max_encoder_seq_length, num_encoder_tokens),dtype='float32')
    for i , input_text in enumerate(input_texts):
        for t,char in enumerate(input_text):
            encoder_input_data[i, t, input_token_index[char]] = 1.
        encoder_input_data[i, t + 1:, input_token_index[' ']] = 1.
    return encoder_input_data



@app.route('/translate',methods=["POST"])
def get_sentence():
    sentence=str(request.form['english'])    
    encoder_input_data=get_encoder_input_data([sentence])
    #print(encoder_input_data.shape)
    decoded_sentence=str(decode_sequence(encoder_input_data))
    #print(decoded_sentence)
    return decoded_sentence



@app.route('/')
def default():
    return "logged into wrong page : log into http://localhost:5000/translate"

if __name__=='__main__':     
    app.run(debug=True)
    
