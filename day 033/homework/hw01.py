def manual_split(text, separator=' '):
    words = []
    current = ''

    for letter in text:
        if letter == separator:
            if current != '':
                words.append(current)
                current = ''
        else:
            current += letter

    if current != '':
        words.append(current)

    return words