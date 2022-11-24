import streamlit as st
import mysql.connector
from PIL import Image

import sys
sys.path.append('../IPL_Tournament_App')

from bowler_functions.read import read
from bowler_functions.update import update
from bowler_functions.delete import delete

st.set_page_config(
    page_title="Bowlers",
)


def main():
    st.title("IPL Bowlers")
    image = Image.open('IPL_3.jpg')
    st.image(image, caption='Batsman')
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