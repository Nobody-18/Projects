class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
    
choice = input("Press '1' then 'Enter' to log in \nPress '2' then 'Enter' to create a new user")
if choice == '1':
    
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    try:
        with open(f"{username}.txt")as f:
            if f.read() == password:
                print("you have succesfully loged in !!")
            else:
                print("incorrect password!!")
    except FileNotFoundError:
        print("there is no user with your username !")
        
        
    

elif (choice == '2'):
     username = input("Please enter a username: ")
     password1 = input("Please enter a password: ")
     password2 = input("Please reeneter your password: ")
     try:
        if password1 == password2:
            name = User(username, password1)
            with open(f"{username}.txt",'x' ) as f:
                f.write(password1)
            print(f"{username} has been successfully added as a new user!!")
        else:
            print("Your passwords do not match please try again!")
     except FileExistsError:
        print("a user with same username already exist!!")
        
