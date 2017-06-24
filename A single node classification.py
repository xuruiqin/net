"""The one layer Perceptron can only be used to linear divisible problems. The eight points on the vertex of
a cube can be seperated by a plane"""
import numpy as np
# The last element of each training data is minus one
X= [[0,0,0,-1],[0,1,1,-1],[0,1,0,-1],[0,0,1,-1],[1,1,0,-1],[1,0,1,-1],[1,1,0,-1],[1,1,1,-1]]
# Some points are labeled by -1, others are 1
label=[-1,1,-1,-1,-1,1,-1,1]
# the weight and threshold value are set to random numbers between 1 and 1
import random
W=[]
for i in range(4):
    W.append(random.uniform(-1,1))
print("The original weight is:",W)
# The activation function is double polarization step function
def activation(x):
    if x>=0:
        return 1
    else:
        return -1
# for non-linear problem
#def actication(x):
#    return 1/(1+np.exp(-x))
# process of learning
# total is the list of activation value
total=0.0
for i in range(8):
    for j in range(4):
            total+=X[i][j]*W[j]
    delta=activation(total)
    for j in range(4):        
            W[j]+=0.11*(label[i]-delta)*X[i][j]
    print("Now",i,"weight is",W)
# I hava get new weights after training, now let's test is. The outcome must comform to X and label
test=[0]*4
n=0.0
for m in range(3):
    test[m]=input("Please input the coordinate:")
    test[m]=int(test[m])
test[3]=-1
for m in range(4):
    n+=test[m]*W[m]
outcome=activation(n)
print("My neural network's prediction of your input is:", outcome)




