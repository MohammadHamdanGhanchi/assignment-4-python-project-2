# Constant for Mars' gravity
MARS_MULTIPLE = 0.378

def main():
    # Prompt the user for their weight on Earth
    earth_weight_str = input('Enter a weight on Earth: ')

    # Convert the input to a float (numeric form) for calculation
    earth_weight = float(earth_weight_str)

    # Calculate the weight on Mars
    mars_weight = earth_weight * MARS_MULTIPLE

    # Round the result to 2 decimal places
    rounded_mars_weight = round(mars_weight, 2)

    # Print the result
    print('The equivalent weight on Mars: ' + str(rounded_mars_weight))

if __name__ == '__main__':
    main()
