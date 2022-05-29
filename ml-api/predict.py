import joblib
import numpy


def predict(data):
    model_loaded = joblib.load('gbmodel.pkl')
    sample = numpy.asarray(data)
    sample = sample.reshape(1, -1)
    predicted = model_loaded.predict(sample)
    return predicted