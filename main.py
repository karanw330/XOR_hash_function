import random


def xor(a, b):
    if int(a) == int(b):
        return 0
    else:
        return 1

def convert_to_binary(num):
    #built-in python function bin() can be used instead of defining our own
    temp = num
    li = []
    while temp != 0:
        li.insert(0, temp % 2)
        temp = int(temp / 2)
    while len(li) != 8:
        li.insert(0, 0)
    return li

def convert_from_binary(bin_list):
    weight = 0
    ascii_num = 0
    for j in reversed(bin_list):
        ascii_num += j*(2**weight)
        weight +=1
    return ascii_num


characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
              'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!',
              '#', '$', '%', '&', '(', ')', '*', '+']

message = str(input("Enter message to encrypt\n"))
binary_message = []

#----------------------------------------conversion of message into binary----------------------------------------

for letter in message:
    ascii_val = ord(letter)
    encrypt = convert_to_binary(ascii_val)
    binary_message.append(encrypt)

#----------------------------------------generation and conversion of key----------------------------------------
key = random.choice(characters)
ascii_key = ord(key)
binary_key = convert_to_binary(ascii_key)

#-----------------------------------------------encryption process-----------------------------------------------

encrypted_list = []

for char in binary_message:
    encrypted_letter = []
    for i in range(8):
        encrypted_letter.append(xor(int(binary_key[i]), int(char[i])))
    encrypted_list.append(encrypted_letter)


encrypted_string = ""

for ch in encrypted_list:
    asc_ = convert_from_binary(ch)
    if asc_ >= 0 and asc_ <= 33:
        asc_ = 33
    elif asc_ >= 125 and asc_ <=127:
        asc_ = 125
    else:
        pass
    encrypted_string += str(chr(asc_))
print(encrypted_string)