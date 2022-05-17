import streamlit as st
# import statsapi
import pandas as pandas 

import py_statsapi_sandbox







# def rookie_leaders():


st.title("An Exploration into Baseball Data Science")

rook_hr = py_statsapi_sandbox.rookie_hr_leader_dict()
st.dataframe(rook_hr)
# st.dataframe




