import datetime

import pandas as pd
import streamlit as st
from database import view_all_umpire, view_only_umpire_names, get_umpire, edit_umpire_data


def update():
    result = view_all_umpire()
    # st.write(result)
    df = pd.DataFrame(result, columns=['umpire_name','umpire_id','no_of_matches','dob','country_origin','age'])
    with st.expander("Current Umpires"):
        st.dataframe(df)
    list_of_items = [i[0] for i in view_only_umpire_names()]
    selected = st.selectbox("Umpire to Edit", list_of_items)
    selected_result = get_umpire(selected)
    # st.write(selected_result)
    if selected_result:
        umpire_name = selected_result[0][0]
        umpire_id = selected_result[0][1]
        no_of_matches = selected_result[0][2]
        dob = selected_result[0][3]
        country_origin = selected_result[0][4]
        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_umpire_name = st.text_input("Umpire name:")
            new_umpire_id = st.text_input("Umpire ID:")
            new_dob = st.text_input("Date of birth:")
        with col2:
            new_country_origin = st.text_input("Country of origin:")
            new_no_of_matches = st.text_input("No. of matches umpired:")

        if st.button("Update Umpire"):
            edit_umpire_data(new_umpire_name,new_umpire_id,new_no_of_matches,new_dob,new_country_origin,umpire_name,umpire_id,no_of_matches,dob,country_origin)
            st.success("Successfully updated:: {} to ::{}".format(umpire_name, new_umpire_name))

    result2 = view_all_umpire()
    df2 = pd.DataFrame(result2, columns=['umpire_name','umpire_id','no_of_matches','dob','country_origin','age'])
    with st.expander("Updated data"):
        st.dataframe(df2)
