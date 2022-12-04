import pandas as pd
import streamlit as st
from database import view_all_team, view_only_team_names, delete_team


def delete():
    result = view_all_team()
    df = pd.DataFrame(result, columns=['team_name','city','wins','losses','draws','team_rank','home_stadium_id','rival_team_name','team_colors','team_captain','points'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_teams = [i[0] for i in view_only_team_names()]
    selected_team = st.selectbox("Task to Delete", list_of_teams)
    st.warning("Do you want to delete ::{}".format(selected_team))
    if st.button("Delete Team"):
        delete_team(selected_team)
        st.success("Team has been deleted successfully")
    new_result = view_all_team()
    df2 = pd.DataFrame(new_result, columns=['team_name','city','wins','losses','draws','team_rank','home_stadium_id','rival_team_name','team_colors','team_captain','points'])
    with st.expander("Updated data"):
        st.dataframe(df2)