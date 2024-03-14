import math  # Import math module for mathematical functions
from fractions import Fraction  # Import Fraction from fractions module for fraction operations

# Function to calculate the midpoint between two points
def get_midpoint(x1, y1, x2, y2):
    midpoint_x = (x1 + x2) / 2  # Calculate midpoint x-coordinate
    midpoint_y = (y1 + y2) / 2  # Calculate midpoint y-coordinate
    return midpoint_x, midpoint_y  # Return both x and y coordinates of the midpoint

# Function to calculate the distance between two points
def get_distance(x2, x1, y2, y1):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)  # Use Pythagorean theorem to calculate distance
    return distance  # Return the calculated distance

# Function to display the midpoint in both decimal and fraction format
def display_midpoint(x1, x2, y1, y2):
    midpoint_x, midpoint_y = get_midpoint(x1, y1, x2, y2)  # Get midpoint coordinates
    # Convert midpoint coordinates to fractions and limit denominator
    midpoint_x_fraction = Fraction(int(x1 + x2), 2).limit_denominator()
    midpoint_y_fraction = Fraction(int(y1 + y2), 2).limit_denominator()
    # Print midpoint in decimal and fraction format
    print(f"The midpoint is: ({midpoint_x}, {midpoint_y})")
    print(f"The midpoint in fraction format is: ({midpoint_x_fraction}, {midpoint_y_fraction})")

# Function to display the distance between two points
def display_distance(x2, x1, y2, y1):
    distance = get_distance(x2, x1, y2, y1)  # Calculate distance between two points
    print(f"The distance between the two points is: {distance}")  # Print the calculated distance

# Main program execution starts here
choice = input("Do you want to find the midpoint or distance? (1 for midpoint/2 for distance): ")

# Conditional block to execute based on user choice
if choice == "1":
    # Prompt user for coordinates of the two points
    x1 = float(input("Enter x1: "))
    x2 = float(input("Enter x2: "))
    y1 = float(input("Enter y1: "))
    y2 = float(input("Enter y2: "))
    display_midpoint(x1, x2, y1, y2)  # Call function to display midpoint
elif choice == "2":
    # Prompt user for coordinates of the two points
    x2 = float(input("Enter x2: "))
    x1 = float(input("Enter x1: "))
    y2 = float(input("Enter y2: "))
    y1 = float(input("Enter y1: "))
    display_distance(x2, x1, y2, y1)  # Call function to display distance

