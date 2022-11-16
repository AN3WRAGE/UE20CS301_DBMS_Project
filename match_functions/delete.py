import pandas as pd
import streamlit as st
from database import view_all_match, view_only_match_result, delete_match


def delete():
    result = view_all_match()
    df = pd.DataFrame(result, columns=['match_no','toss','result','match_date','man_of_match','stadium_id'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_items = [i[0] for i in view_only_match_result()]
    selected_items = st.selectbox("Task to Delete", list_of_items)
    st.warning("Do you want to delete ::{}".format(selected_items))
    if st.button("Delete Match"):
        delete_match(selected_items)
        st.success("Match has been deleted successfully")
    new_result = view_all_match()
    df2 = pd.DataFrame(new_result, columns=['match_no','toss','result','match_date','man_of_match','stadium_id'])
    with st.expander("Updated data"):
        st.dataframe(df2)