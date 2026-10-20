import pyfiglet

def create_ascii_art(name):
    ascii_art = pyfiglet.figlet_format(name)
    return ascii_art

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(create_ascii_art(user_name))