import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

tasks = []
next_id = 1  # счётчик ID: ID не повторяются, даже если задачи удаляли


def add_task(title):
    global next_id
    if not title:
        print("Ошибка: название задачи не может быть пустым.")
        return
    task = {"id": len(tasks) + 1, "title": title, "done": False}
    tasks.append(task)
    print(f"Задача '{title}' добавлена.")


def list_tasks():
    print("\n--- Список задач ---")
    if not tasks:
        print("Список пуст.")
        return
    # ИСПРАВЛЕНИЕ №1: было range(len(tasks) - 1) — последняя задача пропускалась.
    # Теперь перебираем сами задачи.
    for task in tasks:
        status = "V" if task["done"] else "X"
        print(f"[{status}] ID: {task['id']} | {task['title']}")
    print("--------------------")


def mark_task_done(task_id):
    # ИСПРАВЛЕНИЕ №2: ID задачи — это не индекс в списке, поэтому ищем по ID.
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            print(f"Задача с ID {task_id} выполнена.")
            return
    print("Задача не найдена.")


def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            logging.info(f"Задача с ID {task_id} удалена.")
            return
    logging.error(f"Задача с ID {task_id} не найдена.")


def delete_completed_tasks():
    # ИСПРАВЛЕНИЕ №3: нельзя удалять элементы списка, по которому идёт цикл.
    # Собираем новый список из невыполненных задач.
    print("\nУдаление выполненных задач...")
    before = len(tasks)
    tasks[:] = [task for task in tasks if not task["done"]]
    print(f"Удалено задач: {before - len(tasks)}")


def read_task_id():
    # ИСПРАВЛЕНИЕ №4: ввод не числа больше не роняет программу.
    try:
        return int(input("Введите ID задачи: "))
    except ValueError:
        print("Ошибка: ID должен быть целым числом. Попробуйте ещё раз.")
        return None


def main():
    while True:
        print("\nМеню:")
        print("1. Добавить задачу")
        print("2. Показать задачи")
        print("3. Отметить задачу как выполненную")
        print("4. Удалить задачу по ID")
        print("5. Удалить все выполненные задачи")
        print("6. Выход")
        choice = input("Выберите действие: ")
        if choice == '1':
            title = input("Введите название задачи: ")
            add_task(title)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            task_id = read_task_id()
            if task_id is not None:
                mark_task_done(task_id)
        elif choice == '4':
            task_id = read_task_id()
            if task_id is not None:
                delete_task(task_id)
        elif choice == '5':
            delete_completed_tasks()
        elif choice == '6':
            print("Выход.")
            break
        else:
            print("Неверный ввод.")


if __name__ == "__main__":
    main()
