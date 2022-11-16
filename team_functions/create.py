import streamlit as st
import sys
sys.path.append('../IPL_Tournament_App')

from database import add_team

def create():
    col1, col2 = st.columns(2)
    with col1:
        team_name = st.text_input("Team Name:")
        city = st.text_input("City:")
        wins = st.text_input("Wins:")
        home_stadium_id = st.text_input("Home Stadium ID:")
    with col2:
        losses = st.text_input("Losses:")
        draws = st.text_input("Draws:")
        team_rank = st.text_input("Team Rank:")
        rival_team_name = st.text_input("Rival Team Name:")
        #availability = st.selectbox("Availability", ["Yes", "No"])
    if st.button("Add Team"):
        add_team(team_name,city,wins,losses,draws,team_rank,home_stadium_id,rival_team_name)
        st.success("Successfully added Team: {}".format(team_name))