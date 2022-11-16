import streamlit as st
import sys
sys.path.append('../IPL_Tournament_App')

from database import add_match

def create():
    col1, col2 = st.columns(2)
    with col1:
        match_no = st.text_input("Match Number:")
        toss = st.text_input("Toss result:")
        result = st.text_input("Winning team result:")
    with col2:
        match_date = st.text_input("Date:")
        man_of_match = st.text_input("Man of the match:")
        stadium_id = st.text_input("Stadium ID:")
        
    if st.button("Add match"):
        add_match(match_no,toss,result,match_date,man_of_match,stadium_id)
        st.success("Successfully added Match: {}".format(match_no))