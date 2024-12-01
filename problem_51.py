# Exercise 51  : Time Class 
# Create  a class in Python  called Time, which has members of type int such as hours, minutes and seconds. (Make them private)
# 1) A constructor should initialize this data to 0
# 2) Another constructor should initialize it to fixed values.
# 3) A member function should display it, in the format 17h 59min 59s.
# 4) Another function to return the data of each member name them getheurs, getMin and getSec
# 5) A member function should add two objects of type  Time  passed as arguments.

class Time:
    # Constructor with optional arguments for hours, minutes, and seconds
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    # Method to display time in the required format
    def display_time(self):
        print(f"Your current time is: {self.__hours}h {self.__minutes}m {self.__seconds}s")
    
    # Getter for hours
    def get_hours(self):
        return self.__hours
    
    # Getter for minutes
    def get_minutes(self):
        return self.__minutes
    
    # Getter for seconds
    def get_seconds(self):
        return self.__seconds
    
    # Method to add two Time objects
    def addtime(self, newtime):
        total_seconds = self.__seconds + newtime.get_seconds()
        total_minutes = self.__minutes + newtime.get_minutes()
        total_hours = self.__hours + newtime.get_hours()

        # Handling seconds overflow (more than 60 seconds)
        if total_seconds >= 60:
            total_minutes += total_seconds // 60  # Add the overflow minutes
            total_seconds = total_seconds % 60  # Keep the remaining seconds

        # Handling minutes overflow (more than 60 minutes)
        if total_minutes >= 60:
            total_hours += total_minutes // 60  # Add the overflow hours
            total_minutes = total_minutes % 60  # Keep the remaining minutes

        # Return a new Time object with the calculated hours, minutes, and seconds
        return Time(total_hours, total_minutes, total_seconds)

# Creating two Time objects
t1 = Time(2, 30, 25)  # 2 hours, 30 minutes, 25 seconds
t2 = Time(1, 45, 10)  # 1 hour, 45 minutes, 10 seconds

# Display the time for both objects
t1.display_time()
t2.display_time()

# Adding the two times and displaying the result
t1.addtime(t2).display_time()
