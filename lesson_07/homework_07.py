def multiplication_table(number):
    """Print the multiplication table for number while product is not greater than 25."""
    multiplier = 1

    while number * multiplier <= 25:
        result = number * multiplier
        print(f"{number}x{multiplier}={result}")
        multiplier += 1


def sum_two_numbers(first_number, second_number):
    """Return the sum of two numbers."""
    return first_number + second_number


def calculate_average(numbers):
    """Return the arithmetic mean of a non-empty list of numbers."""
    return sum(numbers) / len(numbers)


def reverse_string(text):
    """Return the given string in reverse order."""
    return text[::-1]


def find_longest_word(words):
    """Return the longest word from a non-empty list of words."""
    return max(words, key=len)


def find_substring(str1, str2):
    """Return the index of the first str2 occurrence in str1, or -1 if absent."""
    return str1.find(str2)


def has_more_than_ten_unique_symbols(text):
    """Return True if the text contains more than ten unique symbols."""
    return len(set(text)) > 10


def contains_letter_h(word):
    """Return True if the word contains the letter h in any case."""
    return "h" in word.lower()


def filter_strings(items):
    """Return only string items from the given list."""
    return [item for item in items if isinstance(item, str)]


def sum_even_numbers(numbers):
    """Return the sum of even numbers from the given list."""
    return sum(number for number in numbers if number % 2 == 0)


if __name__ == "__main__":
    multiplication_table(3)

    print(sum_two_numbers(5, 7))
    print(calculate_average([1, 2, 3, 4, 5]))
    print(reverse_string("Python"))
    print(find_longest_word(["cat", "elephant", "dog"]))

    print(find_substring("Hello, world!", "world"))
    print(find_substring("The quick brown fox jumps over the lazy dog", "cat"))

    print(has_more_than_ten_unique_symbols("Hello, Python!"))
    print(contains_letter_h("Hello"))
    print(filter_strings(["1", "2", 3, True, "False", 5, "6", 7, 8, "Python", 9, 0]))
    print(sum_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
