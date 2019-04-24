# -*- coding: utf-8 -*-
""" Data Comparison

In data science, often one wants to compare two different sets of data, like signal/background or prediction and
actual data.

In this very brief script we create two sets of data and compare them in one plot.

"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sciplot

try:
    plt.style.use('sciplot')
except OSError:
    print("Please install sciplot matplotlib style")

import numpy as np

simulation_data = np.append(np.random.random_sample(100)*7 - 3.5, np.random.normal(0, 0.5, 100))
data = np.append(np.random.random_sample(100)*7 - 3.5, np.random.normal(0, 0.4, 100))

sciplot.errorhist(simulation_data, color='black', label='Pseudo Simulation')
sciplot.hist(data, fill=True, lw=2, style=1, label='Pseudo Data')

plt.legend()
sciplot.xlim()
sciplot.labels('E', "Events", "GeV", 1)
sciplot.save("data_comparison.pdf")
