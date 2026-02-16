class chatbook:
    
    
    def __init__(self):
        
        self.username = ""
        self.password = ""
        
        self.loggedin = False
        self.menu()
        
    
    def menu(self):
        
        user_input = input(
            """Welcome to the chatbook! How would you like to proceed
            
            1. Press 1 to signup
            2. Press 2 to signin
            3. Press 3 to write a post
            4. Press 4 to message a friend
            5. Press any other key to exit
            
            """
        )
        
        if user_input == "1":
            
            self.signup()
        elif user_input == "2":
            
            self.signin()
        
        elif user_input == "3":
            
            self.my_post()
        elif user_input == "4":
            
            pass
        
        else:
            
            exit()


    def signup(self):

        email = input("Enter your email here")
        password = input("Enter your password here")

        self.username = email
        self.password = password

        print("Account created successfully!")

        print("\n")

        self.menu()

    def signin(self):
        if self.username == "" and self.password == "":
            print("You are not loggedin")

        else:

            username = input("Enter your username please")
            password = input("Enter your password please")

            if username == self.username and password == self.password:
                print("You are logged in successfully")

                self.loggedin = True

                self.menu()

            else:

                print("Invalid credentials")

                self.menu()


    def my_post(self):

        if self.loggedin == True:

            post = input("Enter your message here - > ")

            print("Post created successfully!")

            self.menu()

        else:

            print("Please Signin first")

            self.menu()

    def send_msg(self):

        if self.loggedin == True:

            message = input("Enter your message here - > ")

            friend = input("Enter your friend's name here - > ")

            print("Message sent successfully to ", friend)

            self.menu()

        else:

            print("Please Signin first")

            self.menu()




chat1 = chatbook()