import streamlit as st
import numpy as np
import pandas as pd
# from PIL import Image
import glob


st.title('Tokyo 2020 Olympic statics')

sex = st.sidebar.selectbox(
    '男子or女子',
    ['men', 'women']
)

select = glob.glob('{}/stats/*.csv'.format(sex))
for i in range(len(select)):
    if sex == 'men':
        select[i] = select[i][10:-4]
    else:
        select[i] = select[i][12:-4]

option = st.sidebar.selectbox(
    '試合・チームを選択してください',
    select
)

'You select', option, '.'

df1 = pd.read_csv(
    '{}/stats/{}.csv'.format(sex, option),
    index_col=0
)

# df2 = pd.read_csv(
#     '{}/stats/{}.csv'.format(sex,option)
# ).iloc[:-1, :]
df2 = pd.read_csv(
    '{}/stats/{}.csv'.format(sex, option)
).iloc[:-1, :]

# st.dataframe(df.style.highlight_max(axis=0))
st.dataframe(df1.iloc[:-1, :])
# st.table(df.style.highlight_max(axis=0))
st.table(df1)

# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df2.iloc[:, -1], label=df2.iloc[:, 2])
st.bar_chart(df2.iloc[:, -1])
# st.map(df)

# if st.checkbox('Show Image'):
#     img = Image.open('raptors_tshirts.JPG')
#     st.image(img, caption='Toronto Raptors', use_column_width=True)

"""

# 男子
## 予選

```python
import streamlit as st
import numpy as np
import pandas as pd
import glob

```

"""
