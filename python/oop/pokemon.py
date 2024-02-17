# TASK 2
class Pokemon:
    def __init__(self,name1,name2,power1,power2,damage):
        self.pokemon1_name=name1
        self.pokemon2_name=name2
        self.pokemon1_power=power1
        self.pokemon2_power=power2
        self.damage_rate=damage

    
# Write your code for class here

team_pika = Pokemon('pikachu', 'charmander', 90, 60, 10)
print('=======Team 1=======')
print('Pokemon 1:',team_pika.pokemon1_name, team_pika.pokemon1_power)
print('Pokemon 2:',team_pika.pokemon2_name, team_pika.pokemon2_power)
pika_combined_power = (team_pika.pokemon1_power + team_pika.pokemon2_power) * team_pika.damage_rate
print('Combined Power:', pika_combined_power)

# Write your code for subtask 2 and 3 here
print("=======Team 2=======")
team_bulb=Pokemon('bulbasaur', 'squirtle', 80, 70, 9)
print('Pokemon 1:',team_bulb.pokemon1_name, team_bulb.pokemon1_power)
print('Pokemon 2:',team_bulb.pokemon2_name, team_bulb.pokemon2_power)
bulb_combined_power = (team_bulb.pokemon1_power + team_bulb.pokemon2_power) * team_bulb.damage_rate
print('Combined Power:', bulb_combined_power)
