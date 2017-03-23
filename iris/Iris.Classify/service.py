#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
irisclassify Service
"""
import nstack
import pandas as pd

from sklearn.ensemble import RandomForestClassifier

class Service(nstack.BaseService):
    def __init__(self):
        train = pd.read_csv("train.csv")
        
        self.cols = ['petal_length', 'petal_width', 'sepal_length', 'sepal_width'] 
        colsRes = ['class']
        trainArr = train.as_matrix(self.cols) #training array
        trainRes = train.as_matrix(colsRes) # training results
        
        rf = RandomForestClassifier(n_estimators=100) # initialize
        rf.fit(trainArr, trainRes) # fit the data to the algorithm
        self.rf = rf

    def predict(self, inputArr):
        points = [inputArr]
        df = pd.DataFrame(points, columns=self.cols)

        results = self.rf.predict(df)
        return results.item()

