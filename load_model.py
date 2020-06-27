from __future__ import print_function
import tensorflow
import pickle


def load_vars():
    f= open('essentials.pkl','rb')
    essentials=pickle.load(f)
    f.close()    
    model=tensorflow.keras.models.load_model('model.h5')    
    return essentials,model 


