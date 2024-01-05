def dodawanie(x, y):
    return x + y

def odejmowanie(x, y):
    return x - y

def mnożenie(x, y):
    return x * y

def dzielenie(x, y):
    if y != 0:  
        return x / y
    else:
        print("Nigdy cholero nie dziel przez ZERO, znaczy Ziobro")
        return None

def calculator():  
    print("Wybierz operację poprzez numer:")
    operation = int(input("1. dodawanie, 2. odejmowanie, 3. mnożenie, 4. dzielenie: "))
    
    x = float(input("Podaj liczbę x: "))
    #if x != float:
        #return("liczbę kurła")#innym razem to zrobię  
    y = float(input("Podaj liczbę y: ")) 
    #if x != float:
        #return liczbę kurła 

    if operation == 1:
        result = dodawanie(x, y)
        print(f"Dodaję {x} do {y}")
        print("Wynik to:", result)
    elif operation == 2:
        result = odejmowanie(x, y)
        print(f"Odejmuję {y} od {x}")
        print("Wynik to:", result)
    elif operation == 3:
        result = mnożenie(x, y)
        print(f"Mnożę {x} przez {y}")
        print("Wynik to:", result)
    elif operation == 4:
        result = dzielenie(x, y)
        if result is not None:
            print(f"Dzielę {x} przez {y}")
            print("Wynik to:", result)
    else:
        print("Niepoprawna operacja")

calculator()