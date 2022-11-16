import datetime

import pandas as pd
import streamlit as st
from database import view_all_coach, view_only_coach_names, get_coach, edit_coach_data


def update():
    result = view_all_coach()
    # st.write(result)
    df = pd.DataFrame(result, columns=['coach_name','coach_id','dob','country_origin','team_name','age'])
    with st.expander("Current Coaches"):
        st.dataframe(df)
    list_of_items = [i[0] for i in view_only_coach_names()]
    selected = st.selectbox("Coach to Edit", list_of_items)
    selected_result = get_coach(selected)
    # st.write(selected_result)
    if selected_result:
        coach_name = selected_result[0][0]
        coach_id = selected_result[0][1]
        dob = selected_result[0][2]
        country_origin = selected_result[0][3]
        team_name = selected_result[0][4]
        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_coach_name = st.text_input("Coach name:")
            new_coach_id = st.text_input("Coach ID:")
            new_dob = st.text_input("Date of birth:")
        with col2:
            new_country_origin = st.text_input("Country of origin:")
            new_team_name = st.text_input("Name of the team:")

        if st.button("Update coach"):
            edit_coach_data(new_coach_name,new_coach_id,new_dob,new_country_origin,new_team_name,coach_name,coach_id,dob,country_origin,team_name)
            st.success("Successfully updated:: {} to ::{}".format(coach_name, new_coach_name))

    result2 = view_all_coach()
    df2 = pd.DataFrame(result2, columns=['coach_name','coach_id','dob','country_origin','team_name','age'])
    with st.expander("Updated data"):
        st.dataframe(df2)
