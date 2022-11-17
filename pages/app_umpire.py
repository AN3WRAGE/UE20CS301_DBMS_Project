import streamlit as st
import mysql.connector

import sys
sys.path.append('../IPL_Tournament_App')

from umpire_functions.create import create
from umpire_functions.read import read
from umpire_functions.update import update
from umpire_functions.delete import delete

st.set_page_config(
    page_title="Umpires",
)


def main():
    st.title("IPL Umpire")
    menu = ["View", "Add", "Edit", "Remove"]
    choice = st.sidebar.selectbox("Menu", menu)

    #create_table()
    if choice == "View":
        st.subheader("View created umpire")
        read()

    elif choice == "Add":
        st.subheader("Enter umpire Details:")
        create()

    elif choice == "Edit":
        st.subheader("Update created umpire")
        update()
        
    elif choice == "Remove":
        st.subheader("Delete created umpire")
        delete()

    else:
        st.subheader("About umpire")


if __name__ == '__main__':
    main()