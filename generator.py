import random

class Generate:
    def __init__(self, length):
        self.length = length
        self.answer = ""
        # self.answer = answer
        # self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.numbers = "0123456789"
        self.letters_numbers = self.letters + self.numbers

    def word_maker(self):
        for i in range(0, self.length):
            self.answer += random.choice(self.letters)
        return self.answer

    def number_maker(self):
        for i in range(0, self.length):
            self.answer += random.choice(self.numbers)
        return self.answer

    def letter_number_maker(self):
        for i in range(0, self.length):
            self.answer += random.choice(self.letters_numbers)
        return self.answer

# print(Generate(4).word_maker())

