import pickle
import pandas as pd



def predict(modelfile,data):
    with open(modelfile, 'rb') as file:
        model = pickle.load(file)
    predictions = model.predict(data)
    return predictions