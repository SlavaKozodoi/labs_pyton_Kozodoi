#1
def mysplit(string):
    list_split = []
    word = ""
    for char in string:
        if char == " ":
            if word:
                list_split.append(word)
            word = ""
        else:
            word += char

    if word:
        list_split.append(word)

    return list_split


# Тести
print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))


#2
number_dict = {
    '1': ('  #', '  #', '  #', '  #', '  #'),
    '2': ('###', '  #', '###', '#  ', '###'),
    '3': ('###', '  #', '###', '  #', '###'),
    '4': ('# #', '# #', '###', '  #', '  #'),
    '5': ('###', '#  ', '###', '  #', '###'),
    '6': ('###', '#  ', '###', '# #', '###'),
    '7': ('###', '  #', '  #', '  #', '  #'),
    '8': ('###', '# #', '###', '# #', '###'),
    '9': ('###', '# #', '###', '  #', '###'),
    '0': ('###', '# #', '# #', '# #', '###')
}

def display_number(num):
    if num < 0:
        print("Число має бути невід'ємним.")
        return

    num_str = str(num)

    for level in range(5):
        for symbol in num_str:
            print(number_dict[symbol][level], end=' ')
        print()

display_number(123)



#3
text = input("Enter your message: ")
cipher = ''

for char in text:
    if not char.isalpha():
        continue

    char = char.upper()

    code = ord(char) + 1

    if code > ord('Z'):
        code = ord('A')

    cipher += chr(code)

print("Encrypted message:", cipher)


#4
cipher = input('Enter your cryptogram: ')
text = ''

for char in cipher:
    if not char.isalpha():
        continue

    char = char.upper()

    code = ord(char) - 1

    if code < ord('A'):
        code = ord('Z')

    text += chr(code)

print("Decrypted message:", text)


# 1
def caesar_cipher(text, shift):
    encrypted_text = ''

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text

text = input("Enter your message: ")

while True:
    try:
        shift = int(input("Enter shift value (1-25): "))
        if 1 <= shift <= 25:
            break
        else:
            print("Please enter a shift value between 1 and 25.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

encrypted_message = caesar_cipher(text, shift)
print("Encrypted message:", encrypted_message)
