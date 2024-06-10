#!/usr/bin/env python3
import sys

player_info = []

def is_left_dominant(p1, p2):
    if p1[1] >= p2[1] and p1[2] >= p2[2] and (p1[1] > p2[1] or p1[2] > p2[2]):
        return True
    return False


for player in sys.stdin:
    player = player.strip()
    name, value = player.split("\t")
    value = value.split(",")
    name = name.strip()
    goal = int(value[0])
    assist = int(value[1])
    p1 = (name, goal, assist)

    if(player_info==[]):
        player_info.append(p1)
    else:
        p1_inserted = True
        for p2 in player_info:
            if(is_left_dominant(p2,p1)):
                p1_inserted = False
                break
        if(p1_inserted==False):
            continue
        for p2 in player_info:
            if(is_left_dominant(p1,p2)):
                player_info.remove(p2)
        player_info.append(p1)

for player in player_info:
    print(player[0])
