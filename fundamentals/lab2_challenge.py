'''
Lab2 Challenge 260918
'''

#Part 1
sessions = [
    {'session_title' : 'Python Fundamentals', 'speaker' : 'Anna', 'room' : 'Room A', 'start_time' : '09:00', 'duration' : 60, 'topic' : 'Fundamentals', 'max_part' : 100},
    {'session_title' : 'SQL & Databases', 'speaker' : 'Bob', 'room' : 'Room B', 'start_time' : '10:00', 'duration' : 60, 'topic' : 'Data', 'max_part' : 100},
    {'session_title' : 'API, Integration, Git', 'speaker' : 'Anna', 'room' : 'Room C', 'start_time' : '11:00', 'duration' : 60, 'topic' : 'API', 'max_part' : 100},
    {'session_title' : 'Team Project', 'speaker' : 'Victoria', 'room' : 'Room A', 'start_time' : '13:00', 'duration' : 60, 'topic' : 'Project', 'max_part' : 100},
    {'session_title' : 'Data Analysis & Visualization', 'speaker' : 'Jimmy', 'room' : 'Room B', 'start_time' : '14:00', 'duration' : 60, 'topic' : 'Data', 'max_part' : 100},
    {'session_title' : 'ML / DL', 'speaker' : 'Hans', 'room' : 'Room C', 'start_time' : '15:00', 'duration' : 60, 'topic' : 'AI', 'max_part' : 100},
    {'session_title' : 'LLM / Prompting', 'speaker' : 'Frank', 'room' : 'Room A', 'start_time' : '16:00', 'duration' : 60, 'topic' : 'AI', 'max_part' : 100},
    {'session_title' : 'AI Agents', 'speaker' : 'Hans', 'room' : 'Room D', 'start_time' : '17:00', 'duration' : 60, 'topic' : 'AI', 'max_part' : 100}
]

speakers = set([d['speaker'] for d in sessions])
# print(speakers)

rooms = set([d['room'] for d in sessions])
# print(rooms)

topics = set(d['topic'] for d in sessions)
# print(topics)

registered_part = [ ('Eric','Python Fundamentals'),('Hasse','Python Fundamentals'),('Linda','SQL & Databases'),('Göran','SQL & Databases'),('Frank','Team Project'),
                    ('Cecilia','Data Analysis & Visualization'),('Li','ML / DL'),('Petter','ML / DL'),('David','LLM / Prompting'),('Guido','AI Agents')
]

#Part 2

# print('First session title:',sessions[0]['session_title'])
# print('Third session speaker:',sessions[2]['speaker'])
# print('Room of the last session:',sessions[-1]['room'])
# print('All info on 2nd session:',sessions[1])
# print('Last reg participant name:', registered_part[-1][0])
# print('First 3 sessions:',*sessions[:3],sep='\n')
# print('Last 2 sessions:',*sessions[-2:],sep='\n')
# reveresed_session = sessions[::-1]
# print(*reveresed_session,sep='\n')
# partial_sessions = sessions[1::2]
# print(*partial_sessions,sep='\n')

#Part 3
sessions[6]['room'] = 'Room B'
sessions[7]['speaker'] = 'Jimmy'
sessions.append({'session_title' : 'AI Security', 'speaker' : 'Hans', 'room' : 'Room C', 'start_time' : '18:00', 'duration' : 60, 'topic' : 'AI', 'max_part' : 100})
del sessions[3]
registered_part.append(('Klas','AI Security'))
del registered_part[4]
sessions[7].update({'difficulty' : 'Advanced'})

# print(*sessions,sep='\n')
# print(*registered_part,sep='\n')

#Part 4
#AI halucinating about workshops

#Part 5
conference_data = {
    '1995-04-10' : {'opening_time' : '08:00', 'closing_time' : '18:00', 
    'session_time_slots' : ['08:00','09:00','10:00','11:00','13:00','14:00','15:00','16:00','17:00']}
}

session_slots_on_date = conference_data['1995-04-10']['session_time_slots']
# print(session_slots_on_date)
session_open_close_on_date = (conference_data['1995-04-10']['opening_time'],conference_data['1995-04-10']['closing_time'])
# print(session_open_close_on_date)

#Part 6

backup_participants = registered_part
# print(backup_participants)
# del backup_participants[0]
# print(registered_part)

#backup_participants refer to the value in registered_part and changes to it will change the value

backup_participants = registered_part.copy() # or [*registered_part]
# print(backup_participants)
backup_participants.clear()
# print(backup_participants)
# print(registered_part)

#This creates an actual copy of the list and wont change the original value

#Part 7

session_titles = ['Python for AI', 'Building APIs', 'Introduction to LLMs']
speakers = ['Ada','Grace','Alan']
rooms = ['Room A','Room B','Room C']
combined_sessions = list(zip(session_titles,speakers,rooms))

# print(f'Second session title: {combined_sessions[1][0]} speaker: {combined_sessions[1][1]} room: {combined_sessions[1][2]}')

#Final Challenge

the_conference = {
    'conference_data' : conference_data,    #dict
    'session_data' : {
        'sessions' : sessions,  #list of dict
        'speakers' : speakers,  #set
        'rooms' : rooms,    #set
        'participants' : registered_part,   #list of tuple
        'topics' : topics   #set
        }
}

# print(the_conference['session_data']['sessions'][1]['speaker'])

#It just works TM

