from logic_utils import check_guess, get_range_for_difficulty, handle_difficulty_change, handle_new_game
import random

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")

def test_new_game_increments_game_id():  # Added: Test that new game clears input by incrementing game_id
    # Simulate session_state as a dict
    session_state = {'game_id': 5}
    difficulty = 'Normal'
    
    handle_new_game(session_state, difficulty)
    
    # Check that game_id incremented
    assert session_state['game_id'] == 6
    # This increment causes the text_input key to change, clearing the input field

def test_difficulty_change_increments_game_id():
    # Simulate session_state as a dict
    session_state = {'current_difficulty': 'Easy', 'game_id': 2}
    new_difficulty = 'Hard'
    
    handle_difficulty_change(session_state, new_difficulty)
    
    # Check that game_id incremented
    assert session_state['game_id'] == 3
    # This increment causes the text_input key to change, clearing the input field
