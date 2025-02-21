# Strings are texts. With that in mind, we can also use those as a password. 
# Let's make something simple. How about, getting the user to type exactly 12 characters? While we're at it, 
# swap the first half into the second half. This way, we have a basic encryption as well. Limit your code to at most 4 lines.

# ea = []
# while (str_in := input()) and len(str_in) != 12: pass 
# ea.extend([''.join(list(str_in)[6:12]), ''.join(list(str_in)[0:6])])
# aaa = ''.join(ea)

while (str_in := input()) and len(str_in) != 12: pass 
print(''.join([str_in[6:12], str_in[0:6]]))