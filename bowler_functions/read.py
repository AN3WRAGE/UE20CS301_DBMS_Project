import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_all_bowler


def read():
    result = view_all_bowler()
    df = pd.DataFrame(result, columns=['jersey_no','player_name','economy','wickets','average','runs','balls_bowled'])
    with st.expander("View all Bowler"):
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