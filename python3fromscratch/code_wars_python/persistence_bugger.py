def multiply_digits(number):
    dev = None
    if len(str(number)) >= 1:
        dev = int(str(number)[0])
        for digit in str(number)[1:]:
            dev *= int(digit)
    return dev

def persistence(n):
    # returns its multiplicative persistence,  the number of times you must multiply the digits in num
    # until you reach a single digit
    num_times = 0
    while len(str(n)) > 1:
        n = multiply_digits(n)
        num_times+=1
    return num_times
real = persistence(39)
print(real)
print("peristence test 1 is ",real == 3)

 