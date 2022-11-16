import datetime

import pandas as pd
import streamlit as st
from database import view_all_team, view_only_team_names, get_team, edit_team_data


def update():
    result = view_all_team()
    # st.write(result)
    df = pd.DataFrame(result, columns=['team_name','city','wins','losses','draws','team_rank','home_stadium_id','rival_team_name'])
    with st.expander("Current Teams"):
        st.dataframe(df)
    list_of_team = [i[0] for i in view_only_team_names()]
    selected_team = st.selectbox("Team to Edit", list_of_team)
    selected_result = get_team(selected_team)
    # st.write(selected_result)
    if selected_result:
        team_name = selected_result[0][0]
        city = selected_result[0][1]
        wins = selected_result[0][2]
        losses = selected_result[0][3]
        draws = selected_result[0][4]
        team_rank = selected_result[0][5]
        home_stadium_id = selected_result[0][6]
        rival_team_name = selected_result[0][7]

        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_team_name = st.text_input("Team Name:")
            new_city = st.text_input("City:")
            new_wins = st.text_input("Wins:")
            new_home_stadium_id = st.text_input("Home Stadium ID:")
        with col2:
            new_losses = st.text_input("Losses:")
            new_draws = st.text_input("Draws:")
            new_team_rank = st.text_input("Team Rank:")
            new_rival_team_name = st.text_input("Rival Team Name:")
        if st.button("Update Team"):
            edit_team_data(new_team_name,new_city,new_wins,new_losses,new_draws,new_team_rank,new_home_stadium_id,new_rival_team_name,team_name,city,wins,losses,draws,team_rank,home_stadium_id,rival_team_name)
            st.success("Successfully updated:: {} to ::{}".format(team_name, new_team_name))

    result2 = view_all_team()
    df2 = pd.DataFrame(result2, columns=['team_name','city','wins','losses','draws','team_rank','home_stadium_id','rival_team_name'])
    with st.expander("Updated data"):
        st.dataframe(df2)
