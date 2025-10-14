class reverseString:
    def __init__(self , text):
        self.text = text
    def reverse_words(self):
        words = self.text.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)
sentence = "Python is very interesting! "
reverser = reverseString(sentence)
print("Original string : " , sentence)
print("Reversed String : " , reverser.reverse_words())