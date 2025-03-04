import click
import os
import json

Todolist = "todo.json"

def load_task():
    if not os.path.exists(Todolist):
        return []
    with open(Todolist, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []  # If the file is empty or corrupted

def save_task(task):
    with open(Todolist, 'w') as file:
        json.dump(task, file, indent=4)

@click.group()
def cli():
    """A simple todo list"""
    pass

@click.command()
@click.argument('task')
def add(task):
    """Add a new task to the list"""
    tasks = load_task()
    tasks.append({"task": task, "done": False})
    save_task(tasks) 
    click.echo(f"✅ Task added Successfully: {task}")

@click.command(name="list")  # Avoid name conflict
def list_tasks():
    """List all tasks"""
    tasks = load_task()
    if not tasks:
        click.echo("📂 No task found")
        return
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        click.echo(f"{i}. [{status}] {task['task']}")

@click.command()
@click.argument('task_number', type=int)
def complete(task_number):
    """Mark a task as completed"""
    tasks = load_task()
    try:
        tasks[task_number - 1]["done"] = True
        save_task(tasks)
        click.echo(f"🎯 Task {task_number} marked as completed")
    except IndexError:
        click.echo("⚠️ Invalid task number")

@click.command()
@click.argument('task_number', type=int)
def delete(task_number):
    """Delete a task"""
    tasks = load_task()
    try:
        del tasks[task_number - 1]
        save_task(tasks)
        click.echo(f"🗑️ Task {task_number} deleted")
    except IndexError:
        click.echo("⚠️ Invalid task number")

cli.add_command(add)
cli.add_command(list_tasks, name="list")
cli.add_command(complete)
cli.add_command(delete)

if __name__ == '__main__':
    cli()
