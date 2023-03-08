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
            else:
                logging.info("Mama mawiała: Nie dziel przez zero cholero!")
                exit(1)
            logging.info("Dzielę", number1, " przez ", number2, " Wynik to: ", result)
        else:
            exit(1)

#calculation("1",1,1)


if __name__ == "__main__":
    type = input("Podaj rodzaj operacji: 1-dodawanie, 2-odejmowanie, 3-mnozenie, 4-dzielenie: ")
    number1 = input("Podaj pierwszą liczbę działania: ")
    number1 = float(number1)
    number2 = input("Podaj drugą liczbę działania: ")
    number2 = float(number2)
    type_no = ["1", "2", "3", "4"]
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
        else:
            exit(1)

    #logging.debug("The program was called with this parameter - action type %s" % sys.argv[1])
    #logging.debug("The program was called with these parameters - numbers %s" % sys.argv[1:])
    #type_no = str(sys.argv[1])
    #number1 = int(sys.argv[1])
    #number2 = int(sys.argv[2])

 

