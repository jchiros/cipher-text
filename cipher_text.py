from cipher_text_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z'] #Copied one more time so it can loop if the input letter is z

print(logo)
def caesar(direct, ptext, ashift):
    cipher_text = ""
    if direction == 'encode':
        for letter in ptext:
            if letter in alphabet: #This will retain the symbols, spaces, and numbers
                pos = alphabet.index(letter)   #will store the position of the inputted letter in the text alphabet
                new_pos = pos + ashift   #adding the position to the shift number
                new = alphabet[new_pos]   #assigned new position of the index
                cipher_text += new
            else:
                cipher_text+=letter #adding the symbols, spaces, numbers together with the encoded string
        print(f"The encoded text is: {cipher_text}")
    else:
      decipher_text = ""
      for letter in ptext:
          if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position - ashift   #subtracts the current position to the shift number
            decipher_text += alphabet[new_position]
          else:
            decipher_text += letter
      print(f"The decoded text is: {decipher_text}")

ifContinue = True  #Will loop through the entire code
while ifContinue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26 #If the input is greater than the alphabet, it will shift down to fit in 26

    caesar(direct=direction, ptext= text, ashift= shift)
    choice = input("\nType 'y' to continue. Otherwise type 'n'\n")
    if choice == 'n':
        ifContinue = False
        print("Thank you for using Caesar Cipher.")

