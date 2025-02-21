num = 322.12299

# printing num without decimal without using int

def  test(num):
    # create empty array of stringn
    num_str_arr = []

    # turn num into string
    num_str = str(num)

    # seperate num using split() '.'
    num_str_arr = num_str.split('.')

    # pop first item from splitted array of string
    num_str_arr.pop()

    # use eval to turn 
    new_num = eval(num_str_arr[0])
    print(new_num)

def test1(num):

    # same without empty array of string
    num_str = str(num)
    new_str, leftover = num_str.split('.')
    new_int = eval(new_str)
    print(new_int)

# still okay
def test2(num):

    num_str = str(num)

    print(round(float(num_str) // 1))
    print(round(num))
    print(num//1)

test(num)
test1(num)
test2(num)