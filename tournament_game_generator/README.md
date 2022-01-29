For this project you will be asked to create a program that can schedule games that teams will play in an end of year tournament. You will only be responsible for determining the games played in the first round of the tournament.

이 프로젝트에서, 당신은 올해 토너먼트에서 여러 팀들이 플레이할 수 있는 게임을 스케쥴할 수 있는 프로그램을 만들어야 합니다. 

You will first need to ask the user of your program to input the number of teams; you may assume there will always be an even number of teams (you don't need to validate this). Next you will need to ask for the names of all of the teams and store them in some way.

당신은 먼저, 팀의 수를 입력하도록 해야 합니다. 팀의 수는 짝수라고 가정할 수 있습니다.(검증할 필요는 없습니다.) 그 다음으로는 그 팀들의 이름을 받고, 어떤 방식으로든 이름을 저장해야 합니다.

After this you'll need to determine the number of games that were played by each team; you may assume each team plays the same number of games. Finally, you'll need to determine the number of wins each team had during the regular season.

그 후에, 당신은 각 팀에게 플레이되는 게임의 수를 확인해야 합니다. 각 팀은 같은 수의 게임을 플레이한다고 확신할 수 있습니다. 마지막으로, 당신은 regular season에서 각 팀의 승리 수를 확인해야 합니다.

When asking for user input, you'll need to make sure all input is valid and ask the user to try again if they give you invalid input. You may assume user input will always be the correct type (i.e. if you ask for a number you will always get an integer). You can determine if the input is invalid by looking at the following constraints:

유저의 입력을 받을 때, 모든 입력이 유효(valid)함을 확실하게 해야 하며, 유효하지 않을 경우에는 다시 입력을 하도록 해야 합니다. 당신은 다음과 같은 조건을 발견할 경우, 입력이 유효하지 않음을 확인할 수 있습니다.

There are always at least 2 teams in the tournament.
Each team plays every other team at least once in the regular season.
All team names contain at most 2 words and at least 2 characters.
Each team has at minimum 0 wins and no more wins than the number of games they played.
In the first round of the tournament the teams with the most regular season wins play the teams with the least regular season wins. For example, if Team A has 5 wins, Team B has 4 wins, Team C has 3 wins and Team D has 2 wins then Team A and Team D play each other and Team B and C play each other. If teams are tied for wins and/or losses then your program can choose any appropriate team.

토너먼트에는 적어도 2개 이상의 팀이 있어야 합니다.
각 팀은 regular season에는 다른 팀과 적어도 한번은 게임을 해야 합니다.
모든 팀의 이름은 최소 2개의 글자, 최대 2개의 단어로 이루어져야 합니다.
각 팀의 승리 수는 0부터 그 팀이 플레이한 게임 수 만큼이어야 합니다.
토너먼트의 첫 라운드에서, regular season의 가장 많은 승리수를 가진 팀은 regular season의 가장 적은 승리수를 가진 팀과 하게 됩니다. 승리수가 같은 경우에 임의로 적절한 팀을 고릅니다.

Your program should output the games that should be played in the format seen below. The first game outputted should contain the team with the most regular season wins, the second game should contain the team with the second most regular season wins, etc. The home team of each game should be the team with the least wins of the two, if there is a tie in wins your program can chose any appropriate team.

당신의 프로그램은, 밑의 포맷과 같이 게임을 출력해야 합니다. 첫번째로 출력되는 게임은 가장 많이 승리한 팀이 포함되어야 하며, 두번째 게임은 두번째로 많이 승리한 팀이 포함되어야 합니다. 각 게임의 홈 팀은 두 팀중 적게 이긴 팀이며, 두 팀이 동점일 경우에 임의의 팀을 고릅니다.

See below for the sample program execution. Your prompts and output should follow the same format as seen below.


Sample Program Execution #1

Enter the number of teams in the tournament: 1
The minimum number of teams is 2, try again.
Enter the number of teams in the tournament: 4
Enter the name for team #1: Python
Enter the name for team #2: Ruby
Enter the name for team #3: JavaScript
Enter the name for team #4: C
Team names must have at least 2 characters, try again.
Enter the name for team #4: C Is Great
Team names may have at most 2 words, try again.
Enter the name for Team #4: C#
Enter the number of games played by each team: 2
Invalid number of games. Each team plays each other at least once in the regular season, try again.
Enter the number of games played by each team: 3
Enter the number of wins Team Python had: 2 
Enter the number of wins Team Ruby had: 1 
Enter the number of wins Team JavaScript had: 0 
Enter the number of wins Team C# had: -2
The minimum number of wins is 0, try again.
Enter the number of wins Team C# had: 3
Generating the games to be played in the first round of the tournament...
Home: JavaScript VS Away: C#
Home: Ruby VS Away: Python

Sample Program Execution #2
Enter the number of teams in the tournament: 6
Enter the name for team #1: AA
Enter the name for team #2: BB
Enter the name for team #3: CC
Enter the name for team #4: DD
Enter the name for team #5: EE
Enter the name for team #6: FF
Enter the number of games played by each team: 2
Invalid number of games. Each team plays each other at least once in the regular season, try again.
Enter the number of games played by each team: 6
Enter the number of wins Team AA had: 1 
Enter the number of wins Team BB had: 4 
Enter the number of wins Team CC had: 3 
Enter the number of wins Team DD had: 4 
Enter the number of wins Team EE had: 2 
Enter the number of wins Team FF had: 7 
The maximum number of wins is 6, try again.
Enter the number of wins Team FF had: 5 
Generating the games to be played in the first round of the tournament...
Home: AA VS Away: FF
Home: EE VS Away: BB
Home: CC VS Away: DD