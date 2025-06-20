def is_palindrome_stack(string: str) -> bool:
    stack = []
    string = string.lower()
    length = len(string)

    mid = length // 2

    for i in range(mid):
        stack.append(string[i])

    start = mid + 1 if length % 2 != 0 else mid

    for i in range(start, length):
        if stack.pop() != string[i]:
            return False

    return True

def is_palindrome_slicing(s: str) -> bool:
    s = s.lower()
    return s == s[::-1]

# if __name__ == "__main__":
    # string = input("Enter word: ")

    # if is_palindrome_stack(string):
    #     print(f"{string} adalah palindrome (dicek menggunakan stack)")
    # else:
    #     print(f"{string} adalah bukan palindrome (dicek menggunakan stack)")

    # if is_palindrome_slicing(string):
    #     print(f"{string} adalah palindrome (dicek menggunakan slicing)")
    # else:
    #     print(f"{string} adalah bukan palindrome (dicek menggunakan slicing)")

test_inputs = [
    "abba",         # (a + b)*
    "abcba",        # (a + b + c)*
    "ababab",       # (a + b)*
    "abccba",       # (a + b + c)*
    "a1b2c3b2a1",   # (a + b + c + 1 + 2 + 3)*
    "x9y8y9x",      # (x + y + 8 + 9)*
    "m0n1n0m",      # (m + n + 0 + 1)*
    "abc123",       # (a + b + c + 1 + 2 + 3)*
    "a1b22a1",      # (a + b + 1 + 2)*
    "a1b2c3d4",     # (a + b + c + d + 1 + 2 + 3 + 4)*
]

print("\nTest case results:")
for s in test_inputs:
    result_stack = is_palindrome_stack(s)
    result_slicing = is_palindrome_slicing(s)

    print(f"- {s}:")
    print(f"  Stack method   : {'Palindrome' if result_stack else 'Bukan Palindrome'}")
    print(f"  Slicing method : {'Palindrome' if result_slicing else 'Bukan Palindrome'}")
    print()
