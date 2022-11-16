import pandas as pd
import streamlit as st
from database import view_all_stadium, view_only_stadium_names, delete_stadium


def delete():
    result = view_all_stadium()
    df = pd.DataFrame(result, columns=['stadium_name','stadium_id','capacity','city','address'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_items = [i[0] for i in view_only_stadium_names()]
    selected_items = st.selectbox("Task to Delete", list_of_items)
    st.warning("Do you want to delete ::{}".format(selected_items))
    if st.button("Delete Stadium"):
        delete_stadium(selected_items)
        st.success("Stadium has been deleted successfully")
    new_result = view_all_stadium()
    df2 = pd.DataFrame(new_result, columns=['stadium_name','stadium_id','capacity','city','address'])
    with st.expander("Updated data"):
        st.dataframe(df2)