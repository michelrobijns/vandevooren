#!/usrp/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.spines as spn
import matplotlib.gridspec as gridspec
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


def plot_cp(x, cp, x_airfoil, y_airfoil, use_TeX=False):
    blue = [0.118, 0.506, 0.984, 1]
    #cyan = [0.129, 0.996, 0.996, 1]
    #green = [0.118, 0.988, 0.133, 1]
    #orange = [0.992, 0.596, 0.118, 1]
    #red = [0.988, 0.047, 0.082, 1]
    
    plt.figure(num='Pressure Distribution', figsize=(6, 6), dpi=100)
    
    if use_TeX:
        plt.rc('font', **{'family': 'serif', 'serif': ['Palatino']})
        plt.rc('text', usetex=True)
    
    gs = gridspec.GridSpec(2, 1, height_ratios=[1, 0.2])
    gs.update(hspace=0.1) # Set the spacing between axes
    
    ax1 = plt.subplot(gs[0])
    ax2 = plt.subplot(gs[1])
    
    ax1.plot(x, cp, color=blue)
    ax1.set_ylabel('$C_p$ $[-]$', fontsize=16)
    ax1.set_xlabel('$x/c$ $[-]$', fontsize=16)
    ax1.set_xlim(0, 1)
    ax1.set_ylim(1, -6)
    ax1.set_xticks(np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]))
    ax1.set_yticks(np.linspace(1, -6, 8))
    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)
    ax1.spines['left'].set_position('zero')
    ax1.spines['bottom'].set_position('zero')
    ax1.yaxis.set_ticks_position('left')
    ax1.xaxis.set_ticks_position('bottom')
    ax1.xaxis.labelpad = 20
    
    ax2.plot(x_airfoil, y_airfoil, color='k')
    ax2.set_xlim(-0.01, 1)
    ax2.set_ylim(-0.11, 0.11)
    ax2.axis('off')
    
    #plt.savefig('name.pdf', format = 'pdf', dpi = 1000, bbox_inches='tight')
    plt.show()


def main():
    pass


if __name__ == '__main__':
    main()
