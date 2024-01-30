import streamlit as st
from datetime import datetime


def main():
    st.title("Time Log System")
    
    name = st.text_input("Name")
    email = st.text_input("Email")
    task = st.text_input("Task")
    Description = st.text_area("Description")

    st.sidebar.write(name)
    st.sidebar.write(email)
    st.sidebar.write(task)
    st.sidebar.write(Description)

    Start = st.button("Start Time") 
    End = st.button("End Time")
    

    if Start:
        st.session_state.start_timestamp = datetime.now()
        formatestart_time = st.session_state.start_timestamp.strftime('%H:%M')
        st.sidebar.write("Start time:",formatestart_time)
       

    if End:
        if "start_timestamp" in st.session_state:
            end_timestamp = datetime.now()
            formateend_time = end_timestamp.strftime('%H:%M')
            st.sidebar.write("End time :",formateend_time)
            
            
        else:
            st.warning("Please set the start time first.")

if __name__ == "__main__":
    main()
