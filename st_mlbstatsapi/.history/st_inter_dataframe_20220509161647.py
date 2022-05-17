
import streamlit as st
import pandas as pd 
import numpy as np
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
import statsapi

# data= pd.read_csv('df_sample_data.csv', index_col=0)

def rookie_hr_leader_dict():
    rookie_hr_leaders_d = statsapi.league_leader_data('homeRuns', season=2021, playerPool='rookies', limit= 15)
    # print(rookie_hr_leaders_d)
    return rookie_hr_leaders_d

def hr_leader_pandas(hr_list):
    df = pd.DataFrame(hr_list)
    # df = df.transpose()
    df.columns = ['Rank', 'Player','Teams', 'HR' ]
    # print(df)
    return df
list_r_hr_leaders = rookie_hr_leader_dict()
hr_rook_df = hr_leader_pandas(list_r_hr_leaders)


AgGrid(hr_rook_df)



#TODO: combine add additional 