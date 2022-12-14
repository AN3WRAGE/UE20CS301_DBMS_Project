import datetime

import pandas as pd
import streamlit as st
from database import view_all_team, view_only_team_names, get_team, edit_team_data
from database import add_color, remove_color


def update():
    result = view_all_team()
    # st.write(result)
    df = pd.DataFrame(result, columns=['team_name','city','wins','losses','draws','team_rank','home_stadium_id','rival_team_name','team_colors','team_captain','points'])
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
            new_team_name = st.text_input("Team Name:",value=team_name)
            new_city = st.text_input("City:",value=city)
            new_wins = st.text_input("Wins:",value=wins)
            new_home_stadium_id = st.text_input("Home Stadium ID:",value=home_stadium_id)
        with col2:
            new_losses = st.text_input("Losses:",value=losses)
            new_draws = st.text_input("Draws:",value=draws)
            new_team_rank = st.text_input("Team Rank:",value=team_rank)
            new_rival_team_name = st.text_input("Rival Team Name:",value=rival_team_name)
        if st.button("Update Team"):
            edit_team_data(new_team_name,new_city,new_wins,new_losses,new_draws,new_team_rank,new_home_stadium_id,new_rival_team_name,team_name)
            st.success("Successfully updated:: {} to ::{}".format(team_name, new_team_name))

    
        #Code to change the color of the team jersey
        col3, col4 = st.columns(2)
        with col3:
            new_add_color = st.text_input("Enter a color to add:")
            if st.button("Add new color"):
                add_color(team_name,new_add_color)
                st.success("Successfully added color {} to {}".format(new_add_color, team_name))
                
        with col4:
            new_rem_color = st.text_input("Enter a color to remove:")
            if st.button("Remove existing color"):
                remove_color(team_name,new_rem_color)
                st.success("Successfully removed color {} from {}".format(new_add_color, team_name))

    result2 = view_all_team()
    df2 = pd.DataFrame(result2, columns=['team_name','city','wins','losses','draws','team_rank','home_stadium_id','rival_team_name','team_colors','team_captain','points'])
    with st.expander("Updated data"):
        st.dataframe(df2)
