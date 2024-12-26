def count_vowels(s):
    # Your code here
    vowels_list = [character for character in s if character in ("a", "e", "i", "o", "u")]
    return len(vowels_list)

# Test
print(count_vowels("hello world"))  # Output: 3
