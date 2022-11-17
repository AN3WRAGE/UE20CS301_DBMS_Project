import streamlit as st
import mysql.connector

import sys
sys.path.append('../IPL_Tournament_App')

from coach_functions.create import create
from coach_functions.read import read
from coach_functions.update import update
from coach_functions.delete import delete

st.set_page_config(
    page_title="Coaches",
)


def main():
    st.title("IPL Coaches")
    menu = ["View", "Add", "Edit", "Remove"]
    choice = st.sidebar.selectbox("Menu", menu)

    #create_table()
    if choice == "View":
        st.subheader("View created coach")
        read()

    elif choice == "Add":
        st.subheader("Enter coach Details:")
        create()

    elif choice == "Edit":
        st.subheader("Update created coach")
        update()
        
    elif choice == "Remove":
        st.subheader("Delete created coach")
        delete()

    else:
        st.subheader("About coach")


if __name__ == '__main__':
    main()