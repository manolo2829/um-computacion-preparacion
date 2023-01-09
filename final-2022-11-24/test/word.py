

class Word:
    def __init__(self):
        self.word = []

    # ESTA FUNCION INDICA QUE SE DEVUELVE AL LLABAR SOLO A PHRASE
    def __repr__(self):
        return f'{self.word}'


    def decode(self, word):
        letter_auxiliar = {}
        letter_position = 0
        for letter in word:
            letter_position += 1
            if not letter in letter_auxiliar:
                letter_auxiliar[letter] = [letter_position]
            else:
                letter_register = letter_auxiliar[letter]
                letter_register.append(letter_position)
                letter_auxiliar[letter] = letter_register

        self.word = letter_auxiliar