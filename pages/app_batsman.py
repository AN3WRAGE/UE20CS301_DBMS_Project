import streamlit as st
import mysql.connector

import sys
sys.path.append('../IPL_Tournament_App')

from batsman_functions.read import read
from batsman_functions.update import update
from batsman_functions.delete import delete

st.set_page_config(
    page_title="Batsmen",
)

def main():
    st.title("IPL Batsmen")
    menu = ["View", "Edit", "Remove"]
    choice = st.sidebar.selectbox("Menu", menu)

    #create_table()
    if choice == "View":
        st.subheader("View created batsmen")
        read()

    elif choice == "Edit":
        st.subheader("Update created batsmen")
        update()
        
    elif choice == "Remove":
        st.subheader("Delete created batsmen")
        delete()

    else:
        st.subheader("About batsmen")


if __name__ == '__main__':
    main()