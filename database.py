# create record
# update record
# read record
# delete record
# CRUD

# find user

import os
user_db_path = "data/user_record/"


def create(user_account_number, first_name, last_name, email, password):

    # create a file
    # name of the file would be account_number.txt
    # add the user details to the file
    # return true
    # if saving to file fails, then deleted created file

    user_data = first_name + "," + last_name + "," + email + "," + password + "," + str(0)

    if account_number_exists(user_account_number):

        return False

    if does_email_exist(email):
        print("User already exists")
        return False

    completion_state = False

    try:

        f = open(user_db_path + str(user_account_number) + ".txt", "x")

    except FileExistsError:

        does_file_contain_data = read(user_db_path + str(user_account_number) + ".txt")
        if not does_file_contain_data:
            delete(user_account_number)

    else:

        f.write(str(user_data));
        completion_state = True

    finally:

        f.close();
        return completion_state


def read(user_account_number):

    # find user with account number
    # fetch content of the file
    is_valid_account_number = account_number_validation(user_account_number)

    try:

        if is_valid_account_number:
            f = open(user_db_path + str(user_account_number) + ".txt", "r")
        else:
            f = open(user_db_path + user_account_number, "r")

    except FileNotFoundError:

        print("User not found")

    except FileExistsError:

        print("User doesn't exist")

    except TypeError:

        print("Invalid account number format")

    else:

        return f.readline()

    return False


def delete(user_account_number):

    # find user with account number
    # delete the user record (file)
    # return true

    is_delete_successful = False
    if os.path.exists(user_db_path + str(user_account_number) + ".txt"):
        try:
            os.remove(user_db_path + str(user_account_number) + ".txt")
            is_delete_successful = True

        except FileNotFoundError:
            print("User not found")
        finally:
            return is_delete_successful


def does_email_exist(email):
    filenames = os.listdir(user_db_path)

    for filename in filenames:
        users_data = str.split(read(filename), ',')
        if email in users_data:
            return True
    return False


def account_number_exists(account_number):
    filenames_list = os.listdir(user_db_path)
    # note that the account number is part of the filename
    # eg xxxxxxxx.txt
    return str(account_number) + ".txt" in filenames_list


def authenticated_user(account_number, password):
    if account_number_exists(account_number):
        user = str.split(read(account_number), ',')
        if password == user[3]:
            return user

    return False


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
