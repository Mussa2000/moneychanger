import inflect

def number_to_words_ordinal(number):
    if not isinstance(number, int) or number < 1 or number > 50:
        return "Number out of range or not an integer."

    p = inflect.engine()
    return p.ordinal(number)

# Example usage:
for i in range(1, 11):
    print(f"{i}: {number_to_words_ordinal(i)}")

