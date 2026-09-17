'''
Lab6 Challenge 260917
'''

#Part 1
players = [
    {'player_name': 'Devilwalk', 'team' : 'FnaTIC', 'country' : 'Sweden', 'score' : 80, 'matches_played' : 5, 'wins' : 1, 'active' : False},
    {'player_name': 'JW', 'team' : 'FnATIc', 'country' : 'Sweden', 'score' : 150, 'matches_played' : 5, 'wins' : 5, 'active' : True},
    {'player_name': 'flusha', 'team' : '    Fnatic', 'country' : 'Sweden', 'score' : 90, 'matches_played' : 5, 'wins' : 5, 'active' : True},
    {'player_name': 'pronax', 'team' : '   Fnatic', 'country' : 'Sweden', 'score' : 100, 'matches_played' : 5, 'wins' : 5, 'active' : True},
    {'player_name': 'schneider', 'team' : 'Fnatic', 'country' : 'Sweden', 'score' : 90, 'matches_played' : 5, 'wins' : 2, 'active' : False},
    {'player_name': 'f0rest', 'team' : 'Ninjas in PyjAMas     ', 'country' : 'Sweden', 'score' : 180, 'matches_played' : 5, 'wins' : 4, 'active' : True},
    {'player_name': 'GeT RiGhT', 'team' : 'Ninjas in Pyjamas', 'country' : 'Sweden', 'score' : 150, 'matches_played' : 5, 'wins' : 4, 'active' : True},
    {'player_name': 'Xizt', 'team' : 'Ninjas in Pyjamas', 'country' : 'Sweden', 'score' : 90, 'matches_played' : 5, 'wins' : 4, 'active' : True},
    {'player_name': 'friberg', 'team' : '    Ninjas in Pyjamas', 'country' : 'Sweden', 'score' : 80, 'matches_played' : 5, 'wins' : 4, 'active' : True},
    {'player_name': 'Fifflaren', 'team' : 'Ninjas in Pyjamas', 'country' : 'Sweden', 'score' : 70, 'matches_played' : 5, 'wins' : 3, 'active' : False},
    {'player_name': 'shox', 'team' : 'VeryGames', 'country' : 'France', 'score' : 100, 'matches_played' : 5, 'wins' : 2, 'active' : True},
    {'player_name': 'SmithZz', 'team' : '    VeryGames', 'country' : 'France', 'score' : 60, 'matches_played' : 5, 'wins' : 3, 'active' : False},
    {'player_name': 'NBK', 'team' : 'VeryGames', 'country' : 'France', 'score' : 80, 'matches_played' : 5, 'wins' : 3, 'active' : True},
    {'player_name': 'ScreaM', 'team' : 'VeryGAMES    ', 'country' : 'France', 'score' : 150, 'matches_played' : 5, 'wins' : 3, 'active' : True},
    {'player_name': 'Ex6TenZ', 'team' : 'VERYGames', 'country' : 'France', 'score' : 70, 'matches_played' : 5, 'wins' : 2, 'active' : False}
]

#Part 2

cleaned_players = [{key:val.strip().lower().title() if isinstance(val,str) else val for key,val in d.items()} for d in players]
# print(cleaned_players)

#Part 3

active_players = [d for d in cleaned_players if d['active']]
# print(*active_players,sep='\n')

players_3_wins = [d for d in cleaned_players if d['wins'] >= 3]
# print(*players_3_wins,sep='\n')

players_100_score = [d for d in cleaned_players if d['score'] >= 100]
# print(*players_100_score,sep='\n')

players_sweden = [d for d in cleaned_players if d['country'] >= 'Sweden']
# print(*players_sweden,sep='\n')

players_100score_5wins = [d for d in cleaned_players if d['score'] >= 100 and d['wins'] >= 5]
# print(*players_100score_5wins,sep='\n')

#Part 4
countries = set([d['country'] for d in cleaned_players])
# print(countries)

teams = set([d['team'] for d in cleaned_players])
# print(teams)

player_to_score = {d['player_name'] : d['score'] for d in cleaned_players}
# print(player_to_score)

player_to_wins = {d['player_name'] : d['wins'] for d in cleaned_players}
# print(player_to_wins)

playername_100_score = {'good_players' : {d['player_name'] for d in cleaned_players if d['score'] >= 100}}
# print(playername_100_score)

#Part 5
player_names = [d['player_name'] for d in cleaned_players]
ranking = [d['score'] * d['wins'] for d in cleaned_players]
player_country_active = [d['country'] for d in cleaned_players if d['active']]

zippedidoodaa = zip(player_names,ranking,player_country_active)
# print(*zippedidoodaa,sep='\n')

#zip() halts when the shortest itterable has been exhausted. results will contain all combined elements up to len(shortest_data)

#Part 6

asc_highest_score = sorted(cleaned_players,key=lambda p: p['score'])
desc_highest_score = sorted(cleaned_players,key=lambda p: p['score'],reverse=True)
# print(asc_highest_score[-1],desc_highest_score[0])

most_wins = sorted(cleaned_players,key=lambda p: p['wins'],reverse=True)
# print(most_wins)

most_matches = sorted(cleaned_players,key=lambda p: p['matches_played'],reverse=True)
# print(most_matches)

names_alphabetic = sorted(cleaned_players,key=lambda p: p['player_name'])
# print(names_alphabetic)

#Part 7

player_rankings = sorted(zip(player_names,ranking),key=lambda t: t[1],reverse=True)
ranked_numbered_strings = [f'{'{:<3}'.format(i)}. {'{:<10}'.format(name)} - {points} points' for i,(name,points) in enumerate(player_rankings,start=1)]
wins_rankings = sorted(player_to_wins.items(),key=lambda p: p[1],reverse=True)
wins_numbered_strings = [f'{'{:<3}'.format(i)}. {'{:<10}'.format(name)} - {wins} wins' for i,(name,wins) in enumerate(wins_rankings,start=1)]


def print_leaderboard():
    print(  f'TOURNAMENT LEADERBOARD\n',
            *ranked_numbered_strings,
            sep='\n'
    )

# print_leaderboard()

#Part 8
teams_players = {team : {d['player_name'] for d in cleaned_players if d['team'] == team} for team in teams}
# print(teams_players)

players_5_wins = {d['player_name'] : d['wins'] for d in cleaned_players if d['wins'] >= 5}
# print(players_5_wins)

represented_teams = set([d['team'] for d in cleaned_players])
# print(represented_teams)

represented_countries = set([d['country'] for d in cleaned_players])
# print(represented_countries)

active_highscore = {d['player_name'] : d['score'] for d in cleaned_players if d['score'] >= 100}
# print(active_highscore)

#Part 9
player_performance = {d['player_name'] : d['score'] + 100 * d['wins'] / d['matches_played'] for d in cleaned_players}
sorted_player_performance = dict(sorted(player_performance.items(),key=lambda p: p[1],reverse=True))
players_ranked_performance = {d['player_name'] : player_performance[d['player_name']] for d in cleaned_players if player_performance[d['player_name']] >= 200}
sorted_ranked_performance = dict(sorted(players_ranked_performance.items(),key=lambda p: p[1],reverse=True))

# print(sorted_player_performance)
# print(sorted_ranked_performance)

#Part 10

def final_report() -> [str]:
    return [f'LE BIG TOURNAMENT REPORT\n{'='*24}',
            f'Total # of Players: {len(cleaned_players)}',      
            f'Number of active Players: {len(active_players)}',
            f'Unique Teams: {', '.join(teams)}',
            f'Unique Contries: {', '.join(countries)}',
            f'Players Ranked by Score:',
            *ranked_numbered_strings,
            f'Players Ranked by Wins:',
            *wins_numbered_strings,
            f'Top 5 Players: {', '.join(list(sorted_player_performance)[:5])}',
            f'Players Performing Well: {', '.join(playername_100_score['good_players'])}'
    ]

# print(*final_report(),sep='\n')
