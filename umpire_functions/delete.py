import pandas as pd
import streamlit as st
from database import view_all_umpire, view_only_umpire_names, delete_umpire


def delete():
    result = view_all_umpire()
    df = pd.DataFrame(result, columns=['umpire_name','umpire_id','no_of_matches','dob','country_origin','age'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_items = [i[0] for i in view_only_umpire_names()]
    selected_items = st.selectbox("Task to Delete", list_of_items)
    st.warning("Do you want to delete ::{}".format(selected_items))
    if st.button("Delete Umpire"):
        delete_umpire(selected_items)
        st.success("Umpire has been deleted successfully")
    new_result = view_all_umpire()
    df2 = pd.DataFrame(new_result, columns=['umpire_name','umpire_id','no_of_matches','dob','country_origin','age'])
    with st.expander("Updated data"):
        st.dataframe(df2)