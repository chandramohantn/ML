"""
Author: CHANDRAMOHAN T N
File: Accuracy_measures.py 

y_in: Actual output
y_out: Predicted output
k: Class label of that particular class whose Precision, Recall and F-scores are to be computed.
"""

def RSS(y_in, y_out):
    i = 0
    res = 0.0
    while i < len(y_out):
        res += (y_in[i] - y_out[i]) * (y_in[i] - y_out[i])
        i += 1
    #print('Residual Sum of Squares: ' + str(res * 1.0 / len(y_in)))
    return res * 1.0 / len(y_in)

def Accuracy(y_in, y_out):
    n = len(y_in)
    acc = 0
    for i in range(n):
        if y_in[i] == y_out[i]:
            acc += 1
    #print('Accuracy: ' + str(acc * 1.0 / n))
    return acc * 1.0 / n

def Precision(y_in, y_out, k):
    tp = 0
    fp = 0
    for j in range(len(y_in)):
        if y_in[j] == y_out[j] == k:
            tp = tp + 1
        elif y_out[j] == k and y_out[j] != y_in[j]:
            fp = fp + 1
    prec = tp * 1.0 / (tp + fp)
    #print('Precision: ' + str(prec))
    return prec

def Recall(y_in, y_out, k):
    tp = 0
    fn = 0
    for j in range(len(y_in)):
        if y_in[j] == y_out[j] == k:
            tp = tp + 1
        elif y_in[j] == k and y_out[j] != y_in[j]:
            fn = fn + 1
    recal = tp * 1.0 / (tp + fn)
    #print('Recall: ' + str(recal))
    return recal

def F1_measure(y_in, y_out, k):
    prec = Precision(y_in, y_out, k)
    recal = Recall(y_in, y_out, k)
    f_meas = prec * recal * 2.0 / (prec + recal)
    #print('Precision: ' + str(prec))
    #print('Recall: ' + str(recal))
    #print('F1_measure: ' + str(f_meas))
    return f_meas
