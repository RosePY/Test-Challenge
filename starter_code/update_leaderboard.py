import os
import sys
from datetime import datetime

LEADERBOARD_FILE = "leaderboard.md"
SCORE_FILE = "score.txt"

def read_score():
    if not os.path.exists(SCORE_FILE):
        raise FileNotFoundError("score.txt not found. Make sure scoring_script.py creates it.")
    with open(SCORE_FILE, "r") as f:
        return float(f.read().strip())

def read_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        return []
    rows = []
    with open(LEADERBOARD_FILE, "r") as f:
        for line in f.readlines():
            if line.startswith("|") and "Rank" not in line:
                parts = [p.strip() for p in line.split("|")[1:-1]]
                rows.append(parts)
    return rows

def write_leaderboard(entries):
    with open(LEADERBOARD_FILE, "w") as f:
        f.write("# Leaderboard\n\n")
        f.write("| Rank | Submission | Score |\n")
        f.write("|------|------------|-------|\n") 
        for i, (submission, score) in enumerate(entries, start=1):
            f.write(f"| {i} | {submission} | {score:.4f} |\n")

def main():
    submission = os.environ.get("SUBMISSION_FILE", "unknown")
    score = read_score()

    entries = read_leaderboard()

    # Remove previous entry with same submission name (if any)
    entries = [e for e in entries if e[0] != submission]

    # Add new entry
    entries.append((submission, score))

    # Sort by score (descending)
    entries.sort(key=lambda x: float(x[1]), reverse=True)

    write_leaderboard(entries)

if __name__ == "__main__":
    main()
