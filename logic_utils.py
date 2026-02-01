import random

def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str): #FIX: Refractored parse and check into logic_utils file
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"  # Fixed: Previously said "Go HIGHER!" which was wrong
        else:
            return "Too Low", "📈 Go HIGHER!"  # Fixed: Ensures correct hint direction
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score


def handle_difficulty_change(session_state, new_difficulty):
    """Handle difficulty change by resetting game state and incrementing game_id."""  # Added: Function to auto-reset game on difficulty change
    if session_state.get('current_difficulty') != new_difficulty:
        session_state['attempts'] = 1
        low, high = get_range_for_difficulty(new_difficulty)
        session_state['secret'] = random.randint(low, high)
        session_state['status'] = "playing"
        session_state['history'] = []
        session_state['game_id'] = session_state.get('game_id', 0) + 1
        session_state['current_difficulty'] = new_difficulty


def handle_new_game(session_state, difficulty):
    """Handle new game by resetting game state and incrementing game_id."""  # Added: Function to reset game and clear input
    session_state['attempts'] = 1
    low, high = get_range_for_difficulty(difficulty)
    session_state['secret'] = random.randint(low, high)
    session_state['status'] = "playing"
    session_state['history'] = []
    session_state['game_id'] = session_state.get('game_id', 0) + 1
