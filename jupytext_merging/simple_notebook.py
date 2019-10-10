# ---
# jupyter:
#   jupytext:
#     formats: md:markdown,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.3'
#       jupytext_version: 0.8.6
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,6)
y = np.sin(x)

plt.plot(x, y)
