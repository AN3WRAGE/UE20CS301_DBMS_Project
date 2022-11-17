import streamlit as st
import mysql.connector

import sys
sys.path.append('../IPL_Tournament_App')

from team_functions.create import create
from team_functions.read import read
from team_functions.update import update
from team_functions.delete import delete

st.set_page_config(
    page_title="Teams",
)


def main():
    st.title("IPL Teams")
    menu = ["View", "Add", "Edit", "Remove"]
    choice = st.sidebar.selectbox("Menu", menu)

    #create_table()
    if choice == "View":
        st.subheader("View created team")
        read()

    elif choice == "Add":
        st.subheader("Enter team Details:")
        create()

    elif choice == "Edit":
        st.subheader("Update created team")
        update()
        
    elif choice == "Remove":
        st.subheader("Delete created team")
        delete()

    else:
        st.subheader("About team")


if __name__ == '__main__':
    main()