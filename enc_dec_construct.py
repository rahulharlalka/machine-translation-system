from __future__ import print_function
import pylint
import tensorflow as tf 

def construct(model):
    latent_dim=256
    encoder_inputs = model.input[0]   
    _, state_h_enc, state_c_enc = model.layers[2].output  
    encoder_states = [state_h_enc, state_c_enc]
    encoder_model = tf.keras.models.Model(encoder_inputs, encoder_states)

    decoder_inputs = model.input[1]   
    decoder_state_input_h = tf.keras.layers.Input(shape=(latent_dim,), name='input_3')
    decoder_state_input_c = tf.keras.layers.Input(shape=(latent_dim,), name='input_4')
    decoder_states_inputs = [decoder_state_input_h, decoder_state_input_c]
    
    decoder_lstm = model.layers[3]
    decoder_outputs, state_h_dec, state_c_dec = decoder_lstm(decoder_inputs, initial_state=decoder_states_inputs)
    decoder_states = [state_h_dec, state_c_dec]
    decoder_dense = model.layers[4]
    decoder_outputs = decoder_dense(decoder_outputs)
    decoder_model = tf.keras.models.Model([decoder_inputs] + decoder_states_inputs,[decoder_outputs] + decoder_states)
    
    return encoder_model,decoder_model
