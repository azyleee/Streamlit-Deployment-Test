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
from sklearn.preprocessing import MinMaxScaler
import scipy 
import numpy as np
from IPython.display import clear_output
sys.path.append(str(Path(__file__).resolve().parent.parent))

from module import function

x = np.random.uniform(size=(10,3))
y = function(x)
st.title(f'{y}')

scaler = MinMaxScaler()
y_scaled = scaler.fit_transform(y)
st.code(y_scaled)