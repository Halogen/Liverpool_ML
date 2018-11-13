import csv
import numpy as np
# from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
# from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
#from sklearn import cross_validation
from sklearn.model_selection import cross_val_score
from SMOTE import *
import pandas as pd

key_prob = {}

def training_forest(X, Y):
    """
    X: inputs arraylike
    Y: target variable arraylike
    """
    best_acc = 0.0
    best_size = 0
    best_depth = 0
    #for depth in range(1, 10):
    for depth in [8,9,10]:
        #for size in [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]:
        for size in [40,60,80]:
            clf = RandomForestClassifier(n_estimators=size, max_depth=depth, n_jobs=6)
            scores = cross_val_score(clf, X, Y, cv=3)
            acc = scores.mean()
            print("size", size, ", depth:", depth, "acc:", acc)
            if acc > best_acc:
                best_acc = acc
                best_size = size
                best_depth = depth
    print("best size", best_size, ", best depth:", best_depth, "best acc", best_acc)
    ### get the best model
    clf = RandomForestClassifier(n_estimators=best_size, max_depth=best_depth, n_jobs=6)
    clf.fit(X, Y)
    return clf


