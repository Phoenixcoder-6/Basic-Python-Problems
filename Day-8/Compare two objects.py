class TwoNum:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __gt__(self, other):
        return (self.num1 + self.num2) > (other.num1 + other.num2)

    def __str__(self):
        return f"TwoNum(num1={self.num1}, num2={self.num2})"

# Creating two objects
T1 = TwoNum(5, 10)
T2 = TwoNum(8, 6)

# Comparing the two objects
if T1 > T2:
    print(f"{T1} is greater than {T2}")
else:
    print(f"{T2} is greater than or equal to {T1}")
