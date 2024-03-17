alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def ceaser(what_to,text,shift):
    if what_to=='decrypt':
        shift*= -1
   
    cipher=""
    for char in text:
        if char in alphabet:
            position=alphabet.index(char)
            new=(position+shift)%26
            cipher+=alphabet[new]
        else:
            cipher+=char
    print("\nThe "+what_to+"ed text is "+cipher) 


end=False
print("                  WELCOME TO CEASER CIPHER TECHNIQUE\n")
while not end:
    what_to_do=input("Type 'encrypt' for encryption and 'decrypt' for decryption:\n")
    text=input("\nEnter the message:\n").lower()
    shift=int(input("\nEnter the key:\n"))

    ceaser(what_to_do,text,shift)

    play=input("\nType 'yes' to continue and 'no' to end...\n").lower()
    if play=='no':
        end=True
        print("\nThank you")
