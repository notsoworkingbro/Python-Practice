n = 5
def tree(n):
    for i in range(0, n):
        print(" " * (0 + n - i - 1) + "*" * (2 * i + 1))
    print(" " * (n-1) + "*")

# short line but still the same
def tree1(n):
    [print(" " * (n-i-1) + "*" * (2*i+1)) for i in range(0, n)]
    print(" " * (n-1) + "*")

tree(n)
tree1(n)