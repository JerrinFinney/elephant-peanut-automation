elephant_position = 5
peanut_position = 5

print("Elephant starts at:", elephant_position)
print("Peanut is located at:", peanut_position)

while elephant_position != peanut_position:

    if elephant_position < peanut_position:
        elephant_position += 1
        print("The elephant moves right!", elephant_position)

    else:
        elephant_position -= 1
        print("The elephant moves left!", elephant_position)

print("Peanut Found! Yummy!")