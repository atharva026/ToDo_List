# [ToDo List](https://atharvamane.pythonanywhere.com)

The project goal was to develop a user-friendly platform that helps users organize their workload. With features like task creation, deletion, and marking tasks as done, the To-Do program offers an efficient and straightforward task management experience.

## Features

1. **User-friendly Interface**: Simple and intuitive interface for managing tasks.
2. **Task Creation**: Easily add new tasks to your to-do list.
3. **Task Deletion**: Remove tasks from the list when no longer needed.
4. **Mark as Done**: Mark tasks as completed to keep track of your progress.

## How to Use

1. **Open the Application**: Visit the [ToDo List](https://atharvamane.pythonanywhere.com) web application.
2. **Create Task**: Add a new task by typing in the input field and clicking the "Add" button.
3. **Manage Tasks**: 
   - **Delete Tasks**: Click the delete button next to a task to remove it from the list.
   - **Mark Tasks as Done**: Click the checkbox next to a task to mark it as completed.

## Installation

To set up the project locally, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using `git clone`.

    ```bash
    git clone https://github.com/atharva026/ToDo_List
    ```

2. **Navigate to the Directory**: Change into the project directory.

    ```bash
    cd ToDo_List
    ```

3. **Install Dependencies**: Install the necessary dependencies.

    ```bash
    pip install flask flask_sqlalchemy
    ```

4. **Set Up the Database**: Create the necessary database tables.

    ```bash
    from app import app, db
    with app.app_context():
        db.create_all()
    ```

5. **Run the Application**: Start the application.

    ```bash
    python -u app.py
    ```

6. **Access the Application**: Open your browser and go to `http://localhost:3000`.

## Troubleshooting

If you encounter issues during setup or while using the application, consider the following steps:

- Ensure all dependencies are installed correctly.
- Verify the database setup is complete.
- Check the console for any error messages and address them accordingly.
- Restart the application after making any changes.

## Contact

If you have any questions or suggestions, please feel free to contact me at [atharvam99@gmail.com](mailto:atharvam99@gmail.com).

---

Thank you for using the ToDo List! Happy organizing!
