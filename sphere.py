# Make a program that calculates and shows the volume of a sphere and the value of its radius (R) is given. The formula for calculating the volume is: (4/3) * pi * R3. Consider (assign) to pi the value 3.14159.
# Tip: When using the formula, try to use (4 / 3.0) or (4.0 / 3), because some languages (among them C ++), assume that the result of the division between two integers is another integer.

n = 3.14159

R = float (input ())

VOLUME = (4/3.0) * n * R**3

print ('VOLUME = {:.3f}'.format (VOLUME))