import streamlit as st
import os

st.title('App 1')
result = os.popen('pip list').read()
st.code(result, language=None)

st.title('Reading file from repo')
file_path = 'text_file.txt'
try:
    with open(file_path, 'r') as file:
        # Read the lines of the file
        file_lines = file.readlines()
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
st.write(file_lines)

from pathlib import Path
import sys
import sklearn 
import scipy 
from IPython.display import clear_output
sys.path.append(str(Path(__file__).resolve().parent.parent))

from module import function

y = function(12.0)
st.title(f'{y}')