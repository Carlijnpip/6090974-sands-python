"""
Python code to define functions which create signals and perform operations on them
"""
import numpy as np
import matplotlib.pyplot as plt


def sinusoidal (duration = 2.0, frequency = 5.0, amplitude = 1, phase = 0.0,sampling_rate= 1000): 
    """
    Generate a sinusoidal signal
    Parameters:
    Duration: Signal duration in seconds
    Frequency: Frequency in Hz
    Amplitude: Signal amplitude
    phase: Phase shift in radians
    Sampling_rate: sampling rate in Hz
    Returns:
    - Time array
    - Signal: Generated sinusoidal signal
    """
    t = np.linspace(0, duration, int(sampling_rate*duration), endpoint=False)
    signal = amplitude *np.sin(2*np.pi*frequency*t+phase)
       
    return t, signal

def unit_step(duration=3.0, step_time=1.0, amplitude = 1.0, sampling_rate=1000):
    """
    Generate a unit step signal
    Parameters:
    - duration: signal duration in seconds
    - step_time: time when step occurs (seconds)
    - amplitude: step amplitude
    - sampling_rate: sampling rate in Hz
    
    Returns:
    -t2: time array
    - signal2: generated unit step signal
    """
    t= np.linspace(0,duration,int(sampling_rate*duration), endpoint=False)
    signal = amplitude * (t>=step_time).astype(float)
    return t, signal
    
def time_shift(t, signal, shift_amount):
    """
    Apply time shifting to a signal.
    
    Parameters:
    - t: Original time array
    - signal: Original signal
    - shift_amount: Shift amount in seconds (positive = delay, negative = advance)
    
    Returns:
    - t_shifted: Shifted time array
    - signal_shifted: Shifted signal
    """
    t_shifted = t - shift_amount
    return t_shifted, signal

def time_scale(t, signal, scale_factor):
    """
    Apply time scaling to a signal.
    
    Parameters:
    - t: Original time array
    - signal: Original signal
    - scale_factor: Scaling factor (>1 = compression, <1 = expansion)
    
    Returns:
    - t_scaled: Scaled time array
    - signal_scaled: Scaled signal
    """
    t_scaled = t * scale_factor
    return t_scaled, signal