import datetime

import pandas as pd
import streamlit as st
from database import view_all_player, view_only_player_names, get_player, edit_player_data
from database import add_batsman, add_bowler


def update():
    result = view_all_player()
    # st.write(result)
    df = pd.DataFrame(result, columns=['player_name','jersey_no','test','odi','t20','dob','debut','keeper','team_name','age'])
    with st.expander("Current players"):
        st.dataframe(df)
    list_of_player = [i[0] for i in view_only_player_names()]
    selected = st.selectbox("Player to Edit", list_of_player)
    selected_result = get_player(selected)
    # st.write(selected_result)
    jersey_no=None
    if selected_result:
        player_name = selected_result[0][0]
        jersey_no = selected_result[0][1]
        test = selected_result[0][2]
        odi = selected_result[0][3]
        t20 = selected_result[0][4]
        dob = selected_result[0][5]
        debut = selected_result[0][6]
        keeper = selected_result[0][7]
        team_name = selected_result[0][8]
        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_player_name = st.text_input("Player Name:",value=player_name)
            new_jersey_no = st.text_input("Unique Jersey Number:",value=jersey_no)
            new_test = st.text_input("Test matches played:",value=test)
            new_odi = st.text_input("ODI matches played:",value=odi)
            new_team_name = st.text_input("Team name:",value=team_name)

        with col2:
            new_t20 = st.text_input("T20 matches played:",value=t20)
            new_dob = st.text_input("Date of birth:",value=dob)
            new_debut = st.text_input("Debut date:",value=debut)
            iskeeper = st.selectbox("Is he a wicket-keeper:", ["Yes", "No"])
            new_keeper=0
            if(iskeeper=="Yes"):
                new_keeper=1

        if st.button("Update player"):
            edit_player_data(new_player_name,new_jersey_no,new_test,new_odi,new_t20,new_dob,new_debut,new_keeper,new_team_name,player_name)
            st.success("Successfully updated:: {} to ::{}".format(player_name, new_player_name))

    
    yes_batsman = st.checkbox("Is this player a batsman?")
    if yes_batsman:
        st.subheader("Enter batsman details")
        col3, col4 = st.columns(2)
        with col3:
            sixes = st.text_input("Number of Sixes:")
            runs = st.text_input("Number of runs:")
            avg = st.text_input("Batting Average:")

        with col4:
            fifties = st.text_input("Number of fifties:")
            fours = st.text_input("Number of fours:")
            hundreds = st.text_input("Number of centuries:")
                
        if st.button("Add batsman"):
            if(jersey_no!=None):
                add_batsman(jersey_no,sixes,runs,avg,fifties,fours,hundreds)
                st.success("Successfully added as a Batsman: {}".format(player_name))
            else:
                st.failure("Enter player details first: {}".format(player_name))

    yes_bowler = st.checkbox("Is this player a bowler?")
    if yes_bowler:
        st.subheader("Enter bowler details")
        col3, col4 = st.columns(2)
        with col3:
            economy = st.text_input("Economy:")
            wickets = st.text_input("Number of wickets:")

        with col4:
            average = st.text_input("Bowling average:")
            runs = st.text_input("Runs given:")
            balls_bowled = st.text_input("Number of balls bowled:")
                
        if st.button("Add bowler"):
            if(jersey_no!=None):
                add_bowler(jersey_no,economy,wickets,average,runs,balls_bowled)
                st.success("Successfully added as a Bowler: {}".format(player_name))
            else:
                st.failure("Enter player details first: {}".format(player_name))
    
    result2 = view_all_player()
    df2 = pd.DataFrame(result2, columns=['player_name','jersey_no','test','odi','t20','dob','debut','keeper','team_name','age'])
    with st.expander("Updated data"):
        st.dataframe(df2)
