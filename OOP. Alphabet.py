import string

class Alphabet:
    def __init__(self, language, letters):
        self.lang = language
        self.letters = list(letters)

    def print(self):
        print(self.letters)

    def letters_num(self):
        len(self.letters)


class engAlphabet(Alphabet):
    __letters_num = 26

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    # Проверяем, относится ли буква к английскому алфавиту
    def is_en_letter(self, letter):
        if letter.upper() in self.letters:
            return True
        return False

    # Возвращаем количество букв в алфавите
    def letters_num(self):
        return engAlphabet.__letters_num

    # Печатаем пример текста на английском языке
    @staticmethod
    def example():
        print("English Example:\nDon't judge a book by it's cover.")


if __name__ == '__main__':
    eng_alphabet = engAlphabet()
    eng_alphabet.print()
    print(eng_alphabet.letters_num())
    print(eng_alphabet.is_en_letter('F'))
    print(eng_alphabet.is_en_letter('Щ'))
    engAlphabet.example()
        
