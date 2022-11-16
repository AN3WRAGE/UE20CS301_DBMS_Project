# Importing pakages
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Home",
)


def main():
    st.title("IPL Tournament Application")
    image = Image.open('IPL_1.jpg')
    st.image(image, caption='IPL')


if __name__ == '__main__':
    main()