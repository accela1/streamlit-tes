import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title("Streamlit hyper入門")

st.write("DataFrame")

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

"""
# 章
## 節
### 公

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""

