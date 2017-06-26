import csv
import numpy
import copy
import math

def norm(matrix):
    maximum = matrix.max()
    minimum = matrix.min()
    norm = copy.copy(matrix)
    for row in norm:
        for value in row:
            value -= minimum
            value /=(maximum - minimum)
    return norm

def read(fileName, check):
    x = []
    with open(fileName, 'r') as f:
        reader = csv.reader(f, delimiter = ',', quoting=csv.QUOTE_NONE)
        for row in reader:
            tmpx = None
            if check == 1:
                tmpx = [1,]
            else:
                tmpx = []
            count = 0
            size = len(row)
            while (count < size):
                tmpx.append(float(row[count]))
                count+=1
            x.append(tmpx)
        return x

#transpTetta * x
def hypothesis(T, x):
    return numpy.dot(T, x.transpose())

def ErrorValue(T, X):
    i = 0
    res = open("Y_log.csv","a")
    while i < X.shape[0]:
        res.write (str(math.ceil(hypothesis(T, X[i, 0:])+0.5))+ '\n')
        #res.write (str(hypothesis(T, X[i, 0:]))+ '\n')
        i+=1
    res.close()

xtrain = read('testing_log.csv', 1)
Xtr = norm(numpy.matrix(xtrain))
T = read("thetta_log.csv", 0)
T = numpy.matrix(T)
print(Xtr)
print(T)
ErrorValue(T, Xtr)
