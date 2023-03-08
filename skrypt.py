def shopping(items, payment='card', shop='local shop'):
    result = ""
    result = result + "Idę na zakupy do %s.\n" % shop
    result = result + "Kupię następujące rzeczy:\n"
    for item in items:
        result = result + " - %s\n" % item
    result = result + "By zapłacić, używam %s." % payment
    return result

def greetings(name, surname):
    result2 = ""
    result2 = result2 + ("Witaj %s %s" %(name, surname)) + " !"
    return result2


if __name__ == "__main__":
    name_text = input("Podaj imię: ")
    surname_text = input("Podaj nazwisko:")
    greetings_result = greetings(name_text, surname_text)
    print(greetings_result)
    items_text = input("Podaj proszę produkty rozdzielone przecinkiem: ")
    items = items_text.split(',')
    shopping_result = shopping(items)
    print(shopping_result)
