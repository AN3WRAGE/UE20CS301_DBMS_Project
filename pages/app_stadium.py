import streamlit as st
import mysql.connector

import sys
sys.path.append('../IPL_Tournament_App')

from stadium_functions.create import create
from stadium_functions.read import read
from stadium_functions.update import update
from stadium_functions.delete import delete


def main():
    st.title("IPL Stadiums")
    menu = ["View", "Add", "Edit", "Remove"]
    choice = st.sidebar.selectbox("Menu", menu)

    #create_table()
    if choice == "View":
        st.subheader("View created stadium")
        read()

    elif choice == "Add":
        st.subheader("Enter stadium Details:")
        create()

    elif choice == "Edit":
        st.subheader("Update created stadium")
        update()
        
    elif choice == "Remove":
        st.subheader("Delete created stadium")
        delete()

    else:
        st.subheader("About stadium")


if __name__ == '__main__':
    main()