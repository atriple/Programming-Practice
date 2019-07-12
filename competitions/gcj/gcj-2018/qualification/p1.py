t = int(input())
for i in range (1, t+1):
    D, P = [s for s in input().split(" ")]
    D = int(D)

    # Organize Shot Tier into List
    # Example : SSCSSSCCSSSC --> [2,3,0,3,0]
    shot_per_tier = []
    shot_count = 0
    for command in P:
        if command == 'S':
            shot_count += 1
        if command == 'C':
            shot_per_tier.append(shot_count)
            shot_count = 0 

    if P[-1] == 'S' :
        shot_per_tier.append(shot_count) #Add the leftovers that can't be appended wihout C appearing

    # Count Initial Damage
    multiplier = 1
    damage_per_tier = []
    for shot in shot_per_tier:
        damage_per_tier.append(multiplier * shot)
        multiplier *= 2

    total_damage = 0
    for damage in damage_per_tier:
        total_damage += damage
  
    if total_damage <= D:
        output = 0
    else :
        output = "IMPOSSIBLE"
        charge_tier = len(shot_per_tier) - 1 #Intialize Current Tier, start from the tail of command
        converted_damage = (2 ** charge_tier) - (2 ** (charge_tier - 1)) # Initialize
        hack_count = 0
        while(charge_tier > 0):
            if shot_per_tier[charge_tier] == 0:
                charge_tier -= 1
                converted_damage = (2 ** charge_tier) - (2 ** (charge_tier - 1))
            
            total_damage -= converted_damage
            shot_per_tier[charge_tier] -= 1
            shot_per_tier[charge_tier - 1] += 1
            hack_count += 1

            if total_damage <= D:
                output = hack_count
                break 

    print("Case #{}: {}".format(i, output)) #OUTPUT, you might need to modify it if it produce >1 output