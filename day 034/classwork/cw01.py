def validate_hello(message):
    greetings = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    message = message.lower()
    return any(greeting in message for greeting in greetings)