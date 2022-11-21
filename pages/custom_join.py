import streamlit as st
import mysql.connector
import pandas as pd

import sys
sys.path.append('../IPL_Tournament_App')

from database import left_outer_join, right_outer_join, full_outer_join, inner_join

st.set_page_config(
    page_title="Joins",
)

def main():
    left = st.text_input("Enter first table name")
    right = st.text_input("Enter second table name")
    common = st.text_input("Enter common attribute")

    if st.button("Left Outer Join"):
        result=left_outer_join(left,right,common)
        df=pd.DataFrame(result)
        st.dataframe(df)

    if st.button("Right Outer Join"):
        result=right_outer_join(left,right,common)
        df=pd.DataFrame(result)
        st.dataframe(df)

    #if st.button("Full Outer Join"):
    #    result=full_outer_join(left,right,common)
    #    df=pd.DataFrame(result)
    #    st.dataframe(df)

    if st.button("Inner Join"):
        result=inner_join(left,right,common)
        df=pd.DataFrame(result)
        st.dataframe(df)


if __name__ == '__main__':
    main()