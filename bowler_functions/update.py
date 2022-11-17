import datetime

import pandas as pd
import streamlit as st
from database import view_all_bowler, view_only_bowler_names, get_bowler, edit_bowler_data


def update():
    result = view_all_bowler()
    # st.write(result)
    df = pd.DataFrame(result, columns=['jersey_no','player_name','economy','wickets','average','runs','balls_bowled'])
    with st.expander("Current bowlers"):
        st.dataframe(df)
    list_of_bowlers = [i[0] for i in view_only_bowler_names()]
    selected = st.selectbox("Bowler to Edit", list_of_bowlers)
    selected_result = get_bowler(selected)
    # st.write(selected_result)
    if selected_result:
        jersey_no = selected_result[0][0]
        player_name = selected_result[0][1]
        economy = selected_result[0][2]
        wickets = selected_result[0][3]
        average = selected_result[0][4]
        runs = selected_result[0][5]
        balls_bowled = selected_result[0][6]
        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_jersey_no = st.text_input("Enter jersey no:")
            new_economy = st.text_input("Economy:")
            new_wickets = st.text_input("Number of wickets:")

        with col2:
            new_average = st.text_input("Bowling average:")
            new_runs = st.text_input("Runs given:")
            new_balls_bowled = st.text_input("Number of balls bowled:")

        if st.button("Update bowler"):
            edit_bowler_data(new_jersey_no,new_economy,new_wickets,new_average,new_runs,new_balls_bowled,jersey_no,economy,wickets,average,runs,balls_bowled)
            st.success("Successfully updated bowler:: {} ".format(player_name))

    result2 = view_all_bowler()
    df2 = pd.DataFrame(result2, columns=['jersey_no','player_name','economy','wickets','average','runs','balls_bowled'])
    with st.expander("Updated data"):
        st.dataframe(df2)
