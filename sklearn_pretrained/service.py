#!/usr/bin/env python3
"""
Propensity:0.0.1-SNAPSHOT Service
"""
import nstack
from sklearn.externals import joblib
import numpy as np

class Service(nstack.BaseService):
    def __init__(self):
        '''
        Here we perform any tasks that only need to be done
        once, on initialisation of the module. In this example,
        that's only calling super().__init__() and loading the
        pre-trained model.
        '''
        
        # The following line is necessary to initialise the module
        # correctly.
        super().__init__()
        
        self.model = joblib.load('propensitymodel.pkl')
    
    def get_propensity(self, features):
        '''
        This is the function that actually runs the model on a
        given input vector. This name must match the one in
        module.nml.
        '''
        
        # We need to convert from a list to a numpy array,
        # because NStack does not (yet) have tensor types.
        # In addition, we reshape to (1, N) because scikit-learn
        # doesn't like 1D arrays (N is the number of features).
        X = np.array(features).reshape(1,-1)
        pred = self.model.predict_proba(X)
        
        # This model returns an array of probabilities (one for
        # each class), we will return only the probability of a
        # positive outcome, so the second element.
        return pred[0,1]
