from flask import Flask,request,url_for,redirect
from __future__ import print_function
import numpy as np
import pickle,pylint
import load_model 
import enc_dec_construct
app=Flask(__name__)

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


def load_defaults():
    global essentials,model=load_model.load_vars()    
    global encoder_model,decoder_model = enc_dec_construct.construct(model)
    global num_encoder_tokens=essentials['num_encoder_tokens']
    global num_decoder_tokens=essentials['num_decoder_tokens']
    global max_encoder_seq_length=essentials['max_encoder_seq_length']
    global max_decoder_seq_length=essentials['max_decoder_seq_length']
    global input_token_index=essentials['input_token_index']
    global target_token_index=essentials['target_token_index']
    global reverse_input_char_index=essentials['reverse_input_char_index']
    global reverse_target_char_index=essentials['reverse_target_char_index']
    del essentials




@app.route('/translate' ,methods=["POST"])
def hello_world():
    return 'code under maintainance'

if __name__=='__main__':
    load_defaults()
    


    app.run(debug=True)
    
