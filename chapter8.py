# -*- coding: utf-8 -*-
"""
Created on Thu Jul 07 07:27:39 2016

@author: yue
Chapter 8: Plotting and Visualization
"""
import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
plt.plot([1.5, 3.5, -2, 1.6])
from numpy.random import randn
plt.plot(randn(50).cumsum(), 'k--')
ax4 = fig.add_subplot(2, 2, 4)
ax4.scatter(range(4), [0.9, 2.2, 3.3, 4])
ax4.plot(range(4), [1, 2, 3, 4], 'k-')
_ = ax1.hist(randn(100), bins=20, color='k', alpha=0.3)
ax2.scatter(np.arange(30), np.arange(30) + 3 * randn(30))

fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
for i in range(2):
    for j in range(2):
        axes[i, j].hist(randn(500), bins=50, color='k', alpha=0.5)
plt.subplots_adjust(wspace=0.1, hspace=0.1)

"""
Color, Markers, and Line Styles
"""
plt.plot(randn(30).cumsum(), 'ko--')        
data = randn(30).cumsum()
plt.plot(data, 'k--', label='Default')
plt.plot(data, 'k-', drawstyle='steps-post', label='steps-post')
plt.legend(loc='best')
       
