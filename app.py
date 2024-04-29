import streamlit as st
import os

st.title('App 1')
result = os.popen('pip list').read()
st.code(result, language=None)

from pathlib import Path
import sys
import sklearn 
import scipy 
from IPython.display import clear_output
sys.path.append(str(Path(__file__).resolve().parent.parent))

from module import function

y = function(12.0)
st.title(f'{y}')