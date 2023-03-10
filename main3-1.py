import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlit hyper入門 動的なウィジェット")

daf = pd.DataFrame(
    np.random.rand(20,3),
    columns=["a","b","c"]
)
st.table(daf.style.highlight_min(axis=0))
#折れ線グラフ
st.line_chart(daf)

st.area_chart(daf)
#棒グラフ
st.bar_chart(daf)

df = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69,139.70],
    columns=["lat","lon"]
)

st.map(df)

st.write("Display Image")

img = Image.open("samp.png")
st.image(img,caption="reiwa suga",use_column_width=True)




st.write("プレぐれすばーの表示")
"Start"

latest_itereation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_itereation.text(f"Iteration{i+1}")
    bar.progress(i+1)
    if i >= 50:
        time.sleep(0.03)
    else:
        time.sleep(0.1)
"Done!!"

st.write("Interactive Widgets")

left_column,right_cokumn = st.columns(2)
button = left_column.button("右からむに文字を表示")
if button:
    right_cokumn.write("ここは右からむ")

expander1 = st.expander("問い合わせ1")
expander1.write("問い合わせ1の回答")
expander2 = st.expander("問い合わせ2")
expander2.write("問い合わせ2の回答")
expander3 = st.expander("問い合わせ３")
expander3.write("問い合わせ３の回答")
# option = st.text_input("あなたの趣味を教えてください")

# "あなたの趣味は",option, "です"

# condition = st.slider("あなたの今の調子は？",0,100,50)
# "コンディション：",condition


if st.checkbox("Show Image"):
    img = Image.open("neko.jpg")
    st.image(img,caption="bikkurineko",use_column_width=True)