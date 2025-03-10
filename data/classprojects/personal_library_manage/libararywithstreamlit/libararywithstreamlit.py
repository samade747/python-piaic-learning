import streamlit as st
import json

# File to store library data
LIBRARY_FILE = "library.json"

# Load library from file
def load_library():
    try:
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save library to file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# Load library data
library = load_library()

# Streamlit UI
st.title("📚 Personal Library Manager")
menu = ["Add a Book", "Remove a Book", "Search for a Book", "Display All Books", "Statistics"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add a Book":
    st.subheader("➕ Add a New Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Publication Year", min_value=1000, max_value=9999, step=1)
    genre = st.text_input("Genre")
    read_status = st.checkbox("Have you read this book?")
    
    if st.button("Add Book"):
        library.append({"title": title, "author": author, "year": year, "genre": genre, "read": read_status})
        save_library(library)
        st.success("Book added successfully!")

elif choice == "Remove a Book":
    st.subheader("🗑️ Remove a Book")
    titles = [book["title"] for book in library]
    book_to_remove = st.selectbox("Select a book to remove", titles)
    
    if st.button("Remove Book"):
        library = [book for book in library if book["title"] != book_to_remove]
        save_library(library)
        st.success("Book removed successfully!")

elif choice == "Search for a Book":
    st.subheader("🔍 Search for a Book")
    search_term = st.text_input("Enter title or author")
    
    if st.button("Search"):
        results = [book for book in library if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower()]
        if results:
            for book in results:
                st.write(f"**{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {'✅ Read' if book['read'] else '❌ Unread'}")
        else:
            st.warning("No matching books found!")

elif choice == "Display All Books":
    st.subheader("📖 Your Library")
    if library:
        for book in library:
            st.write(f"**{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {'✅ Read' if book['read'] else '❌ Unread'}")
    else:
        st.info("Your library is empty!")

elif choice == "Statistics":
    st.subheader("📊 Library Statistics")
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
    
    st.write(f"**Total books:** {total_books}")
    st.write(f"**Percentage read:** {percentage_read:.2f}%")
