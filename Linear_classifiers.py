"""
Author: CHANDRAMOHAN T N
File: Accuracy_measures.py 
"""

from sklearn.neighbors import KNeighborsClassifier
from scipy import linalg
import sklearn.metrics
import numpy
import Accuracy_measures

# Classification using k-NN
def KNN(x_train, y_train, k, x_test, y_test):
    neigh = KNeighborsClassifier(k)
    neigh.fit(x_train, y_train)
    KNeighborsClassifier()
    y_hat = neigh.predict(x_test)
    print('Accuracy: ' + str(sklearn.metrics.accuracy_score(y_test, y_hat)))
    print('Precision: ' + str(sklearn.metrics.precision_score(y_test, y_hat)))
    print('Recall: ' + str(sklearn.metrics.recall_score(y_test, y_hat)))
    print('F1-score: ' + str(sklearn.metrics.f1_score(y_test, y_hat)))

# Linear regression
def Regression(x, y):
    one = numpy.array([[1]] * len(y))
    x = numpy.append(one, x, 1)
    xt = numpy.transpose(x)
    beta = numpy.linalg.solve(xt.dot(x), xt.dot(y))
    return beta

# Ridge regression
def Ridge_regression(x, y):
    xt = numpy.transpose(x)
    beta0 = sum(y) / len(y)
    lmbda = 0.000001
    ind = numpy.identity(len(x[0]))
    ones = numpy.array([[1]] * len(y))
    x1 = numpy.append(ones, x, 1)
    beta = numpy.linalg.solve((xt.dot(x) + lmbda * ind), xt.dot(y))
    beta = beta.tolist()
    beta = [beta0] + beta
    beta = numpy.array(beta)
    return beta

