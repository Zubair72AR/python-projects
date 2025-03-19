import click  # Import the `click` library to create a CLI
import json  # Import `json` to save and load tasks from a file
import os  # Import `os` to check if the file exists

TODO_TASK = "todo.json"  # Define the filename where tasks are stored
# Define the filename where tasks are stored
RECYCLE_BIN_FILE = "recycle_bin.json"


def load_tasks():
    # Function to load tasks from the JSON file
    if not os.path.exists(TODO_TASK):  # Check if file exists
        return []  # If not, return an empty list
    with open(TODO_TASK, "r") as file:  # Open the file in read mode
        # Load and return the JSON data as a Python list
        return json.load(file)


def save_tasks(tasks):
    # Function to save tasks to the JSON file
    with open(TODO_TASK, "w") as file:  # Open the file in write mode
        json.dump(tasks, file, indent=4)  # Save tasks as formatted JSON


def load_recycle_bin():
    if not os.path.exists(RECYCLE_BIN_FILE):
        return []
    with open(RECYCLE_BIN_FILE, "r") as file:
        return json.load(file)


def save_recycle_bin(recycle_bin):
    with open(RECYCLE_BIN_FILE, "w") as file:
        json.dump(recycle_bin, file, indent=4)


@click.group()
def cli():
    # Define a Click command group (main CLI)
    """Simple To-Do List Manager"""  # Docstring for the CLI
    pass  # No action, acts as a container for commands


@click.command()  # Define a command called 'add'
@click.argument("task")  # Accepts a required argument (task name)
def add(task):
    """Add a new task to the list"""
    tasks = load_tasks()  # Load existing tasks
    # Append a new task (default: not done)
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)  # Save the updated tasks
    click.echo(f"Task added: {task}")  # Print a success message


@click.command()  # Define a command called 'list'
def list_tasks():
    """List all tasks"""
    tasks = load_tasks()  # Load existing tasks
    if not tasks:  # If there are no tasks
        click.echo("No tasks found!")  # Print message
        return  # Stop execution
    # Loop through tasks with numbering
    for index, task in enumerate(tasks, start=1):
        # Show '✓' for completed, '✗' for not
        status = "✅ Done" if task["done"] else "❌ Pending"
        # Print task with status
        click.echo(f"{index}. {task['task']} {status}")


@click.command()  # Define a command called 'list_recycle_bin'
def list_recycle_bin():
    """List all Recycle bin task"""
    recycle_bin = load_recycle_bin()  # Load Recycle Bin
    if not recycle_bin:  # If there are no tasks
        # Print message
        click.echo("⛔ Recycle bin is empty. No tasks to restore!")
        return  # Stop execution
    # Loop through tasks with numbering
    for index, task in enumerate(recycle_bin, start=1):
        # Show '✓' for completed, '✗' for not
        status = "✅ Done" if task["done"] else "❌ Pending"
        # Print task with status
        click.echo(f"🗑️ {index}. {task['task']} {status}")


@click.command()  # Define a command called 'complete'
@click.argument("task_number", type=int)  # Accepts a task number as an integer
def complete(task_number):
    """Mark a task as completed"""
    tasks = load_tasks()  # Load existing tasks
    if 0 < task_number <= len(tasks):  # Ensure task number is valid
        tasks[task_number - 1]["done"] = True  # Mark as done
        save_tasks(tasks)  # Save updated tasks
        # Print success message
        click.echo(f"Task {task_number} marked as completed!")
    else:
        click.echo("Invalid task number.")  # Handle invalid numbers


@click.command()  # Define a command called 'remove'
@click.argument("task_number", type=int)  # Accepts a task number as an integer
def remove(task_number):
    """Remove a task from the list"""
    tasks = load_tasks()  # Load existing tasks
    recycle_bin = load_recycle_bin()  # Recycle bin
    if 0 < task_number <= len(tasks):  # Ensure task number is valid
        removed_task = tasks.pop(task_number - 1)  # Remove the task
        # Append Removed Tasks in the Recycle bin
        recycle_bin.append(removed_task)
        save_recycle_bin(recycle_bin)  # Save Recycle Bin
        save_tasks(tasks)  # Save updated tasks
        # Print removed task
        click.echo(
            f"Removed task: {removed_task['task']} (Moved to Recycle Bin)")
    else:
        click.echo("Invalid task number.")  # Handle invalid numbers


@click.command()
@click.argument("restore_number", type=int)
def restore(restore_number):
    """Restore a task from the Recycle bin"""
    tasks = load_tasks()  # Load Task
    recycle_bin = load_recycle_bin()  # Load Recycle Bin
    if not recycle_bin:  # If there are no tasks
        # Print message
        click.echo("⛔ Recycle bin is empty. No tasks to restore!")
        return  # Stop execution
    if 0 < restore_number <= len(recycle_bin):
        restored_task = recycle_bin.pop(restore_number - 1)
        tasks.append(restored_task)
        save_tasks(tasks)
        save_recycle_bin(recycle_bin)
        click.echo(f"✅ Restored task: {restored_task['task']}")
    else:
        click.echo("❌ Invalid task number.")


# Add commands to the main CLI group
cli.add_command(add)
cli.add_command(list_tasks)
cli.add_command(list_recycle_bin)
cli.add_command(complete)
cli.add_command(remove)
cli.add_command(restore)

# If the script is run directly, start the CLI
if __name__ == "__main__":
    cli()
