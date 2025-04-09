def main():
    # Dictionary of planets with their corresponding gravity percentages relative to Earth
    planet_gravity = {
        "Mercury": 37.6,
        "Venus": 88.9,
        "Mars": 37.8,
        "Jupiter": 236.0,
        "Saturn": 108.1,
        "Uranus": 81.5,
        "Neptune": 114.0
    }
    
    # Milestone 1: Input Earth's      
    earth_weight = float(input("Enter a weight on Earth: "))
            
    # Milestone 2: Input the name of the planet
    planet = input("Enter a planet: ")

    # Check if the entered planet is in the dictionary
    if planet in planet_gravity:
        # Calculate the weight on the selected planet
        planet_weight = earth_weight * (planet_gravity[planet] / 100)
        # Print the result, rounded to 2 decimal places
        print(f"The equivalent weight on {planet}: {round(planet_weight, 2)}")
    else:
        print("Sorry, that planet is not recognized in the system.")

if __name__ == "__main__":
    main()
