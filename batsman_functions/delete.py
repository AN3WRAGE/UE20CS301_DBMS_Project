import pandas as pd
import streamlit as st
from database import view_all_batsman, view_only_batsman_names, delete_batsman


def delete():
    result = view_all_batsman()
    df = pd.DataFrame(result, columns=['jersey_no','player_name','sixes','runs','average','fifties','fours','hundreds'])
    with st.expander("Current data"):
        st.dataframe(df)

    total_list = [i[0] for i in view_only_batsman_names()]
    selected = st.selectbox("Task to Delete", total_list)
    st.warning("Do you want to delete ::{}".format(selected))
    if st.button("Delete Batsman"):
        delete_batsman(selected)
        st.success("Batsman details have been deleted successfully")
    new_result = view_all_batsman()
    df2 = pd.DataFrame(new_result, columns=['jersey_no','player_name','sixes','runs','average','fifties','fours','hundreds'])
    with st.expander("Updated data"):
        st.dataframe(df2)