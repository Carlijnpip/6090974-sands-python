# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 15:07:07 2025

@author: Carli
"""

import numpy as np
import matplotlib.pyplot as plt
from signal_functions import *

def plot_signal_comparison(t_original, signal_original, t_modified, signal_modified, title_original, title_modified, filename):
    """
    Plot original and modified signals side by side. 

    """
    fig, (ax1, ax2) = plt.subplots (1,2,figsize=(12,4))
    
    ax1.plot(t_original, signal_original, 'b-', linewidth=1.5)
    ax1.set_title(title_original)
    ax1.set_xlabel('Time(s)')
    ax1.set_ylabel('Amplitude')
    ax1.grid(True, alpha = 0.3)
    
    ax2.plot(t_modified, signal_modified, 'r-', linewidth=2)
    ax2.set_title(title_modified)
    ax2.set_xlabel('Time(s)')
    ax2.set_ylabel('Amplitude')
    
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight') 
    plt.show()
    
def time_operations():
    "Demonatrate time shifting and scaling operations"
    
    "Generate original signal"
    t, sin_signal = sinusoidal(duration = 2.0, frequency = 5.0, amplitude = 1)
    
    "Time shifting"
    t_shifted, signal_shifted = time_shift(t, sin_signal, shift_amount=-0.75)
    plot_signal_comparison(t,sin_signal, t_shifted, signal_shifted,
                           "Original Sinusoidal Signal",
                           "Time-Shifted Signal (0.75 s delay)",
                           "sintime_shift_comparison.png")
   
    "Time Scaling"
    t_shifted, signal_scaled = time_scale(t, sin_signal, scale_factor=0.25)
    plot_signal_comparison(t,sin_signal, t_shifted, signal_scaled,
                                  "Original Sinusoidal Signal",
                                  "Time_Scaled Signal (compression:factor 0.5)",
                                  "sintime_scale_comparison.png")
    t, unit_signal = unit_step(duration=3.0, step_time=1.0, amplitude = 1.0, sampling_rate=1000)
    "Time shifting"
    t_shifted, signal_shifted = time_shift(t, unit_signal, shift_amount=-0.75)
    plot_signal_comparison(t,unit_signal, t_shifted, signal_shifted,
                           "Original Unit Step Signal",
                           "Time-Shifted Signal (0.75 s delay)",
                           "unittime_shift_comparison.png")
   
    "Time Scaling"
    t_shifted, signal_scaled = time_scale(t, unit_signal, scale_factor=0.25)
    plot_signal_comparison(t,unit_signal, t_shifted, signal_scaled,
                                  "Original Unit Step Signal",
                                  "Time_Scaled Signal (compression:factor 0.5)",
                                  "unittime_scale_comparison.png")
    
def signal_generation():
    """Demonstrate different signal types."""
    
    
    plt.figure(figsize=(15, 10))
    
    # Sinusoidal
    plt.subplot(3, 2, 1)
    t, sig = sinusoidal(frequency=2.0)
    plt.plot(t, sig)
    plt.title('Sinusoidal Signal')
    plt.grid(True, alpha=0.3)
    
    # Unit step
    plt.subplot(3, 2, 3)
    t, sig = unit_step(step_time=1.0)
    plt.plot(t, sig)
    plt.title('Unit Step')
    plt.grid(True, alpha=0.3)
   
    plt.savefig("originalsignals.png")
    
def demo_all_operations():
    """Run all demonstrations."""
    signal_generation()
    time_operations()
    
    
if __name__ == "__main__":
    demo_all_operations()
    
       
    
    
    
    
    
    
    
    