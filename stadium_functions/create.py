import streamlit as st
import sys
sys.path.append('../IPL_Tournament_App')

from database import add_stadium

def create():
    col1, col2 = st.columns(2)
    with col1:
        stadium_name = st.text_input("Stadium Name:")
        stadium_id = st.text_input("Stadium ID:")
        capacity = st.text_input("Capacity:")
    with col2:
        city = st.text_input("City:")
        address = st.text_input("Address:")
        
    if st.button("Add Stadium"):
        add_stadium(stadium_name,stadium_id,capacity,city,address)
        st.success("Successfully added Stadium: {}".format(stadium_name))