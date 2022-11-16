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
        st.subheader("View created Player")

    elif choice == "Add":
        st.subheader("Enter Player Details:")

    elif choice == "Edit":
        st.subheader("Update created Player")
        
    elif choice == "Remove":
        st.subheader("Delete created Player")

    else:
        st.subheader("About Player")


if __name__ == '__main__':
    main()