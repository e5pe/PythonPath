""" 
and

or

not 
"""

and_output1 = (10 == 10) and (10 > 9)
and_output2 = (10 == 10) and (10 <= 9)
print(and_output1, and_output2)


or_output1 = (10 == 10) or (10 > 9)
or_output2 = (10 == 10) or (10 <= 9)
print(or_output1, or_output2)

not_true = not (10 == 10) # not true is false
not_false = not (10 > 10) # not false is true
print(not_true, not_false)