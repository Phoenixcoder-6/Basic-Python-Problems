class Time:
    def gettime(self):
        self.hours = int(input("Enter hours: "))
        self.minutes = int(input("Enter minutes: "))
        self.seconds = int(input("Enter seconds: "))

    def putresult(self):
        print(f"The time conversion is: {self.days} days, {self.hours} hours, {self.minutes} minutes, and {self.seconds} seconds")

    def __add__(self, other):
        total_hours = self.hours + other.hours
        total_minutes = self.minutes + other.minutes
        total_seconds = self.seconds + other.seconds

        # Adjust for overflow
        total_minutes += total_seconds // 60
        total_seconds %= 60

        total_hours += total_minutes // 60
        total_minutes %= 60

        total_days = total_hours // 24
        total_hours %= 24

        # Create a new Time object for the result
        result = Time()
        result.hours = total_hours
        result.minutes = total_minutes
        result.seconds = total_seconds
        result.days = total_days

        return result

# Create two time objects
t1 = Time()
print("Enter value for time object 1:")
t1.gettime()

t2 = Time()
print("Enter value for time object 2:")
t2.gettime()

# Add the two time objects
t3 = t1 + t2

# Display the result
t3.putresult()

               
               