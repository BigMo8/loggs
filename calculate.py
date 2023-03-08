import sys
import logging
logging.basicConfig(level=logging.DEBUG)

def calculation(type, number1, number2):
    type_no = ["1", "2", "3", "4"]
    for type_no in type:
        if type_no == "1":
            result = round(number1 + number2, 2)
            logging.info("Dodaję", number1, " i ", number2, " Wynik to: ", result)
        if type_no == "2":
            result = round(number1 - number2, 2)
            logging.info("Odemuję od liczby", number1, "liczbę", number2), '\n', logging.info(" Wynik to: ", result)
        if type_no == "3":
            result = round(number1 * number2, 2)
            logging.info("Mnożę", number1, " przez ", number2, " Wynik to: ", result)
        if type_no == "4":
            if number2 != 0:
                result = round(number1 / number2, 2)
                logging.info("Dzielę", number1, " przez ", number2, " Wynik to: ", result)
            else:
                logging.info("Mama mawiała: Nie dziel przez zero cholero!")
                exit(1)
        else:    
            exit(1)

#calculation("1",1,1) - spraqdzenie funkcji


if __name__ == "__main__":
    type = input("Podaj rodzaj operacji: 1-dodawanie, 2-odejmowanie, 3-mnozenie, 4-dzielenie: ")
    logging.info("The programme is calling with first parameter %s" %type)
    number1 = input("Podaj pierwszą liczbę działania: ")
    number1 = float(sys.argv[1])
    logging.info("First variable given: %s" %number1)
    number2 = input("Podaj drugą liczbę działania: ")
    number2 = float(sys.argv[2])
    logging.info("Second variable given: %s" %number1)
    type_no = ["1", "2", "3", "4"]
    type = str(sys.argv[3])
    logging.info("Podano rodzaj operacji: %s" %type + "  gdzie 1-dodawanie, 2-odejmowanie, 3-mnozenie, 4-dzielenie")
    calculation(type = 'sys.argv[3]', number1 = 'sys.argv[1]', number2= 'sys.argv[2]')
    for type_no in type:
        if type_no == "1":
            result = round(number1 + number2, 2)
            print("Dodaję ", number1, " i ", number2, "Wynik to: ", result)
        if type_no == "2":
            result = round(number1 - number2, 2)
            print("Odemuję od liczby ", number1, "liczbę ", number2, "Wynik to: ", result)
        if type_no == "3":
            result = round(number1 * number2, 2)
            print("Mnożę ", number1, " przez ", number2, "Wynik to: ", result)
        if type_no == "4":
            if number2 != 0:
                result = round(number1 / number2, 2)
                print("Dzielęc", number1, " przez ", number2, "Wynik to: ", result)
            else:
                print("Mama mawiała: Nie dziel przez zero cholero!")
                logging.info("Second variable given is zero")
                exit(1)
        else:
            exit(1)



 

