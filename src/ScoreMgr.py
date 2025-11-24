SCORE_FILE = "tron_scores.txt"


def init_score_file():
    """Create score file if it doesn't exist"""
    file = open(SCORE_FILE, 'w')
    file.write("Tron:0\n")
    file.write("Clu:0\n")
    file.close()
    print("Score file created")


def read_scores():
    """Read scores from file and return as dictionary"""
    # Try to open the file, if it doesn't exist, create it first
    try:
        file = open(SCORE_FILE, 'r')
    except FileNotFoundError:
        print("Score file not found, creating new one...")
        init_score_file()
        file = open(SCORE_FILE, 'r')

    scores = {}
    for line in file:
        line = line.strip()
        if line and ':' in line:  # Skip empty lines and lines without ':'
            player, score = line.split(':')
            scores[player] = int(score)

    file.close()

    # If scores are missing players, add them with 0
    if 'Tron' not in scores:
        scores['Tron'] = 0
    if 'Clu' not in scores:
        scores['Clu'] = 0

    print(f"Scores loaded: {scores}")
    return scores


def write_scores(scores):
    """Write scores dictionary to file"""
    file = open(SCORE_FILE, 'w')
    file.write(f"Tron:{scores['Tron']}\n")
    file.write(f"Clu:{scores['Clu']}\n")
    file.close()
    print(f"Scores saved: {scores}")


def update_winner(winner):
    """Increment the winner's score by 1"""
    scores = read_scores()

    # Make sure the winner exists in scores
    if winner not in scores:
        scores[winner] = 0

    scores[winner] = scores[winner] + 1
    write_scores(scores)
    print(f"{winner} wins! New score: {scores[winner]}")


def reset_scores():
    """Reset all scores to 0"""
    scores = {"Tron": 0, "Clu": 0}
    write_scores(scores)
    print("Scores reset")