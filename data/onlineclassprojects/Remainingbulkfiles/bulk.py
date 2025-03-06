

import os  # Import the os module to interact with the file system
import streamlit as st  # Import Streamlit for UI components

def rename_uploaded_files(files, prefix):
    renamed_files = []  # List to store renamed file names
    
    for index, uploaded_file in enumerate(files, start=1):
        file_extension = os.path.splitext(uploaded_file.name)[1]  # Get file extension
        new_name = f"{prefix}{index}{file_extension}"  # Create new filename with prefix and index
        
        renamed_files.append((new_name, uploaded_file))  # Store new name and file object
    
    return renamed_files  # Return list of renamed files

# Streamlit UI
st.set_page_config(page_title="Bulk File Renamer - Built by Samad", layout="centered")  # Set page title and layout
st.title("Bulk File Renamer - Built by Samad")  # Set title for the Streamlit app

# Custom CSS for black background
st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True  # Allow unsafe HTML for custom styling
)

# File uploader
uploaded_files = st.file_uploader("Upload multiple files", accept_multiple_files=True)  # Upload multiple files
prefix = st.text_input("Enter prefix for new filenames:", value="file_")  # Text input for filename prefix

if st.button("Rename Files"):  # Button to trigger renaming
    if uploaded_files and prefix:
        renamed_files = rename_uploaded_files(uploaded_files, prefix)  # Call rename function
        if renamed_files:
            st.success("Files renamed successfully! Click below to download.")
            for new_name, file in renamed_files:
                st.download_button(label=f"Download {new_name}", data=file, file_name=new_name)  # Provide download link
        else:
            st.error("Failed to rename files.")
    else:
        st.error("Please upload files and enter a prefix.")  # Show error message if inputs are missing

# import os  # Import the os module to interact with the file system
# import streamlit as st  # Import Streamlit for UI components

# def rename_uploaded_files(files, prefix):
#     renamed_files = []  # List to store renamed file names
    
#     for index, uploaded_file in enumerate(files, start=1):
#         file_extension = os.path.splitext(uploaded_file.name)[1]  # Get file extension
#         new_name = f"{prefix}{index}{file_extension}"  # Create new filename with prefix and index
        
#         renamed_files.append((new_name, uploaded_file))  # Store new name and file object
    
#     return renamed_files  # Return list of renamed files

# # Streamlit UI
# st.title("Bulk File Renamer")  # Set title for the Streamlit app

# # Custom CSS for black background
# st.markdown(
#     """
#     <style>
#     body {
#         background-color: black;
#         color: white;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True  # Allow unsafe HTML for custom styling
# )

# # File uploader
# uploaded_files = st.file_uploader("Upload multiple files", accept_multiple_files=True)  # Upload multiple files
# prefix = st.text_input("Enter prefix for new filenames:", value="file_")  # Text input for filename prefix

# if st.button("Rename Files"):  # Button to trigger renaming
#     if uploaded_files and prefix:
#         renamed_files = rename_uploaded_files(uploaded_files, prefix)  # Call rename function
#         if renamed_files:
#             st.success("Files renamed successfully! Click below to download.")
#             for new_name, file in renamed_files:
#                 st.download_button(label=f"Download {new_name}", data=file, file_name=new_name)  # Provide download link
#         else:
#             st.error("Failed to rename files.")
#     else:
#         st.error("Please upload files and enter a prefix.")  # Show error message if inputs are missing

