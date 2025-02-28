import streamlit as st
import numpy as np

# Function to initialize an empty 3x3 board
def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Function to check if a player has won the game
def check_winner(board, player):
    # Check rows for a win
    for row in board:
        if row.count(player) == 3:
            return True
    # Check columns for a win
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals for a win
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full (draw condition)
def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

# Main function to run the Tic-Tac-Toe game
def tic_tac_toe():
    # Set up Streamlit page configuration
    st.set_page_config(page_title="Tic-Tac-Toe", layout="centered", page_icon="🎮")
    st.title("Tic-Tac-Toe Game")
    # Display a styled header
    st.markdown("<h2 style='text-align: center; color: #FFFFFF; background-color: #4CAF50; padding: 10px;'>Enjoy Your Game!</h2>", unsafe_allow_html=True)
    
    # Initialize game state variables in Streamlit session state
    if 'board' not in st.session_state:
        st.session_state.board = initialize_board()
        st.session_state.current_player = 'X'
        st.session_state.players = {'X': 'Player 1', 'O': 'Player 2'}
        st.session_state.winner = None
    
    # Get player names from user input
    if 'player1' not in st.session_state:
        st.session_state.player1 = st.text_input("Enter Player 1 Name:", "Player 1")
        st.session_state.player2 = st.text_input("Enter Player 2 Name:", "Player 2")
        st.session_state.players = {'X': st.session_state.player1, 'O': st.session_state.player2}
    
    # Display the current player's turn
    st.write(f"**{st.session_state.players[st.session_state.current_player]}'s turn ({st.session_state.current_player})**")
    
    # Create a 3x3 button grid for the game board
    cols = st.columns(3)
    for row in range(3):
        for col in range(3):
            if cols[col].button(st.session_state.board[row][col], key=f"{row}-{col}", help="Click to mark"):
                # Check if the selected cell is empty and the game is ongoing
                if st.session_state.board[row][col] == ' ' and st.session_state.winner is None:
                    # Place the current player's mark on the board
                    st.session_state.board[row][col] = st.session_state.current_player
                    # Check if the current player has won
                    if check_winner(st.session_state.board, st.session_state.current_player):
                        st.session_state.winner = st.session_state.current_player
                        st.success(f"{st.session_state.players[st.session_state.winner]} wins! Game Restarting...")
                    # Check if the game is a draw
                    elif is_full(st.session_state.board):
                        st.warning("It's a draw! Game Restarting...")
                    else:
                        # Switch to the other player for the next turn
                        st.session_state.current_player = 'O' if st.session_state.current_player == 'X' else 'X'
    
    # If a player has won or it's a draw, provide a restart button
    if st.session_state.winner or is_full(st.session_state.board):
        if st.button("Restart Game"):
            # Reset the board and game state
            st.session_state.board = initialize_board()
            st.session_state.current_player = 'X'
            st.session_state.winner = None

# Run the Tic-Tac-Toe game
tic_tac_toe()
