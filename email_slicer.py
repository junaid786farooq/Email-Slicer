# Programe that use for Email slicing.

def main():
    
    print("Welcome to the email slicer!")

    while True:
        email_input = input("Enter your Email address or Exit(e): ")

        if email_input == "e" or email_input == "E":
            break
        else:
            try:
                (username, domain) = email_input.split("@")
                (domain, extention) = domain.split(".")
            
                print("Username: ", username)
                print("Domain: ", domain)
                print("Extention: ", extention )
            except ValueError:
                print("Error: Please enter a valid input!")

main()