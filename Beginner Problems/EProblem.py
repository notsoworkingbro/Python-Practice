# Say, there was point where I want to center my print like this:

# O============O
# |    Cool    |
# O============O

# Without changing the size of the border, 
# give me a dynamic code where it centers the 
# user-inputted word inside.

string = input("Enter your value: ")

print("O" + "=" * (12) + "O")
print("|" + " "*((12-len(string))//2) + string + " "*((12-len(string))//2) + "|")
print("O" + "=" * (12) + "O")