try:
    from AutoFeedback.funcchecks import check_func
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.funcchecks import check_func

from AutoFeedback.randomclass import randomvar
import unittest
from main import *

myp = np.array([[1,0,0,0,0],[1/3,1/3,1/3,0,0],[0,0.5,0,0.5,0],[0,0.5,0,0,0.5],[0,0,0,0,1]]) 
myq, myr = np.array([[1/3,1/3,0],[0.5,0,0.5],[0.5,0,0]]), np.array([[1/3,0],[0,0],[0,1/2]])
myprobs = np.dot( np.linalg.inv( np.identity(3) - myq ), myr )

class helper : 
   def test_mean( probs, start, n ) :
       m, e = sample_mean( probs, start, n )
       return m
 
   def test_var( probs, start, n ) :
       m, e = sample_mean( probs, start, n )
       return ( e / scipy.stats.norm.ppf(0.95) )**2 

class UnitTests(unittest.TestCase) :
   def test_markov_move(self) :      
       myvars, inputs, variables = np.array([0,1,2,3,4]), [], [] 
       for j in range(5) : 
           exp = np.dot( myp[j,:], myvars )
           var = var = np.dot( myp[j,:], myvars*myvars ) - exp*exp
           for i in range(10):
               inputs.append((myp,j,))
               myvar = randomvar( exp, variance=var, vmin=0, vmax=4, isinteger=True )
               variables.append( myvar )

       assert( check_func("markov_move", inputs, variables ) )

   def test_endstate(self) :
       inputs, variables = [], [] 
       for j in range(1,4) :
           for i in range(10) :
               inputs.append((myp,j,))
               p = myprobs[j-1,1]
               myvar = randomvar( p, variance=p*(1-p), vmin=0, vmax=1, isinteger=True )
               variables.append( myvar )
       assert( check_func("endstate", inputs, variables, calls=["markov_move"] ) )

   def test_mean(self) :
       ns, inputs, variables = 100, [], []
       for j in range(1,4) : 
           inputs.append((myp,j,ns,))
           p = myprobs[j-1,1]
           myvar = randomvar( p, variance=p*(1-p)/ns, vmin=0, vmax=1, isinteger=False )
           variables.append( myvar )
       assert( check_func("test_mean", inputs, variables, modname=helper ) )

   def test_var(self) :
       ns, inputs, variables = 100, [], []
       for j in range(1,4) : 
           inputs.append((myp,j,ns,))
           p = myprobs[j-1,1]
           myvar = randomvar( p, dist="chi2", variance=p*(1-p)/ns, isinteger=False )
           variables.append( myvar )
       assert( check_func("test_var", inputs, variables, modname=helper ) )
