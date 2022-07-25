import emailGen as gen

def main():
    y = (input('Would you like to generate a throwaway email? y/n: '))
    if y == 'y':
        email = gen.genEmail()
    else:
        quit()
    print("Your email is", email)
    x = (input(('Would you like to see your inbox? y/n: ')))
    while True:
        if x == 'y':
            print(gen.readInbox(email))
        x = (input(('Would you like to see your inbox? y/n: ')))
        if x == 'n':
            main()
    
if __name__ == '__main__':
    main()