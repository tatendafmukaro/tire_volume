import math
"""Prove that you can write a simple Python program 
that gets input from a user, performs arithmetic, 
and displays output for the user to see."""

first_number = float(input("Enter the width of the tire in mm (ex 205): "))
second_number = float(input("Enter the aspect ratio of the tire (ex 60): "))
third_number = float(input("Enter the diameter of the wheel in inches (ex 15): "))

"""v is the volume in milliliters,
π is the constant PI, the ratio of the circumference divided by the diameter of a circle (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches."""


w = first_number
a = second_number
d = third_number
numerator = math.pi * w**2 * a * (w * a + 2540 * d)
denominator = 10000000
v  = numerator / denominator

print (f"{v: .1f}")