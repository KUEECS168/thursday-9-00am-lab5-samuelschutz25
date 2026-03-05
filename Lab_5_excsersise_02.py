def function ():
    planets = [' ', 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', ' ']
    
    user = 0
    mission = ""
    
    while mission.lower() != "y" :
        user = input("Enter a planet name: ")
        mission = input ("Is the mission over? (y/n): ")

    neighbors = input("which planet do you want the neighbors for?: ")

    index = planets.index (neighbors)

    print ('the planets neighboring ', (neighbors), 'are' ,planets [index-1], 'and', planets [index+1])




function()
    
print ("Program ending...")
