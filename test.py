import numpy as np
import pandas as pd
import streamlit as st

array = np.random.randn(10,2) * [100, 100]
df = pd.DataFrame(array,columns=['A', 'B'])

st.title('Random Numbers')
st.table(df)