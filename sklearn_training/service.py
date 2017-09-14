#!/usr/bin/env python3
"""
Training:0.0.1-SNAPSHOT Service
"""
import nstack
from sklearn.linear_model import SGDClassifier
import numpy as np

class Service(nstack.BaseService):
    def __init__(self):
        '''
        Here we perform any tasks that only need to be done once, on
        initialisation of the module. In this example, that's only
        calling super().__init__() and initialising the model.
        '''
        
        # The following line is necessary to initialise the module
        # correctly.
        super().__init__()
        
        # Initialise the model. Set loss to 'log' in order to have a
        # `predict_proba` method.
        self.model = SGDClassifier(loss='log')
    
    def process(self, features):
        '''
        This is the function that actually trains or runs the model on a
        given input vector. This name must match the one in module.nml.
        '''

        # We need to convert from a list to a numpy array,
        # because NStack does not (yet) have tensor types.
        # In addition, we reshape to (1, -1) because scikit-learn
        # doesn't like 1D arrays.
        X = np.array(features).reshape(1,-1)

        # X will contain either 31 or 30 elements, depending on whether
        # we want to be running training or inference respectively. In
        # training mode, the extra element is taken to be the target.
        if X.shape[1] == 31:
            # Assume X[0,-1] is a training value.
            # Since we only use partial_fit, we need to pass all
            # classes in the dataset the first time it's called. For
            # subsequent calls the classes kwarg will be ignored.
            classes = np.array([0.0, 1.0])
            # We index over "all" the rows of X even though we know it
            # only has one row, because that generates the arrays of
            # shape(1,N) that sklearn likes. (otherwise would have to
            # insert calls to .reshape().)
            self.model.partial_fit(X[:,:-1], X[:,-1], classes=classes)
            
            # As no output is produced from training (only the internal
            # state is changed), yield an empty list.
            yield []

        elif X.shape[1] == 30:
            # Assume this means we want to do inference.
            # select element [0,1] since that is the probability of the
            # positive class, and wrap in a list to make the output
            # type be [Double].
            yield [self.model.predict_proba(X)[0,1]]

        else:
            raise ValueError("Wrong shape of argument, need 30 or 31,"\
                             " got " + X.shape[1])
        return
