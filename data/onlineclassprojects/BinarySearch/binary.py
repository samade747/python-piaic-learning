import streamlit as st  # Import Streamlit for creating the web app
import numpy as np  # Import NumPy for numerical operations

# Set the background color using custom CSS
st.markdown(
    """
    <style>
    .stApp {
        background-color: #1E1E2F; /* Unique dark purple background */
        color: white; /* White text for better visibility */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Function to perform binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1  # Initialize left and right pointers
    steps = []  # List to store each step of the search
    
    while left <= right:
        mid = (left + right) // 2  # Calculate the middle index
        steps.append(f"Checking middle index {mid} with value {arr[mid]}")
        
        if arr[mid] == target:
            steps.append(f"Found target {target} at index {mid}")
            return mid, steps  # Return index and search steps
        elif arr[mid] < target:
            left = mid + 1  # Search the right half
            steps.append(f"Target is greater than {arr[mid]}, moving right")
        else:
            right = mid - 1  # Search the left half
            steps.append(f"Target is less than {arr[mid]}, moving left")
    
    steps.append("Target not found")
    return -1, steps  # Return -1 if target is not found

# Streamlit UI
st.title("Binary Search Visualizer")  # Title of the app
st.write("Enter a sorted list and a target number to perform binary search.")

# User input for sorted list
user_input = st.text_input("Enter sorted numbers separated by commas:")

target_input = st.text_input("Enter the target number:")

if st.button("Search"):
    try:
        # Convert input string to a list of integers
        arr = list(map(int, user_input.split(',')))
        target = int(target_input)  # Convert target input to integer
        
        # Ensure the list is sorted
        arr.sort()
        
        # Perform binary search
        index, search_steps = binary_search(arr, target)
        
        # Display the search steps
        st.subheader("Search Steps:")
        for step in search_steps:
            st.write(step)
        
        # Display result
        if index != -1:
            st.success(f"Target {target} found at index {index}.")
        else:
            st.error(f"Target {target} not found in the list.")
    except ValueError:
        st.error("Please enter valid numbers separated by commas.")
