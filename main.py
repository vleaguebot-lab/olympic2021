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
select2 = []
select3 = []
for i in range(len(select)):
    if sex == 'men':
        select[i] = select[i][10:-4]
    else:
        select[i] = select[i][12:-4]
    # print(select[i][select[i].find('vs')+10:])
    select2.append(select[i][:select[i].find('vs')+9])
    select3.append(select[i][select[i].find('vs')+10:])

select2 = list(set(select2))
select2.sort()
select3 = list(set(select3))
select3.sort()

option = st.sidebar.selectbox(
    '試合・チームを選択してください',
    select2
)


stats = st.sidebar.selectbox(
    'スタッツを選択してください',
    select3
)
# print(option.find('vs'))

st.markdown('## *{}*'.format(option))

st.markdown('## *{}*'.format(stats))

st.markdown('### を選択しました。')

df1 = pd.read_csv(
    '{}/stats/{}-{}.csv'.format(sex, option, stats),
    index_col=0
)

# df2 = pd.read_csv(
#     '{}/stats/{}.csv'.format(sex,option)
# ).iloc[:-1, :]
df2 = pd.read_csv(
    '{}/stats/{}-{}.csv'.format(sex, option, stats)
).iloc[:-1, :]

# st.dataframe(df.style.highlight_max(axis=0))
st.dataframe(df1.iloc[:-1, :])
# st.table(df.style.highlight_max(axis=0))
st.table(df1)

# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df2.iloc[:, -1], label=df2.iloc[:, 2])

col = df2.columns[2:]
# print(col)
select_col = st.sidebar.selectbox(
    "グラフにするスタッツを選択してください",
    col
)

st.bar_chart(df2[select_col])
# st.map(df)

# if st.checkbox('Show Image'):
#     img = Image.open('raptors_tshirts.JPG')
#     st.image(img, caption='Toronto Raptors', use_column_width=True)

"""

```python
import streamlit as st
import numpy as np
import pandas as pd
import glob

```

"""
