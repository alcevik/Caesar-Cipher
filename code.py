alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    #What happens if the user enters a number/symbol/space?
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")
  again = input("Do you want to restart the program? Yes or No?")
  if again == "Yes":
    start()
  else:
    print("Goodbye.")

#Import and print the logo from art.py

from art import logo
print(logo)

def start():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

#What if the user enters a shift that is greater than the number of letters in the alphabet?
  shift = shift % 26


  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

start()
