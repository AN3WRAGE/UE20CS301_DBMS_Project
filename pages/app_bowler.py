import streamlit as st
import mysql.connector

import sys
sys.path.append('../IPL_Tournament_App')

from bowler_functions.read import read
from bowler_functions.update import update
from bowler_functions.delete import delete


def main():
    st.title("IPL Bowlers")
    menu = ["View", "Edit", "Remove"]
    choice = st.sidebar.selectbox("Menu", menu)

    #create_table()
    if choice == "View":
        st.subheader("View created bowlers")
        read()

    elif choice == "Edit":
        st.subheader("Update created bowlers")
        update()
        
    elif choice == "Remove":
        st.subheader("Delete created bowlers")
        delete()

    else:
        st.subheader("About bowlers")


if __name__ == '__main__':
    main()