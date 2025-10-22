class IntegerToRoman:
    def __init__(self):
        # Define the mapping of Roman numerals to integer values
        self.value_map = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]
    
    def convert(self, number):
        """Convert integer to Roman numeral."""
        if not (0 < number < 4000):
            return "Number out of range (1–3999)"
        
        roman_numeral = ""
        for value, symbol in self.value_map:
            while number >= value:
                roman_numeral += symbol
                number -= value
        return roman_numeral


# Example usage
if __name__ == "__main__":
    converter = IntegerToRoman()
    num = int(input("Enter an integer (1–3999): "))
    print(f"Roman numeral: {converter.convert(num)}")