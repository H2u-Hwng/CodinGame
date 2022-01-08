# Problem: https://docs.google.com/document/d/1D-3t64PnsEpcF6kKz5ZaquoMMB-r5UyYGyZzM4hjyi0/edit?usp=sharing

def create_dict():
    ''' Create a dictionary including the roles and their damages. '''
    
    n = int(input('Enter the number of your party members: '))
    
    party = {} # initialize a dictionary named party

    for _ in range(n):
        # prompt the user for the role and its damage
        inputs = input('Enter the role and its nominal damage (separated by a space): ').split()
        
        role = inputs[0]
        damage = float(inputs[1])
        party[damage] = role
    
    return party

  
def main():
    ''' define main function. '''
    
    party = create_dict() # determine the dictionary named party
    
    sorted_damage = sorted(party) # sorted the roles' damage
    
    print() # for readability
    
    # determine and display the role who attacks from front
    damage_front = party[sorted_damage[-1]]
    print('The role who attacks from front:', damage_front)
    
    # determine and display the role who attacks from one side
    damage_side = party[sorted_damage[-3]]
    print('The role who attacks from one side:', damage_side)
    
    # determine and display the role who attacks from other side
    damage_other_side = party[sorted_damage[-4]]
    print('The role who attacks from other side:', damage_other_side)
    
    # determine and display the role who attacks from back
    damage_back = party[sorted_damage[-2]]
    print('The role who attacks from back:', damage_back)
    
    # determine and display the total damaged
    total_damaged = sorted_damage[-1]/2 + sum(sorted_damage[-4:-2]) + sorted_damage[-2]*2 
    print('The total damage dealt to the cyclops by the party:', total_damaged)

# call main funciton
main()
