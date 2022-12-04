import streamlit as st
import sys
sys.path.append('../IPL_Tournament_App')

from database import add_match, add_team_match, add_match_umpire

def create():
    col1, col2 = st.columns(2)
    with col1:
        team_1 = st.text_input("Enter Team 1:")
        match_no = st.text_input("Match Number:")
        toss = st.text_input("Toss result:")
        result = st.text_input("Winning team result:")
        umpire1 = st.text_input("Umpire 1 Id:")
        umpire3 = st.text_input("Umpire 3 Id:")
    with col2:
        team_2 = st.text_input("Enter Team 2:")
        match_date = st.text_input("Date:")
        man_of_match = st.text_input("Man of the match:")
        stadium_id = st.text_input("Stadium ID:")
        umpire2 = st.text_input("Umpire 2 Id:")
        
    if st.button("Add match"):
        add_match(match_no,toss,result,match_date,man_of_match,stadium_id)
        add_team_match(match_no,team_1)
        add_team_match(match_no,team_2)
        add_match_umpire(match_no,umpire1) 
        add_match_umpire(match_no,umpire2) 
        add_match_umpire(match_no,umpire3) 
        add_match_umpire(match_no,umpire1)
        st.success("Successfully added Match: {}".format(match_no))