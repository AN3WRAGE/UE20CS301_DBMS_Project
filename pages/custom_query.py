import streamlit as st
import mysql.connector
import pandas as pd

import sys
sys.path.append('../IPL_Tournament_App')

from database import custom_query

st.set_page_config(
    page_title="Custom Query",
)

def main():
    st.title("Enter a custom SQL query")
    q=st.text_input("Enter the query here:")
    colstr=st.text_input("Enter the column names:")
    cols=colstr.strip().split(',')

    if st.button("Show Output"):
        result=custom_query(q)
        if(colstr): 
            df = pd.DataFrame(result,columns=cols)
        else:
            df = pd.DataFrame(result)
        st.dataframe(df)

if __name__ == '__main__':
    main()