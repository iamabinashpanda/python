# Create a list of tuples containing the 5 planets of our solar system along with
# their moons as- earth having 1 moon, Jupiter having 79 moons, Saturn having
# 82 moons, Uranus having 27 moons and Neptune having 14 moons. Sort the
# list according to the ascending number of moons along with the names of
# planet using Lambda function. Display both original and sorted list.

planets = [("Earth",1),("Jupiter",79),("Saturn",82),("Uranus",27),("Neptune",14)]
print(sorted(planets,key=lambda planet: planet[1]))
