""" Positional Parameters
They are like optional parameters
And can be assigned a default value, if no value is provided from outside
 """


def sum_nums(n1=0, n2=0):  # El valor por defecto en ambos es 0
    """
    Get sum of two numbers
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2


sum1 = sum_nums(2, 8)
sum2 = sum_nums(3)
sum3 = sum_nums(n2=23, n1=2)  # Se puede cambiar el orden si los ponemos así

print(sum1, sum2, sum3)
