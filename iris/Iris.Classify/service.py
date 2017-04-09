#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
irisclassify Service
"""
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

import nstack

class Service(nstack.BaseService):
    def __init__(self):
        """Initialise and train the classifier"""
        super().__init__()
        train = pd.read_csv("./train.csv")
        
        self.cols = ['petal_length', 'petal_width', 'sepal_length', 'sepal_width'] 
        train_arr = train.as_matrix(self.cols) # training array
        train_res = train.as_matrix(['class']) # training results
        
        self.rf = RandomForestClassifier(n_estimators=100) # initialize
        self.rf.fit(train_arr, train_res) # fit the data to the algorithm

    def predict(self, input_row):
        """Classify and return the particular iris based on the input values"""
        df = pd.DataFrame([input_row], columns=self.cols)
        results = self.rf.predict(df)
        return results.item()

