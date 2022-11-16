import streamlit as st
import sys
sys.path.append('../IPL_Tournament_App')

from database import add_umpire

def create():
    col1, col2 = st.columns(2)
    with col1:
        umpire_name = st.text_input("Umpire name:")
        umpire_id = st.text_input("Umpire ID:")
        dob = st.text_input("Date of birth:")
    with col2:
        country_origin = st.text_input("Country of origin:")
        no_of_matches = st.text_input("No. of matches umpired:")
        
    if st.button("Add umpire"):
        add_umpire(umpire_name,umpire_id,no_of_matches,dob,country_origin)
        st.success("Successfully added Umpire: {}".format(umpire_name))