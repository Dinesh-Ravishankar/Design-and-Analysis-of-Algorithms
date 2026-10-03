def is_palindrome(string):
    return string == string[::-1]

n = int(input("Enter number of strings: "))

for i in range(n):
    string = input("Enter string: ")

    if is_palindrome(string):
        print("First palindromic string:", string)
        break
else:
    print("No palindromic string found.")