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

def print_leaderboard():
    print(  f'TOURNAMENT LEADERBOARD\n',
            *[f'{'{:<3}'.format(i)}. {'{:<10}'.format(name)} - {points} points' for i,(name,points) in enumerate(player_rankings,start=1)],
            sep='\n'
    )

print_leaderboard()

#Part 8
