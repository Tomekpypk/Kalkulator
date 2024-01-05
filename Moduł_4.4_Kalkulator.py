import logging
logging.basicConfig(level=logging.INFO)

def calculator():
    print("Podaj działanie zgodnie z przypisanym numerem:")
    print("1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
    operation = int(input())
       
    x = float(input("Podaj liczbę X: "))
    y = float(input("Podaj liczbę Y: "))

    
    if operation == 1:
        logging.info(f"Dodaję {x} i {y}")
        result = x + y
    elif operation == 2:
        logging.info(f"Odejmuję {x} od {y}")
        result = x - y
    elif operation == 3:
        logging.info(f"Mnożę {x} i {y}")
        result = x * y
    elif operation == 4:
        logging.info(f"Dzielę {x} przez {y}")
        if y != 0:
            result = x / y
        else:
            logging.error("Nie można dzielić przez zero!")
            return
        

    
    print("Wynik to:", result)


calculator()
