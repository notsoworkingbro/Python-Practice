#Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Input Format

# A single line containing a positive integer, .

# Constraints
n = 2

if(n % 2):
    print("Weird")

else:
    if(2 <= n <= 5):
        print("Not Weird")
    
    elif (6 <= n <= 20):
        print("Weird")

    elif (n > 20):
        print("Not Weird")

