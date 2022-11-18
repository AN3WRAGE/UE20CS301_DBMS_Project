import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_all_match


def read():
    result = view_all_match()
    df = pd.DataFrame(result, columns=['match_no','team_1','team_2','toss','result','match_date','man_of_match','stadium_id'])
    with st.expander("View all Matches"):
        st.dataframe(df)

    '''
    with st.expander("Train Source Location"):
        task_df = df['source'].value_counts().to_frame()
        task_df = task_df.reset_index()
        st.dataframe(task_df)
        p1 = px.pie(task_df, names='index', values='source')
        st.plotly_chart(p1)
    with st.expander("Train Destination Location"):
        task_df = df['destination'].value_counts().to_frame()
        task_df = task_df.reset_index()
        st.dataframe(task_df)
        p1 = px.pie(task_df, names='index', values='destination')
        st.plotly_chart(p1)
    '''