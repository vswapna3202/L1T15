## L1T15 : Capstone Project Task Manager ##
This program helps a small business to manage tasks assigned to its members.The program will work with two text files:   
**user.txt**
```
    1. Stores the username and password for each user that has permission to 
    use your program.  The username and password for each user to this file 
    is in the following format:
        ■ The username followed by a comma, a space, and then the password.
        ■ Only record one username and corresponding password per line.
```
**tasks.txt**
```

    1. Stores a list of all the tasks the team is working on
    2. The data for each task is stored on a separate line in the text file
    3. Each line includes the following data about a task in this order:
    The username of the person to whom the task is assigned.
        ■ The title of the task.
        ■ A description of the task.
        ■ The date that the task was assigned to the user.
        ■ The due date for the task.
        ■ Either a ‘Yes’ or ‘No’ value that specifies if the task has been
        completed.
```  
The program performs the following actions:

■   **Login**:   

    Prompts the user to enter a username and password. 
    A list of valid usernames and passwords is stored in the user.txt text file. 
    Displays an error message "You entered incorrect username or password. Please enter again" if the user enters a username that is not listed in user.txt or enters a valid username but not a valid password. The user is repeatedly asked to enter a valid username and password until they provide appropriate credentials.  

■   **Menu Display**:  
    The following menu is displayed once the user has successfully logged in:  
```  
        Please select one of the following options:  
            r - register user  
            a - add task  
            va - view all tasks  
            vm - view my tasks  
            ds - display statistics (Displayed only for admin users)  
            e - exit 
``` 
■   **User selects menu option r - register user**:
    The user is prompted for a new username and password. The user is asked to confirm the password. If the value entered to confirm the password matches the value of the password, the username and password is written to user.txt in the appropriate format matching existing user.txt.          

■   **User selects menu option a - add task**:
        The user is prompted to enter the username of the person the task is assigned to, the title of the task, a description of the task, and the due date of the task. The data about the new task is written to tasks.txt. The date on which the task is assigned is the current date. The value that indicates whether the task has been completed or not defaults to ‘No’.  

■   **User selects menu option va - view all tasks**:
        Displays the information for each task on the screen in format:
```
        ______________________________________________________________________     
        TASK DETAILS OF USER: 2
        ______________________________________________________________________     

        Task:                            Assign initial tasks
        Assigned to:                     admin
        Date assigned:                   10 Oct 2019
        Due date:                        25 Oct 2019
        Task complete?:                  No
        Task description:
        Use task_manager.py to assign each team member with appropriate tasks      
        ______________________________________________________________________     
        TASK DETAILS OF USER: 3
        ______________________________________________________________________     

        Task:                            Assign payment tasks
        Assigned to:                     swap1
        Date assigned:                   14 Aug 2023
        Due date:                        10 Sep 2023
        Task complete?:                  No
        Task description:
        Assign payment related tasks to accounts team
        ______________________________________________________________________     
```

■   **User selects menu option vm - view my tasks**:
    Displays the information related to tasks that have been assigned to current user in format:
```
    ______________________________________________________________________     

    Task:                            Register Users with task_manager.py       
    Assigned to:                     admin
    Date assigned:                   10 Oct 2019
    Due date:                        20 Oct 2019
    Task complete?:                  No
    Task description:
    Use task_manager.py to add the usernames and passwords for all team members that will be using this program.
    ______________________________________________________________________  
```

**Further Conditions:**    
    - Only the user with the username ‘admin’ is allowed to register users.
    - The admin user is provided with a new menu option that allows them to display statistics. When this menu option is selected, the total number of tasks and the total number of users is displayed as:
```
    ___________________________________

    Total number of users are: 2

    Total number of tasks are: 3
    ___________________________________
```
        
## Installation
1. **Python**: Ensure Python is installed on your system. You can download it from the [official Python website](https://www.python.org/).
2. **Version**: These programs are written in Python 3. Make sure you have Python 3.x installed.

### Clone the Repository
```bash
git clone https://github.com/vswapna3202/L1T15.git  
```

## Running the programs <br>
Navigate to the directory of each Python file
Run Python using python interpreter
```
python task_manager.py
```

## Files needed for the program to give correct output: ##
```
tasks.txt
user.txt
```
