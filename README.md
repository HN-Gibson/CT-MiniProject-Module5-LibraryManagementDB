# CT-MiniProject-Module5-LibraryManagementDB
**Presenting a Library Database Management Program**

**Welcome and thank you for using my program!**

**Goal of the program**
To offer a seemless means of managing a library database containing book info, author info, user info, and allow for easy check-in and check-out features.

**Important Notes:**
- There are three primary collections in the library that you will access via different menus.
    1. The Library Database
    2. The User Database
    3. The Author Database
- Throughout the program, you will be given the option to return to the main menu when met with a menu. Please pay attention to the menu options as they are presented.
- The only means of quitting the program is from the main menu. So, when you're finished using the features of one menu, return to the main menu if you would like to exit.
- When navigating the menus, leaving inputs blank (i.e. Hitting enter without typing an input) may result in having to re-enter information.

**BEFORE RUNNING THE MAIN PROGRAM, ENTER YOUR PASSWORD IN THE 'connect_mysql.py' & RUN 'construct_tables.py'**

**Now, to the important how to of my program:**

- When you start the program by running the 'main.py', you will be met with four options. These represent the means of accessing the three primary collections within the program as well as an option to quit the program.

**Note: When using the menus, please make sure you are entering the number associated with the menu option and not the name of that option**

1. Book Operations

    - Within this menu, you are able to access the Library to: 
        1. Add books, including information about the author, genre, and date it was published.
            - Note: All newly added books will enter the collection with a designation of available. To change this, use the Borrow a book option to update the status as well as who has the book.
        2. Borrow a book, making note of the user that has it checked out and tieing that information to their User ID.
            - This feature uses the User and Book IDs, so please make note of these items before trying to utilize this feature.
        3. Return a book, noting the book was returned in the logs associated with the user.
            - This feature uses the User and Book IDs, so please make note of these items before trying to utilize this feature.
        4. Search for a specific book to see it's information, including if it is available.
            - This feature allows you to search for a book even if you do not know the full title. Simply enter part of what the title is to see if a result is found.
        5. Display the title of all books in the Library.
            - Note: This option can be used prior to searching to see what is in the library.
        6. Return to Main Menu
    - After completeing an operation, you will have the opporunity to continue accessing other operations in this menu before returning to the main menu.

2. User Operations

    -Within this menu, you are able to access the User Database to:
        1. Add user names, which will in turm be linked to a user ID automatically. This User ID is used frequently.

        2. View user details, such as name, User ID, and what books they have currently by searching with the associated User ID.

        3. Display all Users, allowing you to see all the User IDs associated with different users.

            -Note: This option can be used prior to searching to see what is in the database.

        4. Return to Main Menu

            - After completeing an operation, you will have the opporunity to continue accessing other operations in this menu before returning to the main menu.

3. Author Operations

    -Within this menu, you are able to access the Author Database to:

        1. Add authors, including a brief bio.

            - Authors are not automatically added when a book by them is added

        2. View author details, including their name and bio, by searching using the author's name.

            - You do not have to enter the author's full name. Searching with a partial name will pull all matching results.

        3. Display all authors, allowing you to see all authors in the system.

            -Note: This option can be used prior to searching to see what is in the database.

        4. Return to Main Menu
        
            - After completeing an operation, you will have the opporunity to continue accessing other operations in this menu before returning to the main menu.

**Technical Notes**
 1. All functions are contained in the LibraryOps.py file.
 2. The UI.py file is the heart of the program, determining how and what userss are able to access.
 3. The main.py file is used solely to run the program.
 4. When using the add features, your additions will be added to the database even if the book, author, or user already exists. This aspect of the program is still a WIP. I plan to add more verification and error handling in the future to eliminate duplicate entries, but I also want to make sure the constraints are not so strigent that users have a hard time entering items with similar titles or names.
 5. Finally, a second reminder **BEFORE RUNNING THE MAIN PROGRAM, ENTER YOUR PASSWORD IN THE 'connect_mysql.py' & RUN 'construct_tables.py'**

Above all else, enjoy my program. Your feedback is critical to my success. I look forward to receiving it!

**Thank you for using my program**