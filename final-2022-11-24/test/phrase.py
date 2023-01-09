from word import Word

class Phrase:

    def __init__(self):
        self.sequence = []

    # ESTA FUNCION INDICA QUE SE DEVUELVE AL LLABAR SOLO A PHRASE
    def __repr__(self):
        return self.sequence

    def encode(self, sentence):
        words = sentence.split(' ')
        for each in words:
            word = Word()
            word.decode(list(each))
            self.sequence.append(word)
        self.sequence = f'{self.sequence}'
        self.sequence = self.sequence.replace('{','[').replace('}',']').replace("'","")


        
