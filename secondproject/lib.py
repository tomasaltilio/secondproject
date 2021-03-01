def try_me():
    answer = input('This is a test. Hope you like it... Well, do you? y/n\n')
    
    if answer == 'y':
        print('Awesome! I like you too')
        return
    elif answer == 'n':
        print("That's too bad. See ya")
        return
        
        
if __name__ == "__main__":
    try_me()