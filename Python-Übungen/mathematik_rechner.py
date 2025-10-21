number1 = ""
number2 = ""

def get_calcMode():
    while True:
        calc_mode = input("What calculation do you want to do?\nA for Addition\nS for Subtraction\nM for Mulitply\nD for Division\nF for Facult\nE for Exponentation\nR for Modulo\n")
        if calc_mode == "A":
            number1 = input("Please enter first number: ")
            number2 = input("Please enter second number: ")
            addition(number1, number2)
        elif calc_mode== "S":
            number1 = input("Please enter first number: ")
            number2 = input("Please enter second number: ")
            subtraction(number1, number2)
        elif calc_mode == "M":
            number1 = input("Please enter first number: ")
            number2 = input("Please enter second number: ")
            multiply(number1, number2)
        elif calc_mode == "D":
            number1 = input("Please enter first number: ")
            number2 = input("Please enter second number: ")
            division(number1, number2)
        elif calc_mode == "F":
            number1 = input("Please enter the number: ")
            try:
                facult(int(number1))
            except:
                print("Wrong input! Please enter an number!")
        elif calc_mode == "P":
            number1 = input("Please enter the Base: ")
            number2 = input("Please enter the Exponend: ")
            exponentation(number1, number2)
        elif calc_mode == "R":
            number1 = input("Please enter first number: ")
            number2 = input("Please enter second number: ")
            modulo(number1, number2)
        elif calc_mode == "N":
            prime_number(number1)
        elif calc_mode == "V":
            number1 = input("Please enter first number: ")
            number2 = input("Please enter second number: ")
            average(number1, number2)
        else:
            print("Wrong input! Please enter A, S, M or D!")
        print("\n\nDo you want to calculate something else? ")
        x = input("Y for further calculation\n")
        if x != "Y":
            print("Good bye!")
            break
            
    
    
    
    
    

def addition(sum, addend):
    # try to transvert to int
    try:
        sum = int(sum)
    except ValueError:
        print("Please enter a number!")
    try:
        addend = int(addend)
    except ValueError:
        print("Please enter a number!")
    if addend < 0:
            subtraction(sum, addend*(-1)) #handle logic issue. If num2 is <0 for loop doesn't work anymore. So positiv scale gets past to subtraction()
    else:    
        i = 1
        #vget sum by counting up +1
        while i <= addend:
            sum+=1
            i+=1
        print("Result: " + str(sum))
    

def subtraction(difference, subtrahend):
    # try to transvert to int
    try:
        difference = int(difference)
    except ValueError:
        print("Please enter a number!")
    try:
        subtrahend = int(subtrahend)
    except ValueError:
        print("Please enter a number!")
    if subtrahend < 0:
            addition(difference, subtrahend*(-1)) #handle logic issue. If num2 is <0 for loop doesn't work anymore. So positiv scale gets past to subtraction()
    else:    
        i = 1
        #vget sum by counting down by -1
        while i <= subtrahend:
            difference-=1
            i+=1
        print("Result: " +str(difference))
    

def multiply(factor1, factor2):
    try:
        factor1 = float(factor1)
        factor2 = float(factor2)
    except ValueError:
        print("Please enter valid numbers!")
        return

    # Count decimal places in factor2
    fact2check = str(factor2)
    if "." in fact2check:
        dec_place_count = len(fact2check.split(".")[1])
    else:
        dec_place_count = 0

    try:
        mult = 10 ** dec_place_count
    except OverflowError:
        print("Please enter smaller numbers")
        return

    # Simulate multiplication using repeated addition
    int_factor2 = int(factor2 * mult)
    produc = 0
    for _ in range(int_factor2):
        produc += factor1

    # Adjust for decimal places
    produc = produc / mult

    # Handle zero case
    if factor1 == 0 or factor2 == 0:
        produc = 0

    print("Result " + str(produc))


def division(dividend, divisor):
    correct = False
    about_ = False
    quotient = 0

    try:
        dividend = float(dividend)
    except ValueError:
        print("Please enter a number!")
        return
    try:
        divisor = float(divisor)
    except ValueError:
        print("Please enter a number!")
        return

    # tolerance for "close enough"
    tolerance = 0.001  

    while not correct:
        if abs(quotient * divisor - dividend) < 1e-9:
            correct = True
        elif abs(quotient * divisor - dividend) < tolerance:
            about_ = True
            correct = True
        else:
            quotient += 0.001   # finer step

    print("Result: ")
    if about_:
        print("about ", end="")

    # round to 3 decimal places
    print(round(quotient, 3))
    
def facult(number1):
    if type(number1) == int and number1 >= 0:
        result = 1
        i = 1
        while i <= number1:
            result *= i
            i += 1
        print("The factorial of " + str(number1) + " is " + str(result))
    else:
        print("Wrong input")
        
        
def exp_series(x, terms=500000):
    """Approximation von e^x über Taylorreihe"""
    result = 1.0
    term = 1.0
    for n in range(1, terms):
        term *= x / n
        result += term
    return result

def ln_series(x, terms=500000):
    """Approximation von ln(x) über Reihenentwicklung"""
    if x <= 0:
        raise ValueError("ln nur für x > 0 definiert")

    k = 0
    # bringe x in den Bereich (0.5, 2]
    while x > 2:
        x /= 2
        k += 1
    while x < 0.5:
        x *= 2
        k -= 1

    y = x - 1
    result = 0.0
    sign = 1
    for n in range(1, terms):
        result += sign * (y**n) / n
        sign *= -1
    return result + k * 0.6931471805599453  # ln(2)

def exponentation(base, exponend, terms=500000):
    """Berechnet base^exponend für reelle Exponenten im Loop-Style"""
    result = 1.0
    try:
        base = float(base)
    except ValueError:
        print("Please enter a number for base!")
        return None

    try:
        exponend = float(exponend)
    except ValueError:
        print("Please enter a number for exponend!")
        return None

    if base <= 0:
        print("Base must be > 0 for real exponents!")
        return None

    # Definition: a^b = exp(b * ln(a))
    ln_base = ln_series(base, terms)
    result = exp_series(exponend * ln_base, terms)

    print(round(result, 3))
    return result

def modulo(dividend, divisor):
    result = dividend%divisor
  
    return result

def prime_number(number1):
    not_prime_num = False 
    try:
        number1 = int(number1)
    except ValueError:
        print("Please enter a number for base!")
        return None
    x = number1
    i = 2
    while not_prime_num == False:
        x = x/i
        if type(x) == float:
            i+=1
            continue
        not_prime_num = (int(x)*i==number1)
        if not_prime_num == True:
            break
        i+=1
        if x<1:
            break
        
    if not_prime_num == True:
        print(str(number1) + "is not a prime number")        
    else: print(str(number1) + "is a prime number")   

def average(number1, number2):
    try:
        number1 = int(number1)
    except ValueError:
        print("Please enter a number!")
        return None
    try:
        number2 = int(number2)
    except ValueError:
        print("Please enter a number!")
        return None
    result = number2+number1
    result = result/2
    return result
    
        
get_calcMode()


