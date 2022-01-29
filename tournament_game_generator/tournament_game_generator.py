# Write your code here.

def get_number_of_teams():

    while True:
        try:
            number_of_teams = int(input("Enter the number of teams in the tournament: "))
            if number_of_teams < 2 : print("The minimum number of teams is 2, try again.") 
            else : break
        except ValueError:
            print("The number of teams should be integer.")

    return number_of_teams


def get_team_names(num_teams):
    team_names = []
    i = 1
    while i <= num_teams:
        team_name = input("Enter the name for team #{i}: ".format(i=i))
        name_words = team_name.split(" ")
        if len(name_words) <= 1 and len(team_name) <= 1:
            print("Team names must have at least 2 characters, try again.")
        elif len(name_words) > 2 :
            print("Team names may have at most 2 words, try again.")
        else :
            team_names.append(team_name)
            i += 1
    
    return team_names

def get_number_of_games_played(num_teams):
    while True:
        try:
            number_of_games = int(input("Enter the number of games played by each team: "))
            if number_of_games < num_teams-1: 
                print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")
            else:
                break
        except ValueError:
            print("The number of games should be integer.")
            
    return number_of_games

def get_team_wins(team_names, games_played):
    team_wins = []
    i = 0
    while i < len(team_names):
        team = team_names[i]
        try:
            team_win = int(input("Enter the number of wins Team {team} had: ".format(team=team)))
        except ValueError:
            print("The number of wins should be integer.")
        else:
            if team_win < 0 :
                print("The minimum number of wins is 0, try again.")
            elif team_win > games_played:
                print("The maximum number of wins is {games_played}, try again.".format(games_played=games_played))
            else :
                team_wins.append(team_win)
                i += 1
    
    return team_wins

# It is not necessary to use the functions defined above. There are simply here
# to help give your code some structure and provide a starting point.
num_teams = get_number_of_teams()
team_names = get_team_names(num_teams)
games_played = get_number_of_games_played(num_teams)
team_wins = get_team_wins(team_names, games_played)

print("Generating the games to be played in the first round of the tournament...")

# get order of teams by wins
index_of_team_sorted_by_wins = sorted(range(num_teams), key = lambda x : team_wins[x])
#print(index_of_team_sorted_by_wins)

for i in range(num_teams//2):

    away_team_idx = index_of_team_sorted_by_wins[num_teams-1-i]
    home_team_idx = index_of_team_sorted_by_wins[i]
    print("Home: {home_team} VS Away: {away_team}".format(home_team=team_names[home_team_idx], away_team=team_names[away_team_idx]))