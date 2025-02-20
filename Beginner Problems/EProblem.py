# Say, there was point where I want to center my print like this:

# O============O
# |    Cool    |
# O============O

# Without changing the size of the border, 
# give me a dynamic code where it centers the 
# user-inputted word inside.

string = input("Enter your value: ")
print(string)

n = count(string)

print("O" + "=" * (12) + "O")
print("|" + " "*(n) + string + " "*(n) + "|")
print("O" + "=" * (12) + "O")

# for i in range(0, n):
#         print(" " * (0 + n - i - 1) + "*" * (2 * i + 1))cool
#     print(" " * (n-1) + "*")