
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



st.set_page_config(page_title="Dataframe Test")

AgGrid(hr_rook_df)


# resiszing st.dataframe default sizing
# df = pd.DataFrame([[33,]*1000])
# st.dataframe(df)

gb = GridOptionsBuilder.from_dataframe(hr_rook_df)
gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
gb.configure_side_bar() #Add a sidebar
gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
gridOptions = gb.build()

grid_response = AgGrid(
    hr_rook_df,
    gridOptions=gridOptions,
    data_return_mode='AS_INPUT', 
    update_mode='MODEL_CHANGED', 
    fit_columns_on_grid_load=False,
    theme='blue', #Add theme color to the table
    enable_enterprise_modules=True,
    height=350, 
    width='100%',
    reload_data=True
)

data = grid_response['data']
selected = grid_response['selected_rows'] 
df = pd.DataFrame(selected) #Pass the selected rows to a new dataframe df

#TODO: combine add additional data to DF


