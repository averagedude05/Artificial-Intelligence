import random
table = {
    ('A', 'Clean'): random.choice(['Down','Left']),
    ('A', 'Dirty'): 'Suck',
    ('B', 'Clean'): random.choice(['Down','Right']),  
    ('B', 'Dirty'): 'Suck',
    ('D', 'Clean'): random.choice(['Up','Left']),  
    ('D', 'Dirty'): 'Suck',
    ('C', 'Clean'): random.choice(['Up','Right']),    
    ('C', 'Dirty'): 'Suck'
}
percepts=[]  # to store percept sequence
def table_driven_agent(percept):
    print('Perception Received: '+ str(percept))
    percepts.append(percept) # updating percept history
    action = lookup(percept,table) # searching for action
    return action

def lookup(p,t):
    return t[p]
import random
Location = random.choice(['A','B','C','D'])
Condition= random.choice(['Clean','Dirty'])
while True: # to perceieve environment repeatedly
    action = table_driven_agent((Location, Condition))
    print('Action Performed: '+ action)
    cmd = input('Get Perception (yes/no): ')
    if(cmd != 'yes'): break
    if action == 'Right':
      if Location == 'A':
        Location = 'B'
        Condition = random.choice(['Clean','Dirty'])
      elif Location == 'C':
        Location = 'D'
        Condition = random.choice(['Clean','Dirty'])
    elif action == 'Left':
        if Location == 'B':
          Location = 'A'
          Condition = random.choice(['Clean','Dirty'])
        elif Location == 'D':
          Location = 'C'
          Condition = random.choice(['Clean','Dirty'])
    elif action == 'Down':
        if Location == 'A':
          Location = 'C'
          Condition = random.choice(['Clean','Dirty'])
        elif Location== 'B':
          Location = 'D'
          Condition = random.choice(['Clean','Dirty'])
    elif action == 'Up':
        if Location == 'C': Location = 'A'
        elif Location == 'D': Location = 'B'
        Condition = random.choice(['Clean','Dirty'])
    else:
        Condition = 'Clean'