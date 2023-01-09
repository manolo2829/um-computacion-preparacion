from word import Word

class Phrase:

    def __init__(self):
        self.sequence = []

    # ESTA FUNCION INDICA QUE SE DEVUELVE AL LLABAR SOLO A PHRASE
    def __repr__(self):
        return f'{self.sequence}'

    def encode(self, sentence):
        words = sentence.split(' ')
        for each in words:
            word = Word()
            word.encode(each)
            self.sequence.append(word)
