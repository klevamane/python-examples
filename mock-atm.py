# register
# - first name, last name, password, email
# - generate user account number


# login
# - account number & password


# bank operations

# Initializing the system
import random
import database
from getpass import getpass
import datetime

user_db_path = "data/user_record/"


def init():
    print("Welcome to bankPHP")

    have_account = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if have_account == 1:

        login()

    elif have_account == 2:

        register()

    else:
        print("You have selected invalid option")
        init()


def login():
    print("********* Login ***********")

    account_number_from_user = input("What is your account number? \n")

    is_valid_account_number = account_number_validation(account_number_from_user)

    if is_valid_account_number:

        password = getpass("What is your password \n")

        user = database.authenticated_user(account_number_from_user, password);

        if user:

            print("current DateTime - ", datetime.datetime.today().strftime('Date: %d %B %Y Time: %H:%M'))
            bank_operation(user)

        print('Invalid account or password')
        login()

    else:
        print("Account Number Invalid: check that you have up to 10 digits and only integers")
        init()


def register():
    print("****** Register *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = getpass("Create a password for yourself \n")

    account_number = generation_account_number()

    is_user_created = database.create(account_number, first_name, last_name, email, password)

    if is_user_created:

        print("Your Account Has been created")
        print(" == ==== ====== ===== ===")
        print("Your account number is: %d" % account_number)
        print("Make sure you keep it safe")
        print(" == ==== ====== ===== ===")

        login()

    else:
        print("Something went wrong, please try again")
        register()


def bank_operation(user):
    print("Welcome %s %s " % (user[0], user[1]))

    selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

    if selected_option == 1:
        deposit_operation(user)

    elif selected_option == 2:
        withdrawal_operation(user)

    elif selected_option == 3:
        logout()

    elif selected_option == 4:
        exit()
    else:

        print("Invalid option selected")
        bank_operation(user)


def withdrawal_operation(user):
    withdrawal_amount = int(input("How much would you like to withdraw \n"))
    current_balance = int(get_current_balance(user))
    if withdrawal_amount > current_balance:
        print("Insufficient funds")
        return bank_operation(user)
    current_balance -= withdrawal_amount
    set_current_balance(user, current_balance)
    print("New balance: {}".format(get_current_balance(user)))


def deposit_operation(user):
    deposit_amount = int(input("How much would you like to deposit \n"))
    current_balance = int(get_current_balance(user))
    current_balance += deposit_amount
    set_current_balance(user, current_balance)
    print("New balance: {}".format(get_current_balance(user)))
    return


def complaint_operation():
    input("What issue would you like to report?")
    print("Thank you for contacting us")


def set_current_balance(user_details, balance):
    user_details[4] = balance


def get_current_balance(user_details):
    return user_details[4]


def generation_account_number():
    return random.randrange(4111111111, 9999999999)


def logout():
    login()


def account_number_validation(account_number):
    if account_number:
        try:
            int(account_number)

            if len(str(account_number)) == 10:
                return True

        except ValueError:
            return False
        except TypeError:
            return False

    return False

init()
