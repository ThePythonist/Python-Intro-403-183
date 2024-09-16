def pn_formatter():
    phonenumber = input("Enter your phone number : ")

    if len(phonenumber) == 11:
        if phonenumber[0] == "0":
            print(phonenumber.replace("0", "+98", 1))
        else:
            print("Phone number must start with 0")
            pn_formatter()
    else:
        print("Phone number must contain 11 digits")
        pn_formatter()


pn_formatter()
