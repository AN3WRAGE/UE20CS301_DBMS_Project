import datetime

import pandas as pd
import streamlit as st
from database import view_all_match, view_only_match_number, get_match, edit_match_data, edit_team_match_data


def update():
    result = view_all_match()
    # st.write(result)
    df = pd.DataFrame(result, columns=['match_no','team_1','team_2','toss','result','match_date','man_of_match','umpire_1','stadium_id'])
    with st.expander("Current Matches"):
        st.dataframe(df)
    list_of_items = [i[0] for i in view_only_match_number()]
    selected = st.selectbox("Match to Edit", list_of_items)
    selected_result = get_match(selected)
    # st.write(selected_result)
    if selected_result:
        match_no = selected_result[0][0]
        team_1=selected_result[0][1]
        team_2=selected_result[0][2]
        toss = selected_result[0][3]
        result = selected_result[0][4]
        match_date = selected_result[0][5]
        man_of_match = selected_result[0][6]
        stadium_id = selected_result[0][7]
        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_team_1 = st.text_input("Enter Team 1:")
            new_match_no = st.text_input("Match Number:")
            new_toss = st.text_input("Toss result:")
            new_result = st.text_input("Winning team result:")
        with col2:
            new_team_2 = st.text_input("Enter Team 2:")
            new_match_date = st.text_input("Date:")
            new_man_of_match = st.text_input("Man of the match:")
            new_stadium_id = st.text_input("Stadium ID:")

        if st.button("Update match"):
            edit_match_data(new_match_no,new_toss,new_result,new_match_date,new_man_of_match,new_stadium_id,match_no,toss,result,match_date,man_of_match,stadium_id)
            edit_team_match_data(new_team_1,new_match_no,team_1,match_no)
            edit_team_match_data(new_team_2,new_match_no,team_2,match_no)
            st.success("Successfully updated:: {} to ::{}".format(match_no, new_match_no))

    result2 = view_all_match()
    df2 = pd.DataFrame(result2, columns=['match_no','team_1','team_2','toss','result','match_date','man_of_match','umpire_1','stadium_id'])
    with st.expander("Updated data"):
        st.dataframe(df2)
