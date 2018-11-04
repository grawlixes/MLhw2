import numpy
import math

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

def q1():
    # ------------- part 1
    N = 200
    x = list(float(i-1)/(N-1) for i in range(1, N+1))
    y = list(math.sin(2*math.pi*x[i]) for i in range(len(x)))
    gwn = numpy.random.normal(0, 0.1, size=N)
    for i in range(N):
        y[i] += gwn[i]

    D = list((x[i], y[i]) for i in range(N))

    fig = plt.figure()
    ax = fig.add_subplot(111)

    sinusoidal_y = list(math.sin(2*math.pi*x[i]) for i in range(len(x)))
    ax.plot(x, sinusoidal_y)
    ax.plot(x, y, 'ro')

    # commented out because I don't want to generate this every test
#    name = raw_input("Finished plotting. What would you like to name the image? ")
#    fig.savefig(name)
#    print("Plot of data set D and sinusoidal function saved as " + name + '.')

    # ----------- part 2

    # Polynomial fitting for d in [1, 9].
    for d in range(2, 3+1):
        X = [[x[i]**j for j in range(d+1)] for i in range(len(x))]
        Xt = numpy.matrix.transpose(numpy.array(X))
        # x^t * x
        W = numpy.matmul(Xt, X)
        # (x^t * x)^-1
        W = numpy.linalg.inv(W)
        # x^t * y
        XtY = numpy.matmul(Xt, y)
        # final coefficient vector W
        W = numpy.matmul(W, XtY)
        Wt = numpy.matrix.transpose(W)
        pred = numpy.matmul(Wt, Xt)

        print("Coefficient vector for d = %i:" % d)
        print(W)
        print("Prediction vector for d = %i:" %d)
        print(pred)
        print("Mean squared error for d = %i:" %d)
        print(sum((pred[i]-y[i])**2 for i in range(len(pred))))

        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(x, pred)
        name = "asdf" + str(d) + ".png"
        fig.savefig(name)

def main():
    q1()

main()
