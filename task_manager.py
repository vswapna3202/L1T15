"""
This program helps a small business manage tasks assigned to each member of
its team.
Referred: For current date and formatting dates referred the links below
https://stackoverflow.com/questions/65894809/python-convert-date-format-yyyy-mm-dd-to-dd-mon-yyyy-with-abbreviated-month
https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime.datetime.today
https://docs.python.org/3/library/datetime.html?highlight=datetime#strftime-and-strptime-behavior
Referred: For removing space from string
https://www.geeksforgeeks.org/python-remove-spaces-from-a-string
Referred: For file operations
https://docs.python.org/3/library/io.html#seeking
https://stackoverflow.com/questions/28873349/python-readlines-not-returning-anything
https://www.geeksforgeeks.org/python-try-except/
"""
from datetime import datetime

"""
Constants are declared at the beginning so it is easier to change them if 
needed. The file names user.txt and tasks.txt are declared. Also, the 
date formats are declared.
"""
USER_FILE_NAME = "user.txt"
TASK_FILE_NAME = "tasks.txt"
TASK_FILE_DATE_FORMAT = "%d %b %Y"
INPUT_DATE_FORMAT = "%d/%m/%Y"
ADMIN_USER = "admin"


def open_file(file_name, open_for):    
    """
    This function opens the filename in either read mode or append+ mode
    depending on what open_for variable holds
    param:  file_name name of the file to be opened
            open_for holds r , a or a+ for read or append or append/read
    return: file object is returned
    """
    try:    
        file = open(file_name, open_for)
        return file
    except FileNotFoundError:
        print(f"\n{file_name} does not exist! Cannot proceed!")
        exit()


def close_file(file):
    """
    This function closes the file which is sent as parameter
    param: file the file to be closed
    return: None
    """
    file.close()


def login_user():
    """
    This function checks the user login credentials and if correctly 
    entered logins in the user and allows to proceed further.
    param: none
    return: username is needed for further operations so it is returned
    """

    while True:           
        # Get username, password from user
        username, password = get_user_details() 
        
        # Fetch login details stored in user.txt and match with user details
        # entered by user
        file = open_file(USER_FILE_NAME, "r")
        if check_user_exists(file, username, password):           
            print("\nYour login credentials are correct! \n")  
            close_file(file)
            return username  
        else:
            close_file(file)
            print("\nYou entered incorrect username or password. Please enter again\n")    


def get_user_details(): 
    """
    This function gets username and password from the user.
    param:: None
    return: username, password: Returns username and password entered
    """  
    username = input("Enter username: ")
    password = input("Enter password: ")  
    return username, password
    
      
def register_user(username): 
    """
    This function checks if the current user is an admin. If so registers a 
    new user. It gets new username and password. If user confirms password 
    correctly writes credentials to file user.txt following convention of 
    separating username and password by , and a single space on a new line. 
    If not user not registered message is displayed. If username already 
    exists an appropriate message is displayed and user not registered
    param: username username who is logged in and registering new users
    return: None
    """ 
    if (username == ADMIN_USER):   # Allow registration to happen
        new_username, new_password, passwords_match = get_register_details() 
        if passwords_match:                      
            file = open_file(USER_FILE_NAME, "a+")
            file.seek(0)

            # Check if user already exists in user.txt if so user cannot
            # be registered
            if not check_user_exists(file, new_username, ""): 
                file.write(f"\n{new_username}, {new_password}")                   
                print("\nUser registered successfully!\n")                    
            else:
                print(f"\nUser {new_username} already exists cannot register!\n")
            close_file(file)        
        else:
            print("\nPasswords do not match cannot register user\n")   
    else:
        print("\nYou are not an admin. You do not have privileges to register a user\n")    


def get_register_details():  
    """
    This function gets the new username and password to be registered.
    It asks user to confirm password entered. Passwords match set to
    True if not set to False
    param:: None
    return: username, password, passwords_match: Username, password and 
    if password matches confirmed return True else False    
    """
    print("\nEnter new user details to be registered: ")
    username, password = get_user_details()    
    confirm_password = input("Confirm the password entered: ")
    passwords_match = password == confirm_password

    return username, password, passwords_match    

def check_user_exists(file, username, password):
    """
    This function checks if the user already exists in user.txt file
    Username and password are checked if it is login credential check
    and only username is checked if it is register a user.
    param: file: file object 
           username: username to check  if user is a valid user
           password: password is sent if operation is login user, if register
           new user or task password is sent as null as we need to check only 
           user exists or not  
    return: True if user/password already exists in user.txt else False
    """        
    user_exists_flag = False       
    
    if file:
        lines = file.readlines()    
        for line in lines:
            contents = line.strip().split(", ")
            if (password):
                if (username == contents[0] and password == contents[1]):
                    user_exists_flag = True # A match found no need for further check
                    break
            else:
                if (username == contents[0]):
                    user_exists_flag = True
                    break                
    else:
        print(f"\nError! {USER_FILE_NAME} does not exist!")
    return user_exists_flag     


def get_task_details():
    """
    This function gets all task details from the user. It gets the date in
    format dd/mm/yyyy and converts it to format dd mon yyyy as shown in 
    tasks.txt file. It also adds current date to the user string which
    has username, title, description, current date, due date and task
    completion status all separated by ,<space>
    param: None
    return: file_data string of all data to be written in tasks.txt
    """
    username = input("\nPlease enter username task should be assigned to: ")

    # Check if user exists in users.txt and user is valid to be assigned a task
    # Password does not need checking so sending it empty to the function
    file = open_file(USER_FILE_NAME, "r")
    user_exists_flag = check_user_exists(file, username, "") 
    close_file(file)

    # If user is valid and exists in user.txt allow user to input further 
    # task details else print message user is not valid
    if (user_exists_flag):

        title = input("Please enter title of task: ")
        description = input("Please enter description of task: ")

        # Check if user has entered date in correct format if not throw a 
        # error message and ask the user for correct date
        date_flag = True
        while (date_flag):
            try:
                due_date_str = input("Please enter due date of task(dd/mm/yyyy): ") 
                # Format due_date to be in correct date format as stored already in file
                # tasks.txt
                due_datetime = datetime.strptime(due_date_str, INPUT_DATE_FORMAT)
                date_flag = False   
            except ValueError:
                print("\nDate is not entered in correct format! Please enter correctly") 
                date_flag = True
        
        due_date = due_datetime.strftime(TASK_FILE_DATE_FORMAT)

        # Get current date and set in same format as already existing in 
        # tasks.txt    
        current_date = datetime.today().strftime(TASK_FILE_DATE_FORMAT)
        file_data = f"\n{username}, {title}, {description}, {current_date}, {due_date}, No"  
        return file_data         
    else:
        print("\nUser does not exist cannot add task for this user!\n")
    

def add_task(): 
    """
    This function gets all task details from user and writes all the 
    details entered by user to file tasks.txt.     
    param: None
    return: None
    """

    # Get all task details
    file_data = get_task_details() 

    # Write all captured details to file tasks.txt after opening file in a+
    # mode. Do seek (0)
    file = open_file(TASK_FILE_NAME, "a")
    file.seek(0)   

    # If file_data has data in it that means user was valid and further data
    # was inputed by user and sent in file_data   
    if file_data:
        if file:        
            file.write(file_data)                
            print("\nTask details have been added successfully!")
            close_file(file)
        else:
            print(f"\nError! {TASK_FILE_NAME} does not exist!")


def read_tasks(read_all, username):
    
    """
    This function reads all the tasks in file tasks.txt and displays it to 
    the user in a easy to read format if read_all is true. If not it reads 
    the task record matching the username passed from all user records and 
    displays this user's task details
    param: read_all: True reads all records, False prints record matching
    username
    return: None
    """     
    file = open_file(TASK_FILE_NAME, "r")
    if file:
        record_found = False
        lines = file.readlines()               
        print("_"*70)       # Print lines to keep output neat

        # Loop through all the records in tasks.txt split the records based 
        # on , space and remove \n. Print index to show Record No. Print all
        # task records
        for index, line in enumerate(lines, start=0):                      
            contents = line.strip().split(",")    
            if (read_all):  # Prints all task records
                print(f"TASK DETAILS OF USER: {index+1}")             
                print_tasks(contents)                   
            else:   # Prints record matching username
                if (username == "".join(contents[0])):  
                    print_tasks(contents)                   
                    record_found = True                 
                    break     
        if not read_all and not record_found:   
            print(f"\nNo Task records exists for user: {username}\n")       
        close_file(file)
    else:
        print(f"\nError! {TASK_FILE_NAME} does not exist!")      


def print_tasks(task_record):   
    
    """
    Prints all the task details from the file tasks.txt. Displays in a easy 
    to read format.
    param: task_record: Holds the task record from file tasks.txt
    return: None
    """                 
    print("_"*70+"\n")     
    print("Task:\t\t\t\t", end="")
    print(task_record[1])            
    print("Assigned to:\t\t\t", end=" ")
    print(task_record[0])                      
    print("Date assigned: \t\t\t", end= "")
    print(task_record[3])
    print("Due date: \t\t\t", end="")
    print(task_record[4])
    print("Task complete?: \t\t", end="")
    print(task_record[5])
    print("Task description:")
    print(task_record[2].lstrip())
    print("_"*70)


def display_statistics(file_name):
    
    """
    This function reads the users.txt file and finds the total number of 
    users and reads the tasks.txt file and finds the total number of tasks 
    and displays this to the user.
    param: file_name name of file to be opened
    return: None
    """    
    
    file = open_file(file_name, "r")
    lines = file.readlines()      
    if (file_name == USER_FILE_NAME):
        print("_"*35)    
        print(F"\nTotal number of users are: {len(lines)}") 
    else:
        print(f"\nTotal number of tasks are: {len(lines)}")
        print("_"*35)
    close_file(file)   


def main():
    """
    This is the main function where users login credentials are checked and menu  
    displayed. Depending on user selection the resepective functions are called 
    data fetched and displayed or file updated.
    param: None
    return: None
    """   
    # Check user login credentials are correct and login user
    username = login_user()

    while True:
        # Present the menu to the user and 
        # make sure that the user input is converted to lower case.
        # If user is "admin" display extra menu of display statistics
        if (username != ADMIN_USER):    
            menu = input('''Please select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()
        else:
            menu = input('''Please select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
ds - display statistics                         
e - exit
: ''').lower()            

        if menu == 'r':             
            # Invoke function to register a new user
            register_user(username)
        elif menu == 'a':                   
            # Function add_task() to add task details entered by user to task.txt
            add_task()
        elif menu == 'va':                   
            # Function read_tasks() which reads all tasks for all users and 
            # displays it to user            
            read_tasks(True, username)
        elif menu == 'vm':                  
            # Function read_current_user_task which fetches task details of 
            # username and displays it to user                 
            read_tasks(False, username)
        elif menu == 'ds' and username == ADMIN_USER:
            # Function to display statistics to admin user of total number of 
            # users and total number of tasks            
            display_statistics(USER_FILE_NAME)
            display_statistics(TASK_FILE_NAME)           
        elif menu == 'e':
            print('Goodbye!!!')
            exit()
        else:
            print("You have made entered an invalid input. Please try again")


# Call the main function
main()