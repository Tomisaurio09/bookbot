def main():
    path = "/home/tomisaurio/workspace/github.com/Tomisaurio09/bookbot/books/frankenstein.txt"
    
    text = get_book(path)
    
    num_words = counting_words(text)
    
    chars_dict = counting_characters(text)
    
    chars_sorted = sort(chars_dict)

    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted:
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def counting_words(file):
    return len(file.split())

def sort_on(d):
    return d["num"]

def sort(diccionario):
    lista = [{"char": ch, "num": count} for ch, count in diccionario.items()]
    
    lista.sort(reverse=True, key=sort_on)
    
    return lista

def counting_characters(file):
    diccionario = {}
    for letra in file:
        if letra.isalpha():  
            letra = letra.lower()  
            diccionario[letra] = diccionario.get(letra, 0) + 1
    return diccionario

def get_book(path):
    
    with open(path) as f:
        return f.read()


main()
