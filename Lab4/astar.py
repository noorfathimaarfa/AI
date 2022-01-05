def h_n(state,target):
    dist=0
    for i in state:
        d1,d2=state.index(i),target.index(i)
        x1,y1=d1%3,d1//3
        x2,y2=d2%3,d2//3
        dist+=abs(x1-x2)+abs(y1-y2)
    return dist
def print_grid(src):
    state=src.copy()
    state[state.index(-1)]=' '
    print(
        f"""
{state[0]}{state[1]}{state[2]}
{state[3]}{state[4]}{state[5]}
{state[6]}{state[7]}{state[8]}
"""
        )
def aStar(src,target):
    states=[src]
    g=0
    visited_states= set()
    while len(states):
        print(f"Level:{g}")
        moves=[]
        for state in states:
            visited_states.add(tuple(state))
            print_grid(state)
            if state==target:
                print("Success")
                return
            moves+=[move for move in possible_moves(state,visited_states) if move not in moves]
            cost=[g+h_n(move,target) for move in moves]
            states=[moves[i] for i in range(len(moves)) if cost[i]==min(cost)]
            g+=1
    print("Fail")
def possible_moves(state,visited_states):
    b=state.index(-1)
    d=[]
    if b-3 in range(9):
        d.append('u')
    if b not in [0,3,6]:
        d.append('l')
    if b not in [2,5,8]:
        d.append('r')
    if b+3 in range(9):
        d.append('d')
    pos_moves=[]
    for move in d:
        pos_moves.append(gen(state,move,b))
    return [move for move in pos_moves if tuple(move) not in visited_states]
def gen(state,m,b):
    temp=state.copy()
    if m=='u':
        temp[b-3],temp[b]=temp[b],temp[b-3]
    if m=='l':
        temp[b-1],temp[b]=temp[b],temp[b-1]
    if m=='r':
        temp[b+1],temp[b]=temp[b],temp[b+1]
    if m=='d':
        temp[b+3],temp[b]=temp[b],temp[b+3]
    return temp
src = [1,2,3,-1,4,5,6,7,8]
target = [1,2,3,4,5,-1,6,7,8]         
       


aStar(src, target)
