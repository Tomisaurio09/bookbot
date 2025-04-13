def count_words(book_text):
    words = book_text.split()
    return len(words)

def count_characters(book_text):
    texts = book_text.lower()
    diccionario = {}
    for characther in texts:
        if characther in diccionario:
            diccionario[characther] += 1
        else:
            diccionario[characther] = 1
    return diccionario

def sort_on(dict):
    return dict["count"]

def sort_dictionary(dictionary):
    dictionary_list = []
    for key,value in dictionary.items():
        dictionaries = {"characther": key, "count": value}
        dictionary_list.append(dictionaries)
    dictionary_list.sort(reverse=True, key=sort_on)

    return dictionary_list
