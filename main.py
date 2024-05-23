import math

# Function to calculate the volume of a cylinder
def calculate_cylinder_volume(radius, height):
    return math.pi * radius**2 * height

# Main function
def main():
    # Input radius and height from the user
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))
    
    # Calculate the volume
    volume = calculate_cylinder_volume(radius, height)
    
    # Print the result
    print("The volume of the cylinder is:", volume)

# Calling the main function to execute the program
if __name__ == "__main__":
    main()