import streamlit as st
import sys
sys.path.append('../IPL_Tournament_App')

from database import add_player, add_batsman

def create():
    col1, col2 = st.columns(2)
    with col1:
        jersey_no=None
        player_name = st.text_input("Player Name:")
        jersey_no = st.text_input("Unique Jersey Number:")
        test = st.text_input("Test matches played:")
        odi = st.text_input("ODI matches played:")
        team_name = st.text_input("Team name:")
    with col2:
        t20 = st.text_input("T20 matches played:")
        dob = st.text_input("Date of birth:")
        debut = st.text_input("Debut date:")
        is_keeper = st.selectbox("Is he a wicket-keeper:", ["Yes", "No"])
        keeper=0
        if(is_keeper=="Yes"):
            keeper=1
        #availability = st.selectbox("Availability", ["Yes", "No"])
    if st.button("Add Player"):
        add_player(player_name,jersey_no,test,odi,t20,dob,debut,keeper,team_name)
        st.success("Successfully added Player: {}".format(player_name))
    
    yes_batsman = st.checkbox("Is this player a batsman?")
    if yes_batsman:
        st.subheader("Enter batsman details")
        col3, col4 = st.columns(2)
        with col3:
            sixes = st.text_input("Number of Sixes:")
            runs = st.text_input("Number of runs:")
            avg = st.text_input("Batting Average:")

        with col4:
            fifties = st.text_input("Number of fifties:")
            fours = st.text_input("Number of fours:")
            hundreds = st.text_input("Number of centuries:")
                
        if st.button("Add batsman"):
            if(jersey_no!=None):
                add_batsman(jersey_no,sixes,runs,avg,fifties,fours,hundreds)
                st.success("Successfully added as a Batsman: {}".format(player_name))
            else:
                st.failure("Enter player details first: {}".format(player_name))
        
    if st.checkbox("Is this player a bowler?"):
            st.subheader("Enter bowler details")
