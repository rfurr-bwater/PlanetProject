import pandas as pd 

class planet():
    def __init__(self,name,radius=1,color='blue'):
        self.name = name
        self.radius = radius
        self.color = color
        self.moon_list = []

class moon():
    def __init__(self,name,radius=1,color='white',tidally_locked=False,planet_companion=None):
        self.name = name
        self.radius = radius
        self.color = color
        self.tidally_locked = tidally_locked
        self.planet_companion = planet_companion
    
    def update_planet(self):
        self.planet_companion.moon_list.append(self)

def print_largest(pl):
    largest = None  #will be a moon type object
    for moon in pl.moon_list:
        if largest is None:
            largest = moon
        else:
            if largest.radius < moon.radius: largest = moon      
    if largest is not None:
        print(f"The largest moon of {pl.name} is {largest.name}")

def print_locked_moons(planet):
    print(f"The planet {planet.name} has the following tidally-locked moons:")
    for m in planet.moon_list:
        if m.tidally_locked:
            print("* "+m.name)

if __name__ == "__main__":
    df = pd.read_csv('planet_data.csv', index_col='eName')
    df = df[['isPlanet','meanRadius','orbit_type','orbits']]

    planet_d = dict() #key: name of planet. value: planet object
    moon_d = dict() #key: name of moon. value: moon object

    for index, row in df.iterrows(): # Get all the planets first
        if row['isPlanet'] == True:
            planet_d[index] = planet(
                name = index,
                radius = row['meanRadius']
            )

    for index, row in df.iterrows(): # Then, get the moons
        if row['isPlanet'] == False:
            moon_d[index] = moon(
                name = index,
                radius = row['meanRadius'],
                planet_companion = planet_d[row['orbits']] # Grab the planet the moon orbits, and plug it in as a key in the planets dictionary to get the object
            )

    for key, val in planet_d.items():  #now we can check to see what is in our planet dictionary
        print(key, val.radius)

    for key, val in moon_d.items(): #check that the planets got updated
        val.update_planet()
        print(key, val.radius, val.planet_companion.name)

    for key, val in planet_d.items():  #get the largest moon for each planet!
        print_largest(val) #sample output: The largest moon of Uranus is Titania
        print(key, [moon.name for moon in val.moon_list]) #sample output: Pluto ['Charon', 'Nix', 'Hydra', 'Kerberos', 'Styx']