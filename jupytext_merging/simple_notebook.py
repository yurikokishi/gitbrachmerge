# ---
# jupyter:
#   jupytext_format_version: '1.3'
#   jupytext_formats: md:markdown,py:light
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   language_info:
#     codemirror_mode:
#       name: ipython
#       version: 3
#     file_extension: .py
#     mimetype: text/x-python
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#     version: 3.7.0
# ---

import numpy as np
import altair as alt
import pandas as pd

x = np.linspace(0,6)
y = np.sin(x)
df = pd.DataFrame({'x': x, 'y': y})

alt.Chart(df
        ).mark_point(
            color='red'
        ).encode(
            x='x:Q',
            y='y:Q')


