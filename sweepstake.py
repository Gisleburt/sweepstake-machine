# sweepstake.py

import numpy as np
import pandas as pd

def get_assignments(my_seed):
    
    data = pd.read_csv("world_cup_sweepstake.csv")
    
    people = data.names.values
    
    good_teams = data.top_teams.values
    
    bad_teams = data.bottom_teams.values
    
    np.random.seed(my_seed)
    
    np.random.shuffle(people)
    np.random.shuffle(bad_teams)
    np.random.shuffle(good_teams)
    
    assigned_bad  = zip(people, bad_teams) 
    assigned_good = zip(people, good_teams)
    
    return assigned_bad, assigned_good

def make_sweepstake():
    
    dice_seed_s = raw_input(
        "ROLL A DIE AND ENTER THE NUMBER YOU GET. THEN PRESS ENTER... \n"
    )
    
    dice_seed = int(dice_seed_s)
    
    assigned_bad, assigned_good = get_assignments(dice_seed)
    
    print '----- BAD TEAMS ---- \n'
    
    for name, team in assigned_bad:
        print name, team
        _ = raw_input('') # pause
    
    print '----- GOOD TEAMS ---- \n'
    
    for name, team in assigned_good:
        print name, team
        _ = raw_input('') # pause
    
    bad_df = pd.DataFrame(assigned_bad, columns=['name','bad_team']).set_index('name')
    good_df = pd.DataFrame(assigned_good, columns=['name','good_team']).set_index('name')
    
    results = bad_df.join(good_df)
    
    return results.sort_index()

if __name__ == "__main__":
    
    results = make_sweepstake()

