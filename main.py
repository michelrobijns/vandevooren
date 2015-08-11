#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from vandevooren import van_de_vooren
from plotting import plot_cp


def main():
    # Input
    epsilon = 0.025
    tau = 30
    alpha = 10
    
    # Generate coordinates and cp distribution
    x, y, cp = van_de_vooren(tau, epsilon, alpha)
    
    # Plot the pressure distribution
    plot_cp(x, cp, x, y)


if __name__ == '__main__':
    main()
