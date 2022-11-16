import streamlit as st
import mysql.connector

#from create import create_player
#from database import create_table
#from delete import delete_player
#rom read import read_player
#from update import update_player



def main():
    st.title("IPL Coaches")
    menu = ["View", "Add", "Edit", "Remove"]
    choice = st.sidebar.selectbox("Menu", menu)

    #create_table()
    if choice == "View":
        st.subheader("View created coaches")

    elif choice == "Add":
        st.subheader("Enter coaches Details:")

    elif choice == "Edit":
        st.subheader("Update created coaches")
        
    elif choice == "Remove":
        st.subheader("Delete created coaches")

    else:
        st.subheader("About coaches")


if __name__ == '__main__':
    main()