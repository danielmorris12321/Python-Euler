def Fibonacci(terms):
    if terms < 1:
        print("Incorrect limit")
    elif terms == 1:
        return(0)
    elif terms == 2:
        return(1)
    else:
        return (Fibonacci(terms - 1) + Fibonacci(terms - 2))
    
print(Fibonacci(9))
