from compress import Compress

if __name__ == '__main__':
    file = open('tdd.txt')
    text_1 = file.read()
    compress = Compress()
    print(compress.compress(text_1))
    print([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 17, 24, 25, 26, 14, 27, 28, 29, 30, 31, 7, 32, 33, 24, 25, 34, 35, 11, 36, 37, 38, 39, 40, 41, 25, 42, 43, 42, 44, 42, 45, 46, 10, 47, 48, 16, 24, 49, 50, 51, 52, 53, 54, 55, 16, 56, 1, 57, 58, 59,
                             12, 60, 61, 62, 42, 63, 64, 10, 65, 66, 67, 16, 28, 68, 46, 69, 70, 71, 72, 73, 41, 74, 75, 76, 77, 16, 35, 78, 79, 80, 16, 81, 15, 82, 16, 81, 83, 36, 84, 85, 46, 86, 87, 88, 89, 46, 90, 91, 61, 92, 93, 94, 95, 96, 97, 14, 98, 99, 41, 100, 53, 82, 10, 101, 102, 103, 53, 104, 46, 105, 106, 1, 16, 107])