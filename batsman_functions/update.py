import datetime

import pandas as pd
import streamlit as st
from database import view_all_batsman, view_only_batsman_names, get_batsman, edit_batsman_data


def update():
    result = view_all_batsman()
    # st.write(result)
    df = pd.DataFrame(result, columns=['jersey_no','player_name','sixes','runs','average','fifties','fours','hundreds'])
    with st.expander("Current batsmen"):
        st.dataframe(df)
    list_of_batters = [i[0] for i in view_only_batsman_names()]
    selected = st.selectbox("Batsman to Edit", list_of_batters)
    selected_result = get_batsman(selected)
    # st.write(selected_result)
    if selected_result:
        jersey_no = selected_result[0][0]
        player_name = selected_result[0][1]
        sixes = selected_result[0][2]
        runs = selected_result[0][3]
        average = selected_result[0][4]
        fifties = selected_result[0][5]
        fours = selected_result[0][6]
        hundreds = selected_result[0][7]
        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_jersey_no = st.text_input("Enter jersey no:",value=jersey_no)
            new_sixes = st.text_input("Number of sixes:",value=sixes)
            new_runs = st.text_input("Number of runs:",value=runs)
            new_hundreds = st.text_input("Number of hundreds:",value=hundreds)

        with col2:
            new_average = st.text_input("Batting average:",value=average)
            new_fifties = st.text_input("Number of fifties:",value=fifties)
            new_fours = st.text_input("Number of fours:",value=fours)

        if st.button("Update batsman"):
            edit_batsman_data(new_jersey_no,new_sixes,new_runs,new_average,new_fifties,new_fours,new_hundreds,jersey_no)
            st.success("Successfully updated batsman:: {} ".format(player_name))

    result2 = view_all_batsman()
    df2 = pd.DataFrame(result2, columns=['jersey_no','player_name','sixes','runs','average','fifties','fours','hundreds'])
    with st.expander("Updated data"):
        st.dataframe(df2)
