import pandas as pd
import streamlit as st
from database import view_all_bowler, view_only_bowler_names, delete_bowler


def delete():
    result = view_all_bowler()
    df = pd.DataFrame(result, columns=['jersey_no','player_name','economy','wickets','average','runs','balls_bowled'])
    with st.expander("Current data"):
        st.dataframe(df)

    total_list = [i[0] for i in view_only_bowler_names()]
    selected = st.selectbox("Task to Delete", total_list)
    st.warning("Do you want to delete ::{}".format(selected))
    if st.button("Delete Bowler"):
        delete_bowler(selected)
        st.success("Bowler details have been deleted successfully")
    new_result = view_all_bowler()
    df2 = pd.DataFrame(new_result, columns=['jersey_no','player_name','economy','wickets','average','runs','balls_bowled'])
    with st.expander("Updated data"):
        st.dataframe(df2)