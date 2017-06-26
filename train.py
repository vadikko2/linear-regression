import csv
import numpy
import random
import copy
import matplotlib.pyplot as plt

def norm(matrix):
    maximum = matrix.max()
    minimum = matrix.min()
    norm = copy.copy(matrix)
    for row in norm:
        for value in row:
            value -= minimum
            value /=(maximum - minimum)
    return norm
#transpTetta * x
def hypothesis(T, x):
    return numpy.dot(T, x.transpose())

def recount(T, alpha,X, Y):
    newT = [[]]
    #alpa*(1/m)
    j = 0
    while j < T.shape[1]:
        i = 0
        _sum = 0
        while i < X.shape[0]:
            _sum += (hypothesis(T, X[i, 0:]) - Y.item(i))*X.item(i, j)
            i+=1
        newT[0].append(T.item(j) - (_sum*(alpha[j]/X.shape[0])).item())
        j+=1
        #newT.append(newt.item)
    return numpy.matrix(newT)

def ErrorValue(T, X, Y):
    _sum = 0;
    i = 0
    while i < X.shape[0]:
        _sum+=abs(hypothesis(T, X[i, 0:]) - Y.item(i))
        i+=1

    return _sum / (2*X.shape[0])

def writeThetta(thetta, f):
    i = 0
    while i < thetta.shape[1]:
        f.write(str(thetta[0, i]) + ',')
        i+=1
    f.write('\n')
def read(fileName):
    x = []
    y = []
    with open(fileName, 'r') as f:
        reader = csv.reader(f, delimiter = ',', quoting=csv.QUOTE_NONE)
        for row in reader:
            tmpx = [1,]
            tmpy = []
            count = 0
            size = len(row)
            while (count < size):
                if(count != size - 1):
                    tmpx.append(float(row[count]))
                else:
                    tmpy.append(float(row[count]))
                count+=1
            x.append(tmpx)
            y.append(tmpy)
        return x, y

xtr, ytr = read('train_log.csv')
xtest, ytest = read('test_log.csv')
#матрицы X, Y
Xtr = norm(numpy.matrix(xtr))
Ytr = numpy.matrix(ytr)
Xtest = norm(numpy.matrix(xtest))
Ytest = numpy.matrix(ytest)
#случайное заполнение Tetta
t = [0,]
i = 0
while i < Xtr.shape[1]-1:
    t.append(random.uniform(-1,1))
    i+=1
T = numpy.matrix(t)
#T = numpy.matrix([random.random() for i in range(Xtr.shape[1])])
#T = numpy.matrix(random.sample(range(0, 101), Xtr.shape[1]))
print("X\n",Xtr)
print("Y\n",Ytr)
print("tetta\n",T)
fcsv = open('resultErrors.csv', 'w')
f = open('resultT.csv', 'w')
alpha = [1.3333333333333333, 4.0, 0.8888888888888888, 2.0, 1.6, 1.1428571428571428, 1.0, 8.0, 1.0, 4.0, 1.6, 1.6, 2.6666666666666665, 1.1428571428571428, 1.6, 2.6666666666666665, 2.0, 8.0, 4.0, 1.3333333333333333, 1.1428571428571428, 8.0, 1.0, 0.8888888888888888, 1.3333333333333333]
i = 0
#A
 #[1.3333333333333333, 4.0, 0.8888888888888888, 2.0, 1.6, 1.1428571428571428, 1.0, 8.0, 1.0, 4.0, 1.6, 1.6, 2.6666666666666665, 1.1428571428571428, 1.6, 2.6666666666666665, 2.0, 8.0, 4.0, 1.3333333333333333, 1.1428571428571428, 8.0, 1.0, 0.8888888888888888, 1.3333333333333333]

'''while i < 25:
    alpha.append(8)
    i+=1

j = 0
while j < len(alpha):
    alpha[j] /= random.sample(range(1, 10), 1)[0]
    j+=1
'''
t = 1
error = ErrorValue(T, Xtr, Ytr)
print("L = ",error)
errors = []
errorsTest = []
errorTest = ErrorValue(T, Xtest, Ytest)
while  t < 10:
    T = recount(T, alpha, Xtr, Ytr)
    j = 0
    while j < len(alpha):
        if errorTest < 80:
            if(alpha[j] > 0.08):
                if j%3 == 0:
                    alpha[j] /= 10
                else:
                    alpha[j]/= 10
            #alpha[j] /= random.sample(range(1, 5), 1)[0]
        j+=1
    print("A\n", alpha)
    #print(a) for a in alpha
    print("T\n", T)
    #f.write(str(T)+'\n')
    writeThetta(T, f)
    print("L = ",error)
    print("LTest = ",errorTest)
    fcsv.write(str(errorTest[0,0]) +'\n')
    errors.append(error[0,0])
    errorsTest.append(errorTest[0,0])
    t+=1
    error = ErrorValue(T, Xtr, Ytr)
    errorTest = ErrorValue(T, Xtest, Ytest)
f.close()
plt.plot(errors)
plt.plot(errorsTest)
plt.ylabel('errors')
plt.show()
