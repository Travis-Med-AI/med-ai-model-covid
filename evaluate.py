import numpy as np
from fastai.vision import load_learner
import numpy as np


def evaluate(imgs):
    model = load_learner('.', 'covid_inference.pkl')
    data_classes = ['Covid-19', 'No_findings', 'Pneumonia']
 
    return np.array([model.predict(img)[0].obj for img in imgs])
