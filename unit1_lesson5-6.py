
# number_1 = int(input("Enter number 1: "))
# number_2 = int(input("Enter number 2: "))
#
# print(f"{number_1} + {number_2} = {number_1 + number_2}")

# print(f"{(n1 := int(input('Enter number 1: ')))} + {(n2 := int(input('Enter number 2: ')))} = {n1 + n2}")


# length = float(input("Enter the length: "))
# width = float(input("Enter the width: "))
#
# area = length * width
#
# print("Area of the rectangle:", area)

print(
    f"Area of the rectangle: "
    f"{(length := float(input('Enter the length: '))) * (width := float(input('Enter the width: ')))}"
)