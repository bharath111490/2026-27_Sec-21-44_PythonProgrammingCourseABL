# Sports Tournament Ranking System

teams = int(input("Enter number of teams: "))

team_data = []

for i in range(teams):
    print(f"\nTeam {i + 1}")

    name = input("Enter team name: ")
    wins = int(input("Enter number of wins: "))
    draws = int(input("Enter number of draws: "))
    losses = int(input("Enter number of losses: "))
    goals_scored = int(input("Enter goals scored: "))
    goals_conceded = int(input("Enter goals conceded: "))

    # Competition Policy
    points = (wins * 3) + (draws * 1)
    goal_difference = goals_scored - goals_conceded

    team_data.append([
        name,
        points,
        goal_difference,
        goals_scored
    ])

# Ranking Rules:
# 1. Higher Points
# 2. Higher Goal Difference
# 3. Higher Goals Scored

team_data.sort(
    key=lambda x: (x[1], x[2], x[3]),
    reverse=True
)

print("\nTournament Rankings")

rank = 1

for team in team_data:
    print(
        f"{rank}. {team[0]} - "
        f"Points: {team[1]}, "
        f"Goal Difference: {team[2]}, "
        f"Goals Scored: {team[3]}"
    )
    rank += 1