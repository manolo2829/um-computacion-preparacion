

class Compress:

    def __init__(self):
        self.dictionary = {}
        self.compressed = []


    def compress(self, text):
        words = text.split(' ')
        words_auxiliar = []
        word_position = 0

        for each in  words:
            if not each in words_auxiliar:
                word_position += 1
                words_auxiliar.append(each)
                self.dictionary[each] = word_position
        
        for each in words:
            self.compressed.append(self.dictionary[each])

        return self.dictionary, self.compressed

    def uncompress(self, compressed, values):
        self.dictionary = values
        self.compressed = compressed

        for key, value in compressed:
            print(key, value)
