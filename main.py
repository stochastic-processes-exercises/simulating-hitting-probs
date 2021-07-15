import matplotlib.pyplot as plt
import scipy.stats
import numpy as np


def markov_move( trans, start ) :
    myrand, myvar, accum  = np.random.uniform(0,1), 0, trans[start,0]
    while myrand>accum : 
          myvar = myvar + 1
          accum = accum + trans[start,myvar]
    return myvar

def endstate( trans, start ) :
    while start!=0 and start!=4 :
       start = markov_move( trans, start )
    if start==0 : return 0
    return 1

def sample_mean( trans, start, nsamples ) :
    m = 0 
    for i in range(nsamples) : m = m + endstate( trans, start )
    mean = m / nsamples 
    var = mean*(1-mean)
    conf = np.sqrt( var / nsamples )*scipy.stats.norm.ppf(0.95)
    return mean, conf

# Setup the transition matrix here
A = np.array([[1,0,0,0,0],[1/3,1/3,1/3,0,0],[0,0.5,0,0.5,0],[0,0.5,0,0,0.5],[0,0,0,0,1]])


# Now estimate some hitting probablities if we start from state 2
prob, conf = sample_mean( A, 1, 100 )
print("There is a 90% probablity that the conditional probablity of finishing in state 5 given you start in state 2 is within", conf, "of", prob )
prob, conf = sample_mean( A, 2, 100 )
print("There is a 90% probablity that the conditional probablity of finishing in state 5 given you start in state 3 is within", conf, "of", prob )
prob, conf = sample_mean( A, 3, 100 )
print("There is a 90% probablity that the conditional probablity of finishing in state 5 given you start in state 4 is within", conf, "of", prob )
