#todo

from storage import load_tasks, save_tasks


def add_task(text):
    tasks = load_tasks()

    task = {
        "id": len(tasks) + 1,
        "text": text,
        "done": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print(f'Задача "{text}" добавлена.')

#DARKle

def list_tasks():
    tasks = load_tasks()

    if not tasks:
        print("Список задач пуст.")
        return

    for task in tasks:
        status = "✓" if task["done"] else " "
        print(f'[{status}] {task["id"]}. {task["text"]}')


def done_task(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)

            print("Задача отмечена как выполненная.")
            return

    print("Задача не найдена.")


def remove_task(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)

            for index, t in enumerate(tasks, start=1):
                t["id"] = index

            save_tasks(tasks)

            print("Задача удалена.")
            return

    print("Задача не найдена.")