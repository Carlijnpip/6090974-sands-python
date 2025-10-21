# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 13:30:28 2025

@author: Carli
"""

import numpy as np
import matplotlib.pyplot as plt
from signal_functions import *
from main import * 
def test_sinusoidal(): 
    'Testing sinusoidal'
    t, signal = sinusoidal(duration = 2.0, frequency = 5.0, amplitude = 1)    
    assert len(t) == len(signal)
    assert signal[0]==0  

    t, signal = sinusoidal (3,10,2)
    assert np.isclose(np.max(signal), 2.0, atol=1e-2)

    t, signal = sinusoidal(5, 1, 0)
    assert np.allclose(signal, 0)

    t, signal = sinusoidal(-1, 2, 1)  # duration = -1
    assert len(t) == 0
    assert len(signal) == 0

test_sinusoidal()


def test_unitstep():
    'Testing unit step function'
    t, signal = unit_step(duration=2.0, step_time=0.5, amplitude=1.0, sampling_rate=1000)
    assert len(t) == len(signal)
    assert np.all(signal[t < 0.5] == 0.0)
    assert np.all(signal[t >= 0.5] == 1.0)

    t, signal = unit_step(2,0.5,2,1000)
    assert np.isclose(np.max(signal), 2.0, atol=1e-2)

test_unitstep()

def test_timeshift():
    'Testing time shifting function'
    t = np.linspace(0, 1, 1000, endpoint=False)
    signal = np.sin(2*np.pi*5*t)
    t_shifted, signal_shifted = time_shift(t, signal, 0.2)

    # time shifted correctly
    assert np.isclose(t_shifted[0], -0.2)
    assert np.all(signal_shifted == signal)  # signal values should not change

test_timeshift()

def test_timescale():
    'Testing time scaling function'
    t = np.linspace(0, 1, 1000, endpoint=False)
    signal = np.sin(2*np.pi*5*t)
    t_scaled, signal_scaled = time_scale(t, signal, 0.5)

    # scaling test: last time value should be halved
    assert np.isclose(t_scaled[-1], 0.5 * t[-1])
    
    # signal itself unchanged
    assert np.all(signal_scaled == signal)
    
test_timescale()