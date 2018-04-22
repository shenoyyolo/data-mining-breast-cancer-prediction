import numpy as np
from sklearn import preprocessing, model_selection, tree, metrics
import pandas as pd
from sklearn import svm


import time
start_time = time.time()

dataFrame = pd.read_csv('/Users/Vikram/Documents/Projects/Data-Mining-Breast-Cancer/data/breast-cancer-wisconsin.data',
                       names = ['id','clump_thickness', "unif_cell_size", "unif_cell_shape", "marg_adhesion", "single_epith_cell_size", "bare_nuclei", "bland_chrom", "norm_nucleoli", "mitoses", "class"])


#Drop missing data values
dataFrame.replace('?',np.nan, inplace=True)
dataFrame.dropna(0,'any',inplace=True)


#Drop the ID column
dataFrame.drop(['id'],1,inplace=True)


#Separate attributes and class
X = np.array(dataFrame.drop('class',1))
y = np.array(dataFrame['class'])

#Set up 10 fold cross-validation
kf = model_selection.KFold(n_splits = 10);
globalAccuracy = 0.0

print(len(X))

clf = svm.SVC(kernel='poly',degree=3)



for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    #print(train_index)
    print("--------")
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_train)

    misclassified_samples = X_test[y_test != y_pred]
    print(len(misclassified_samples))

    accuracy = clf.score(X_test, y_test)
    metrics.confusion_matrix(y_test, y_pred)
    print(metrics.classification_report(y_test, y_pred))
    globalAccuracy+=accuracy
    print(accuracy)

print()
print()
print()
print(globalAccuracy/10)

print(time.time() - start_time)