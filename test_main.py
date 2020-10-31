import unittest
import scipy.stats as st
import scipy.special as sp
from main import *

class UnitTests(unittest.TestCase) :
    def test_normalised(self) : 
        ssum = 0.
        fighand=plt.gca()
        for i in range(6) : ssum = ssum + fighand.patches[i].get_height()
        self.assertTrue( np.fabs(ssum - 1.)<1e-7, "your histogram does not appear to have been normalised" )
        
    def test_plot(self) :
        fighand=plt.gca()
        for i in range(6) :
            pval = sp.binom( 5, i )*pow(0.5,i)*pow( 0.5, 5-i )
            bar = np.sqrt( pval*(1-pval)  )*st.norm.ppf( (0.99 + 1) / 2 )
            self.assertTrue( np.fabs( fighand.patches[i].get_height() - pval )<bar, "the heights of the bars in your histogram appear to be incorrect" )
            
    def test_errorcheck1(self) : 
        for i in range(6) : self.assertTrue( np.abs(lower[i]-upper[i])<1e-7, "the error bars you have plotted are not symmetric" )
        
    def test_errorcheck2(self) : 
        fighand=plt.gca()
        for i in range(6) :
            mm = histo[i]
            sd = -lower[i] / st.norm.ppf(0.05) * np.sqrt(500)
            self.assertTrue( np.fabs( sd*sd - mm*(1-mm) )<1e-7, "the upper error bar you have drawn appears to be incorrect" )
            sd = upper[i] / st.norm.ppf(0.95) * np.sqrt(500)
            self.assertTrue( np.fabs( sd*sd - mm*(1-mm) )<1e-7, "the lower error bar you have drawn appears to be incorrect" )
    
