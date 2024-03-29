import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('streamlit 入門')
# st.write('Interactive widgets')
st.write('プレぐれすばーの表示')
'Start'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.01)

    'Done'

# option = st.selectbox(
#     'あなたが好きな数字を教えてください、',
#     list(range(1,11))
# )

# 'あなたの好きな数字は、',option,'です'

# text = st.sidebar.text_input('あなたの趣味を教えてください、')
# 'あなたの趣味：', text

# condition = st.sidebar.slider('あなたの今の調子は？',0,100,50)
# 'コンディション', condition
left_column, right_column = st.columns(2)
button = left_column.button('右カラムにボタンを表示')
if button:
    right_column.write('ここは右カラム')

expender1 = st.expander('問い合わせ1')
expender1.write('問い合わせ1の回答')

expender2 = st.expander('問い合わせ2')
expender2.write('問い合わせの回答')

expender2 = st.expander('問い合わせ2')
expender2.write('問い合わせ2の回答')


# if st.checkbox('show Image'):
#     img = Image.open('dog.jpg')
#     st.image(img, caption='dog',use_column_width=True)

# df = pd.DataFrame({
#     '1列目':[1,2,3,4],
#     '2列目':[10,20,60,40]
# })

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.69, 139.70],
#     columns=['lat','lon']
# )

# st.write(df)

# st.dataframe(df.style.highlight_max(axis=0), width=100, height=100)

# st.dataframe(df.style.highlight_max(axis=0))

# st.table(df.style.highlight_max(axis=0))

# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)
# st.map(df)

# """

# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

# """