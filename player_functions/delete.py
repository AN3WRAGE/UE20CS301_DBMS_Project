import pandas as pd
import streamlit as st
from database import view_all_player, view_only_player_names, delete_player


def delete():
    result = view_all_player()
    df = pd.DataFrame(result, columns=['player_name','jersey_no','test','odi','t20','dob','debut','keeper','team_name','age'])
    with st.expander("Current data"):
        st.dataframe(df)

    total_list = [i[0] for i in view_only_player_names()]
    selected = st.selectbox("Task to Delete", total_list)
    st.warning("Do you want to delete ::{}".format(selected))
    if st.button("Delete Player"):
        delete_player(selected)
        st.success("Player has been deleted successfully")
    new_result = view_all_player()
    df2 = pd.DataFrame(new_result, columns=['player_name','jersey_no','test','odi','t20','dob','debut','keeper','team_name','age'])
    with st.expander("Updated data"):
        st.dataframe(df2)