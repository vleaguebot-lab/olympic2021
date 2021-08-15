import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


st.title('Tokyo 2020 Olympic statics')

st.write('DataFrame')

df = pd.DataFrame(
    np.random.rand(100, 2),
    columns={'lat', 'lon'}
)

st.dataframe(df.style.highlight_max(axis=0))
# st.table(df.style.highlight_max(axis=0))

# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)
# st.map(df)

if st.checkbox('Show Image'):
    img = Image.open('raptors_tshirts.JPG')
    st.image(img, caption='Toronto Raptors', use_column_width=True)

"""

# 男子
## 予選

```python
import streamlit as st
import numpy as np
import pandas as pd

```

"""
