import pandas as pd
import numpy as np

a = pd.Series([1, 0.3, np.nan])
b = pd.Series(np.array([1, 2, 3]))
print("a\n", a)
print("b\n", b)
