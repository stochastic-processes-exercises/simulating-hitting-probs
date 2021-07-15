import matplotlib.pyplot as plt
import scipy.stats
import numpy as np


def markov_move( trans, start ) :


def endstate( trans, start ) :


def sample_mean( trans, start, nsamples ) :

    return mean, conf

# Setup the transition matrix here
A = 


# Now estimate some hitting probablities if we start from state 2
prob, conf = sample_mean( A, 1, 100 )
print("There is a 90% probablity that the conditional probablity of finishing in state 5 given you start in state 2 is within", conf, "of", prob )
prob, conf = sample_mean( A, 2, 100 )
print("There is a 90% probablity that the conditional probablity of finishing in state 5 given you start in state 3 is within", conf, "of", prob )
prob, conf = sample_mean( A, 3, 100 )
print("There is a 90% probablity that the conditional probablity of finishing in state 5 given you start in state 4 is within", conf, "of", prob )
