import time
import streamlit as st

#Streamlit UI setup
st.title(" ⏳ Countdown Timer")
st.markdown("Enter the time in hours, min and sec to start the countdown timer")

# user input for hours, mintues, and seconds,
col1, col2, col3 = st.columns(3)

with col1:
    hours = st.number_input("Hours", min_value=0, step=1)

with col2:
    minutes = st.number_input("Minutes", min_value=0, max_value=59, step=1)

with col3:
    seconds = st.number_input("Seconds", min_value=0, max_value=59, step=1)

#Convert the input time to total seconds
total_seconds = (hours * 3600) + (minutes * 60) + seconds


#start button
if st.button("Start countdown"):
    if total_seconds > 0:
        countdown_placeholder = st.empty()
        progress_bar = st.progress(0)

    for remaining in range(total_seconds, -1, -1):
        hrs = remaining // 3600
        mins = (remaining % 3600) // 60
        secs = remaining % 60

        countdown_placeholder.markdown(f"Time remaining: {hrs:02d}:{mins:02d}:{secs:02d}")
        progress_bar.progress((total_seconds - remaining) / total_seconds)
        time.sleep(1)

    countdown_placeholder.markdown(" 🎉 Time's Up! 🚀 ")
    progress_bar.progress(1)
else:
     st.warning("Please enter a valid time greater than 0!")
