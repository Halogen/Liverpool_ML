import csv
import numpy as np
import nltk
from nltk.stem.porter import *
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score, confusion_matrix, mean_squared_error, r2_score
#from sklearn import cross_validation
from sklearn.model_selection import cross_val_score
from SMOTE import *
import pandas as pd
import sys


def process_data_pd():
	data = pd.read_csv("data/swslhd_comp_stat_no_doc.csv")

	data2 = data[['FRE_WT', 'FRE_APPT', 'GENDER', 'AGE',
       'SUBURB', 'STATE', 'POSTCODE', 'LAT', 'LON', 'HOSP_LAT',
	   'HOSP_LON','HOSP_DIST', 'LOC_FACILITY_CD_DISPLAY',
	   'PLANNED_PROCEDURE_DISPLAY','WAIT_DUR']].dropna()

	data2 = data2.reset_index().drop("index", axis = 1)
	data2.WAIT_DUR = data2.WAIT_DUR.apply(lambda x: float(x.split()[0]))

	data2 = data2[data2.WAIT_DUR < 4000]
	data2 = data2[data2.WAIT_DUR > 0]
	catagorical = ['GENDER', 'SUBURB', 'STATE', 'POSTCODE',
		'LOC_FACILITY_CD_DISPLAY', 'PLANNED_PROCEDURE_DISPLAY']

	values_dict = {}
	for column in catagorical:
    	# get frequencies
		freq = list(reversed(data2[column].value_counts().index))
    	#print(freq)
    	# add catagories to values dictionary
		values_dict[column] = dict(enumerate(freq))

    	# make numeric based of frequencies
		data2[column] = to_num_cat(data2[column], freq)
	return data2.astype('float')

# convert a catagorical column to numerical, numbered from most frequent to least frequent
def to_num_cat(column, freq):
    return (column.astype('category', catagories=freq).cat.codes).astype('category')

def gen_data_set_with_smote(pos_data):
	synthetic_data = SMOTE(pos_data, 20000, 10)
	new_pos_data = np.concatenate((pos_data, synthetic_data))
	return new_pos_data

def training_forest(data, labels):
	best_acc = 0.0
	best_size = 0
	best_depth = 0
	labels = np.ravel(labels)
	for depth in range(1, 10):
	#print(type(data))
	#print(type(labels))
	#for depth in [8,9,10]:
		for size in [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]:
		#for size in [40,60,80]:
			clf = RandomForestRegressor(n_estimators=size, max_depth=depth)#, n_jobs=6)
			scores = cross_val_score(clf, data, labels,cv=3)
			#print(scores[0])
			acc = abs(scores.mean())
			print("size", size, ", depth:", depth, "acc:", acc)
			if acc > best_acc:
				best_acc = acc
				best_size = size
				best_depth = depth
	print("best size", best_size, ", best depth:", best_depth, "best acc", best_acc)
	clf = RandomForestRegressor(n_estimators=best_size, max_depth=best_depth, n_jobs=6)
	clf.fit(data, np.asarray(labels))
	return clf

def test_forest(model, test_data):
	res = model.predict(test_data)
	print('Predicted values:', res)
	return res

def output_res_new(data):
	data['prob'] = data['key'].map(key_prob)
	data.to_csv('data/res.csv')



def main():
	test_size = 100
	dt = process_data_pd()
	#pos_data, neg_data = text2vec()
	print('Running SMOTE... to rebalance')
	new_data = gen_data_set_with_smote(dt.values)
	#new_data = dt.values
	#print(new_data)
	print('New positive data size:', new_data.shape[0])
	#data = np.concatenate((new_pos_data, neg_data))
	column_num = new_data.shape[1]
	X, y = np.split(new_data, [column_num - 1], 1)
	X_train, X_test = np.split(X, [test_size], 0)
	y_train, y_test = np.split(y, [test_size], 0)

	#print(X_train.shape)
	#print(X_test.shape)
	#print(y_train.shape)
	#print(y_test.shape)

	print('Training Random Forest...')
	model = training_forest(X_train, y_train)

	res = test_forest(model, X_test)

	final = res.reshape((res.shape[0],1))
	y_test = y_test.reshape((y_test.shape[0],1))
	print('Write result to file...')
	results = pd.DataFrame(final, columns = ["predicted"])
	results["actual"] = y_test
	results.to_csv("results.csv")

	print("Mean squared error: %.2f"
	      % mean_squared_error(y_test, res))

	#output_res_new(dt)


if __name__ == '__main__':
	main()
