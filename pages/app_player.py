import streamlit as st
import mysql.connector
from PIL import Image

import sys
sys.path.append('../IPL_Tournament_App')

from player_functions.create import create
from player_functions.read import read
from player_functions.update import update
from player_functions.delete import delete

st.set_page_config(
    page_title="Players",
)


def main():
    st.title("IPL Players")
    image = Image.open('IPL_6.jpg')
    st.image(image, caption='Players')
    menu = ["View", "Add", "Edit", "Remove"]
    choice = st.sidebar.selectbox("Menu", menu)

    #create_table()
    if choice == "View":
        st.subheader("View created player")
        read()

    elif choice == "Add":
        st.subheader("Enter player Details:")
        create()

    elif choice == "Edit":
        st.subheader("Update created player")
        update()
        
    elif choice == "Remove":
        st.subheader("Delete created player")
        delete()

    else:
        st.subheader("About player")


if __name__ == '__main__':
    main()