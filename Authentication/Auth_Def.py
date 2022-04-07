import os
from . import Auth_Validation  # because iam run from welcome
from Database import Database_CRUD
import current_login_user
from Projects import Projects_Def


class Authentication_Class:
    validation = Auth_Validation.Validation_Class()
    database_connection = Database_CRUD.Database_Class()

    def login(self):
        print("""
        +=======================================================================================+
        |                   You Have Chosen to Login Please Enter Your Data 😁                  |
        +=======================================================================================+
        """)
        try:
            login_email = input("Enter Your Email  : ")
            login_password = input("Enter Your Password : ")

            while not self.validation.login_validation(login_email):
                print("""
        +=======================================================================================+
        |                   invalid Email or Password Enter it Aging 😢                         |
        +=======================================================================================+
                """)
                login_email = input("Enter Your Email  : ")
                login_password = input("Enter Your Password : ")

        except Exception as e:
            print(f"""
        +=======================================================================================+
        | Exception 😤 : {e}                                                                    |
        +=======================================================================================+
                """)
        else:
            self.database_connection.find_user(login_email.lower())
            if len(current_login_user.get_user()) != 0:
                if current_login_user.get_user()["password"] == login_password:
                    print("""
        +=======================================================================================+
        |                                   welcome back 🤩                                     |
        +=======================================================================================+
                    """)
                    project = Projects_Def.Project_Class()
                    project.all_projects()
                else:
                    print("""
        +=======================================================================================+
        |                                   Wrong password 🤥                                   |
        +=======================================================================================+
                    """)
                    self.main()
            else:
                os.system("cls")
                print("""
        +=======================================================================================+
        |                           There is No User With this Email 😑                         |
        +=======================================================================================+
                """)
                self.main()

    def registration(self):
        print("""
        +=======================================================================================+
        |               You Have Chosen to Register Please Enter Your Data 😁                   |
        +=======================================================================================+
        """)
        try:
            first_name = input("Enter Your First Name : ")
            # make condition false
            while not self.validation.name_validation(first_name):
                first_name = input(
                    "Invalid First Name Please Enter it Again : ")

            last_name = input("Enter Your Second Name : ")
            while not self.validation.name_validation(last_name):
                last_name = input(
                    "Invalid Second Name Please Enter it Again : ")

            user_email = input("Enter Your Email : ")
            while not self.validation.email_validation(user_email):
                user_email = input("Invalid Email Please Enter it Again : ")

            user_password = input("Enter Your Password  : ")
            while not self.validation.password_validation(user_password):
                user_password = input(
                    "Invalid Password Please Enter it Again : ")

            confirm_password = input("confirm Your Password  : ")
            while not self.validation.confirm_password_validation(user_password, confirm_password):
                confirm_password = input(
                    "password don't match Please Enter it Again : ")

            mobile_phone = input("Enter Your phone Number : ")
            while not self.validation.phone_validation(mobile_phone):
                mobile_phone = input(
                    "Invalid Phone Number Please Enter it Again : ")
        except Exception as e:
            print(f"""
        +=======================================================================================+
        | Exception 😤 : {e}                                                                    |
        +=======================================================================================+
                """)
        else:
            self.database_connection.add_user(
                id=0,
                first_name=first_name.lower().strip(),
                last_name=last_name.lower().strip(),
                email=user_email.lower().strip(),
                password=user_password.strip(),
                phone=mobile_phone.strip(),
            )
            print("""
        +=======================================================================================+
        |                               welcome in Our System 🤩                                |
        +=======================================================================================+
                    """)
            project = Projects_Def.Project_Class()
            project.all_projects()

    def authentication(self, _user_select):
        user_select = int(_user_select)
        if user_select == 1:
            self.login()
        elif user_select == 2:
            self.registration()
        elif user_select == 3:
            current_login_user.set_user()
            print("""
        +=======================================================================================+
        |                   Exit Successfully, We Hope You Will Come Back Soon 🥺               |
        +=======================================================================================+
                """)
            os.system("exit")

    def main(self):
        print("""
        +=======================================================================================+
        |                           Welcome to the Products Program 😎                          |
        +=======================================================================================+
        |                                   1.Login                                             |
        |                                   2.Regestration                                      |
        |                                   3.Exit Project                                      |
        +=======================================================================================+
        """)

        user_select = input("Enter Your Choice : ")
        while not user_select:
            print("""
        +=======================================================================================+
        |               You can't enter empty data please enter only Numbers 😢                 |
        +=======================================================================================+
        """)
            user_select = input("Enter Your Choice : ")

        if user_select.isdigit() and user_select in ["1", "2", "3"]:
            os.system("cls")  # to clear the screen
            self.authentication(user_select)
        else:
            print("""
        +=======================================================================================+
        |                           You Must Enter Only 1 or 2 or 3 👌                          |
        +=======================================================================================+
        """)
            self.main()
