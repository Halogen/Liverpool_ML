import csv
import numpy as np
import nltk
from nltk.stem.porter import *
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.feature_extraction import DictVectorizer
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

def test_forest(model, test_data):
    res = model.predict(test_data)
    #print('Predicted labels:', res)
    res = model.predict_proba(test_data)
    # print res
    prob = res[:,1]
    #print('Predicted probabilities:', prob)
    # res = np.argsort(prob)
    # print res[::-1]
    keys = positive_keys + negative_keys
    for i in range(len(keys)):
        key_prob[keys[i]] = prob[i]
    # print key_prob


def output_res_new(data):
    data['prob'] = data['key'].map(key_prob)
    data.to_csv('data/res.csv')



def main():
    dt = process_data_pd()
    pos_data, neg_data = text2vec()
    print('Running SMOTE... to rebalance')
    new_pos_data = gen_data_set_with_smote(pos_data)
    print('New positive data size:', new_pos_data.shape[0])
    data = np.concatenate((new_pos_data, neg_data))
    label = ['1']*new_pos_data.shape[0] + ['0']*neg_data.shape[0]
    print('Training Random Forest...')
    model = training_forest(data, label)

    test_data = np.concatenate((pos_data, neg_data))
    test_forest(model, test_data)
    print('Write result to file...')
    output_res_new(dt)


if __name__ == '__main__':
    main()






