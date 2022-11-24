import streamlit as st
import mysql.connector
from PIL import Image

import sys
sys.path.append('../IPL_Tournament_App')

from match_functions.create import create
from match_functions.read import read
from match_functions.update import update
from match_functions.delete import delete

st.set_page_config(
    page_title="Matches",
)


def main():
    st.title("IPL Matches")
    image = Image.open('IPL_5.jpg')
    st.image(image, caption='Match')
    menu = ["View", "Add", "Edit", "Remove"]
    choice = st.sidebar.selectbox("Menu", menu)

    #create_table()
    if choice == "View":
        st.subheader("View created matches")
        read()

    elif choice == "Add":
        st.subheader("Enter matches Details:")
        create()

    elif choice == "Edit":
        st.subheader("Update created matches")
        update()
        
    elif choice == "Remove":
        st.subheader("Delete created matches")
        delete()

    else:
        st.subheader("About matches")


if __name__ == '__main__':
    main()