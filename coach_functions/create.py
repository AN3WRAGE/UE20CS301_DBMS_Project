import streamlit as st
import sys
sys.path.append('../IPL_Tournament_App')

from database import add_coach

def create():
    col1, col2 = st.columns(2)
    with col1:
        coach_name = st.text_input("Coach name:")
        coach_id = st.text_input("Coach ID:")
        dob = st.text_input("Date of birth:")
    with col2:
        country_origin = st.text_input("Country of origin:")
        team_name = st.text_input("Name of the team:")
        
    if st.button("Add coach"):
        add_coach(coach_name,coach_id,dob,country_origin,team_name)
        st.success("Successfully added Coach: {}".format(coach_name))