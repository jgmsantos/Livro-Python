import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 4), index='A B C D E'.split(), columns='W X Y Z '.split())

print(df)