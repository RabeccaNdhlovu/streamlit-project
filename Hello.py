import streamlit as st
from datetime import datetime

def main():
    st.title("Time Log System")

    Start = st.button("Start Time") 
    End = st.button("End Time")
    

    if Start:
        st.session_state.start_timestamp = datetime.now()
        st.success(f"Start time set to {st.session_state.start_timestamp}")

    if End:
        if "start_timestamp" in st.session_state:
            end_timestamp = datetime.now()
            time_difference = end_timestamp - st.session_state.start_timestamp
            st.success(f"End time set to {end_timestamp}")
            st.info(f"Time difference: {time_difference}")
        else:
            st.warning("Please set the start time first.")

if __name__ == "__main__":
    main()
