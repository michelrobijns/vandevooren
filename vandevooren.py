#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from math import sqrt


def van_de_vooren(tau, E, alpha):
    tau = np.radians(tau)
    alpha = np.radians(alpha)
    
    TL = 0.5
    AK = (2 * np.pi - tau) / np.pi
    A = 2 * TL * np.power(E + 1, AK - 1) / np.power(2, AK)
    
    angles = np.arange(361)
    
    x = np.zeros(np.size(angles))
    y = np.zeros(np.size(angles))
    cp = np.zeros(np.size(angles))
    
    for i in angles:
    
        if (i == 0 | i == 360):
            X = 1
            Y = 0
            CP = 1
            
            x[i] = X
            y[i] = Y
            
            if (AK == 2 & (i == 0 | i == 360)):
                continue;
            
            cp[i] = CP
        
        TH = i / 180 * np.pi
        
        R1 = sqrt((A * (np.cos(TH) - 1)) ** 2 + (A * np.sin(TH)) ** 2)
        R2 = sqrt((A * (np.cos(TH) - E)) ** 2 + (A * np.sin(TH)) ** 2)
        
        if (TH == 0):
            TH1 = np.pi / 2
        else:
            TH1 = np.arctan((A * np.sin(TH)) / (A * (np.cos(TH) - 1))) + np.pi
        
        if ((np.cos(TH) - E) < 0 and np.sin(TH) > 0):
            TH2 = np.arctan((A * np.sin(TH)) / (A * (np.cos(TH) - E))) + np.pi
        elif ((np.cos(TH) - E) < 0 and np.sin(TH) < 0):
            TH2 = np.arctan((A * np.sin(TH)) / (A * (np.cos(TH) - E))) + np.pi
        elif ((np.cos(TH) - E) > 0 and np.sin(TH) < 0):
            TH2 = np.arctan((A * np.sin(TH)) / (A * (np.cos(TH) - E))) + 2 * np.pi
        else:
            TH2 = np.arctan((A * np.sin(TH)) / (A * (np.cos(TH) - E)))
        
        # Compute transformed positions
        COM1 = (((R1 ** AK) / (R2 ** (AK - 1)) ) /
            ((np.cos((AK - 1)*TH2)) ** 2 + (np.sin((AK - 1) * TH2)) ** 2))
        X = (COM1 * (np.cos(AK * TH1) * np.cos((AK - 1) * TH2) +
            np.sin(AK * TH1) * np.sin((AK - 1) * TH2)) + TL)
        Y = (COM1 * (np.sin(AK * TH1) * np.cos((AK - 1) * TH2) -
            np.cos(AK * TH1) * np.sin((AK - 1) * TH2)) + TL)
        
        x[i] = X
        y[i] = Y
        
        # Compute transformed pressure distribution
        A1 = np.cos((AK - 1) * TH1) * np.cos(AK * TH2) + np.sin((AK - 1)
            * TH1) * np.sin(AK * TH2)
        B1 = np.sin((AK - 1) * TH1) * np.cos(AK * TH2) - np.cos((AK - 1)
            * TH1) * np.sin(AK * TH2)
        C1 = (np.cos(AK * TH2)) ** 2 + (np.sin(AK * TH2)) ** 2
        P = A * (1 - AK + AK * E)
        D1 = A1 * (A * np.cos(TH) - P) - B1 * A * np.sin(TH)
        D2 = A1 * A * np.sin(TH) + B1 * (A * np.cos(TH) - P)
        
        TEMP = 2 * C1 * (np.sin(alpha) - np.sin(alpha - TH)) / (D1 ** 2 + D2 ** 2)
        COM2 = TEMP * (R2 ** AK) / (R1 ** (AK - 1))
        
        VX = D1 * np.sin(TH) + D2 * np.cos(TH)
        VY = -(D1 * np.cos(TH) - D2 * np.sin(TH))
        
        CP = 1 - COM2 ** 2 * (VX ** 2 + VY ** 2)
        
        cp[i] = CP
    
    length = np.amax(x) - np.amin(x)
    thickness = np.amax(y) - np.amin(y)
    
    # Move the leading edge to the origin
    x = x - np.amin(x)
    y = y - y[-1]
    
    # Scale the airfoil to unit length
    x = x / length
    y = y / length
    
    return x, y, cp
    

def main():
    pass


if __name__ == '__main__':
    main()

