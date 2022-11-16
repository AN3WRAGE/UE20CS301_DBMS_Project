import pandas as pd
import streamlit as st
from database import view_all_coach, view_only_coach_names, delete_coach


def delete():
    result = view_all_coach()
    df = pd.DataFrame(result, columns=['coach_name','coach_id','dob','country_origin','team_name','age'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_items = [i[0] for i in view_only_coach_names()]
    selected_items = st.selectbox("Task to Delete", list_of_items)
    st.warning("Do you want to delete ::{}".format(selected_items))
    if st.button("Delete Coach"):
        delete_coach(selected_items)
        st.success("Coach has been deleted successfully")
    new_result = view_all_coach()
    df2 = pd.DataFrame(new_result, columns=['coach_name','coach_id','dob','country_origin','team_name','age'])
    with st.expander("Updated data"):
        st.dataframe(df2)