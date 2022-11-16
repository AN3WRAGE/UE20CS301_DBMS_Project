import datetime

import pandas as pd
import streamlit as st
from database import view_all_stadium, view_only_stadium_names, get_stadium, edit_stadium_data


def update():
    result = view_all_stadium()
    # st.write(result)
    df = pd.DataFrame(result, columns=['stadium_name','stadium_id','capacity','city','address'])
    with st.expander("Current Stadiums"):
        st.dataframe(df)
    list_of_items = [i[0] for i in view_only_stadium_names()]
    selected = st.selectbox("Stadium to Edit", list_of_items)
    selected_result = get_stadium(selected)
    # st.write(selected_result)
    if selected_result:
        stadium_name = selected_result[0][0]
        stadium_id = selected_result[0][1]
        capacity = selected_result[0][2]
        city = selected_result[0][3]
        address = selected_result[0][4]
        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_stadium_name = st.text_input("Stadium Name:")
            new_stadium_id = st.text_input("Stadium ID:")
            new_capacity = st.text_input("Capacity:")

        with col2:
            new_city = st.text_input("City:")
            new_address = st.text_input("Address:")

        if st.button("Update stadium"):
            edit_stadium_data(new_stadium_name,new_stadium_id,new_capacity,new_city,new_address,stadium_name,stadium_id,capacity,city,address)
            st.success("Successfully updated:: {} to ::{}".format(stadium_name, new_stadium_name))

    result2 = view_all_stadium()
    df2 = pd.DataFrame(result2, columns=['stadium_name','stadium_id','capacity','city','address'])
    with st.expander("Updated data"):
        st.dataframe(df2)
