from ceaser_cipher_utils import cipher,logo

print(logo)

repeat = True
while repeat:
    option = input("\nType \"ENCODE\" to encode your message (or) \"DECODE\" to decode your encoded message: ")
    text = input("Enter the message: ")
    shift = int(input("Enter the shift number: "))
    result = cipher(text,shift,option)
    print(result)
    opinion = input("Do you wish you want to continue??\n \"Yes\" or \"No\" : ")
    if opinion.lower() == "yes":
        repeat = True
    else:
        repeat = False
        print("Good Bye!!")