#!/usr/bin/env python3

from fractions import Fraction
import math

degree = int(input("What is the degree of the equation (power of the first x)? "))

# The frequency of synthetic divison needed is determined from what is needed to make it down to x².  
frequencyOfSyntheticDivison = degree - 2

amountOfTerms = degree +  1 


# Dictionary linking numeric value of iteration of for loop (numeric value of term in the formula)  to a variable that could be formulaically understood by the end user

numericToAlphabetic = {

             
         "0":   "A" ,
         "1":   "B" ,
         "2":   "C" ,
         "3":   "D" ,
         "4":   "E" ,
         "5":   "F" ,
         "6":   "G" ,
         "7":   "H" ,
         "8":   "I" ,
         "9":   "J" ,
         "10":  "K" ,
         "11":  "L" ,
         "12":  "M" ,     
         "13":  "N" ,     
         "14":  "O" ,
         "15":  "P" ,
         "16":  "Q" ,   
         "17":  "R" ,     
         "18":  "S" ,     
         "19":  "T" ,     
         "20":  "U" ,     
         "21":  "V" ,     
         "22":  "W" ,     
         "23":  "X" ,    
         "24":  "Y" ,    
         "25":  "Z"     
 }

terms = []

for i in range(amountOfTerms):
    
    numInput= int(input(f"What is the value for variable {numericToAlphabetic[str(i)]}? "))
    terms.append(numInput)

p = (terms[-1])
q = (terms[ 0])


print(f'Your p value is {p} and your q value is {q}')
print("Rational root therom allows us to deduct possible roots through ± factors of p / factors of q")




def Factors(num):
    factor_list = []
    if num > 0:
        for i in range (1, num + 1):
            if num % i == 0:
                factor_list.append(i)
    # Uses x - > 0 rather then 1 - > x  if neg
    if num < 0:
        for i in range (num , 0):
             if num % i == 0:
                factor_list.append(i)

    return factor_list


print(Factors(p) , "are the factors of p")

print(Factors(q) , "are the factors of q")

print(f'This means our our possible rational roots are ± {Factors(p)} / {Factors(q)}')

def rational_roots():
    root_list = []
    for i in Factors(p):
        for v in Factors(q):
            root_list.append(i / v)
    return root_list



print(f'±{rational_roots()} are your possible rational roots divided')

print("Now I'll do some synthetic divison to find possible roots")

#def synthetic_divison_quartic():
#    for x in rational_roots():
#        if  x * (x * (x * (x * terms[0]  + terms[1]) + terms[2] ) + terms[3]) + terms[4] == 0:
#            global cubic_a
#            cubic_a = terms[0]
#            global cubic_b
#            cubic_b = x * terms[0] + terms[1]
#            global cubic_c
#            cubic_c = x * cubic_b + terms[3]
#            global cubic_d
#            cubic_d = x * cubic_c + terms[4]
#            global cubic_list
#            cubic_terms = [cubic_a, cubic_b, cubic_c, cubic_d]
#            print(f'{x} is a root!')
#            print(f'Now I am  with the cubic {cubic_a}x³ + {cubic_b}x² + {cubic_c}x + {cubic_d}')

def is_square(n):
    sqrt = math.sqrt(n)
    return (sqrt - int(sqrt)) == 0

def synthetic_divison_cubic():
    #if degree > 4:
    #   terms = cubic_terms
    global root_list
    root_list = []
    for x in rational_roots():
        if x * (x * (x * terms[0]  + terms[1]) + terms[2] ) + terms[3] == 0:
            global quadratic_a
            global quadratic_b
            global quadratic_c
            quadratic_a = terms[0]
            quadratic_b = x * terms[0] + terms[1]
            quadratic_c = x + terms[3]
            print(f'{x} is a root!')
            root_list.append(x)
    print(f"The root / roots found through synthetic divison were {root_list}")
    print(f'We are left with the quadratic {quadratic_a}x² + {quadratic_b}x + {quadratic_c}')
 
def quadraticFormula():
    print(f'To find the final factor/factors quadratic formula will be used.')
    print(f'(-{quadratic_b} ± √{quadratic_b}² - 4({quadratic_a})({quadratic_c})) / 2({quadratic_a})')
    print(format)
    discriminant = (quadratic_b ** 2) - (4 * quadratic_a * quadratic_c)
    if discriminant < 0:
        root_list.append(f"{quadratic_b * -1} ± i√{discriminant * -1} / {quadratic_a *2}")
    
    elif is_square(discriminant) == True:
        positive_solution_set = ((quadratic_b * -1) + math.sqrt(discriminant)) / (2*a)
        negative_solution_set = ((quadratic_b * -1) - math.sqrt(discriminant)) / (2*a)
        root_list.append(positive_solution_set)
        root_list.append(negative_solution_set)
    else:
        print("discriminant isn't a perfect square")
        root_list.append(f'(-{quadratic_b} ± √{quadratic_b}² - 4({quadratic_a})({quadratic_c})) / 2({quadratic_a})')
    print(root_list, "are you roots")

#synthetic_divison_quartic()
synthetic_divison_cubic()
quadraticFormula()
