# line by line debugging

# rubber duck debugging

# debugging by walking away

# debugging with print
# e.g

def titlize(sentence):
    words = sentence.split()
    # print(words)
    new_words = []

    for word in words:
        # print(word)
        if len(word) > 2:
            # print(word)
            word = word.capitalize()
            # print(word)
        new_words.append(word)
        
    return ' '.join(new_words)

title = 'hello world of programming'
print(titlize(title))
# titlize(title)