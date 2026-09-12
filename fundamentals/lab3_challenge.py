'''
Lab3 Challenge 260911
'''

#Part 1
flights = [
    {'flight' : 'KL1228', 'destination' : 'Amsterdam', 'departure' : '06:00', 'gate' : '17', 'passengers' : 355, 'max_cap' : 380, 'delay' : 6, 'cancelled' : False},
    {'flight' : 'LH2433', 'destination' : 'Munich', 'departure' : '06:00', 'gate' : '16', 'passengers' : 375, 'max_cap' : 380, 'delay' : 0, 'cancelled' : False},
    {'flight' : 'LX1223', 'destination' : 'Zürich', 'departure' : '14:55', 'gate' : '13', 'passengers' : 329, 'max_cap' : 380, 'delay' : 57, 'cancelled' : False},
    {'flight' : 'FR6090', 'destination' : 'Gdansk', 'departure' : '15:20', 'gate' : '20A', 'passengers' : 345, 'max_cap' : 380, 'delay' : -5, 'cancelled' : False},
    {'flight' : 'DK1766', 'destination' : 'Palma', 'departure' : '18:45', 'gate' : '21A', 'passengers' : 367, 'max_cap' : 380, 'delay' : 13, 'cancelled' : False},
    {'flight' : 'LH819', 'destination' : 'Frankfurt', 'departure' : '18:55', 'gate' : '20A', 'passengers' : 355, 'max_cap' : 380, 'delay' : 19, 'cancelled' : False},
    {'flight' : 'AY868', 'destination' : 'Helsinki', 'departure' : '20:55', 'gate' : '17', 'passengers' : 372, 'max_cap' : 380, 'delay' : -9, 'cancelled' : False},
    {'flight' : 'FR4013', 'destination' : 'Alicante', 'departure' : '21:10', 'gate' : '20A', 'passengers' : 362, 'max_cap' : 380, 'delay' : 25, 'cancelled' : False},
    {'flight' : 'WF209', 'destination' : 'Bergen', 'departure' : '22:05', 'gate' : '14', 'passengers' : 378, 'max_cap' : 380, 'delay' : -1, 'cancelled' : False},
    {'flight' : 'FR4011', 'destination' : 'Krakow', 'departure' : '23:15', 'gate' : '13', 'passengers' : 345, 'max_cap' : 380, 'delay' : 121, 'cancelled' : False}
]

#Part 2
def departure_board():
    for i,flight in enumerate(flights):
        print(  f'{'{:>2}'.format(i+1)}. '
                f'{'{:<7}'.format(flight['flight'])}- '
                f'{'{:<10}'.format(flight['destination'])}- '
                f'{'{:<6}'.format(flight['departure'])}- '
                f'Gate {'{:<4}'.format(flight['gate'])}- '
                f'{'{:<12}'.format(flight_status(flight['delay'],flight['cancelled']))}'
)

# departure_board()

#Part 3
def flight_status(delay,cancelled):
    if cancelled:
        return 'CANCELLED'
    elif delay in range (1,20):
        return 'SLIGHT DELAY'
    elif delay in range (20,60):
        return 'DELAYED'
    elif delay >= 60:
        return 'SEVERELY DELAYED'
    else:
        return 'ON TIME'
    
#Part 4
def airport_statistics():
    cancelled, delayed, total_pass, largest_pass, filled_flights = 0,0,0,0,0
    for flight in flights:
        if flight['cancelled']: cancelled += 1
        if flight['delay'] > 0: delayed += 1
        if flight['passengers'] > largest_pass: largest_pass = flight['passengers']
        if flight['passengers'] / flight['max_cap'] >= 0.8: filled_flights += 1
        total_pass += flight['passengers']

    print(  f'# of flights: {len(flights)}',
            f'# of cancelled flights: {cancelled}',
            f'# of delayed flights: {delayed}',
            f'# of on-time flights: {len(flights)-delayed}',
            f'# of total passengers: {total_pass}',
            f'# of average passenger per flight: {round(total_pass/len(flights))}',
            f'# of passengers in the highest load flight: {largest_pass}',
            f'# of flights with >80% capacity: {filled_flights}',
            sep='\n'
)

# airport_statistics()

#Part 5


