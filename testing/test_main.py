try:
    from AutoFeedback.plotchecks import check_plot
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.plotchecks import check_plot

from AutoFeedback.plotclass import line
from AutoFeedback.funcchecks import check_func
from AutoFeedback.randomclass import randomvar
from scipy.stats import binom
import unittest
from main import *

class errclass : 
   def get_error(i) : 
       from scipy.stats import norm
       return ( error[i] / norm.ppf(0.95) )**2

class UnitTests(unittest.TestCase) :
    def test_binom(self) :
        inputs, variables = [], []
        for n in range(3,6) :
            for i in range(1,9) :
                p = i*0.1
                inputs.append((n,i*0.1,))
                myvar = randomvar( n*p, variance=n*p*(1-p), vmin=0, vmax=n, isinteger=True )
                variables.append( myvar )
        assert( check_func('binomial',inputs, variables ) ) 

    def test_error(self) :
        inputs, variables = [], [] 
        for i in range(6) :
            inputs.append((i,))
            pval = binom.pmf(i, 5, 0.5 )
            myvar = randomvar( pval, dist="chi2", variance=pval*(1-pval)/nsamples, isinteger=False)
            variables.append( myvar )
        assert( check_func("get_error", inputs, variables, modname=errclass ) )  

    def test_plot(self) :
        x, e, var, bmin, bmax, isi  = [], [], [], [], [], []
        for i in range(6) :
            x.append(i)
            pval = binom.pmf(i, 5, 0.5 )
            e.append(pval)
            var.append(pval*(1-pval)/nsamples)
            bmin.append(0)
            bmax.append(1)
            isi.append(False)
        
        val = randomvar( e, variance=var, vmin=bmin, vmax=bmax, isinteger=isi )
        line1=line( x, val )
        axislabels=["Outcome", "Fraction of occurances"] 
        assert(check_plot([line1],exppatch=line1,explabels=axislabels,explegend=False,output=True))
