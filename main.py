import matplotlib.pyplot as  plt
import numpy as np
import scipy.stats 

# You may want to add some code here

def binomial(n,p) :
  # Your code to generate the binomial random variables goes here.
  
histo = np.zeros(6)
# Insert code to compute a histogram by generating 500 binomial random variables with
# n=5 and p=0.5 here.  

# Don't forget to normalise your histogram.


# Include the code to compute the error bars at the 90% confidence limit here.  The list
# called lower should contain the difference between the mean and the 5th percentile of the
# distributions.  The list called upper should contain the differenc between the 95th percentile 
# of the distribution and the mean.
lower, upper = np.zeros(6), np.zeros(6)


# This will plot the histogram and the error bars
plt.bar( [0,1,2,3,4,5], histo, width=0.1 )
# This plots the small bar around each of the values.
plt.errorbar( [0,1,2,3,4,5], histo, yerr=[lower,upper], fmt='ko' )
plt.savefig("histo_with_errors.png")
