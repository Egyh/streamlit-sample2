import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello World")
st.header('こんにちは 世界やねん😀')

st.markdown('''
こんにちはやねん！

これはStreamlitAppのテストやねん。
''')


input_num = st.number_input('好きな数字いれたら倍になるねん', value=0)

result = input_num * 2
st.write('これが結果やねん', result)


# *** sidebar
st.sidebar.title('これはサイドバーやねん')