import json
from json import JSONDecodeError

# Официальная палитра Nord (ANSI коды)
NORD_BLUE = "\033[38;5;110m"
NORD_GREEN = "\033[38;5;150m"
NORD_YELLOW = "\033[38;5;221m"
NORD_RED = "\033[38;5;131m"
NORD_SNOW = "\033[38;5;253m"
RESET = "\033[0m"


def menu():
    print(
        f"{NORD_BLUE}"
        "\n┌──────── МЕНЕДЖЕР ЗАДАЧ ────────┐\n"
        "│ 1 — Показать все записи        │\n"
        "│ 2 — Добавить запись            │\n"
        "│ 3 — Отметить выполненной       │\n"
        "│ 4 — Редактировать задачу       │\n"
        "│ 5 — Удалить запись             │\n"
        "│ 6 — Поиск                      │\n"
        "│ 7 — Выход                      │\n"
        "└────────────────────────────────┘"
        f"{RESET}"
    )


def open_json(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, JSONDecodeError):
        return []


def save_tasks(path, data):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def show_tasks(tasks):
    if not tasks:
        print(f"{NORD_RED}Список пуст{RESET}")
    else:
        for task in tasks:
            id_task = task["id"]
            if task["done"]:
                status = f"{NORD_GREEN}[x]{RESET}"
                title = f"{NORD_GREEN}{task['title']}{RESET}"
            else:
                status = f"{NORD_BLUE}[ ]{RESET}"
                title = f"{NORD_SNOW}{task['title']}{RESET}"
            print(f"{id_task}. {status} {title}")


def add_task(path, tasks):
    note = input(f"{NORD_SNOW}Введите задачу: {RESET}").strip()
    if not note:
        print(f"{NORD_RED}Задача не может быть пустой.{RESET}")
        return

    id_note = tasks[-1]["id"] + 1 if tasks else 1
    tasks.append({"id": id_note, "title": note, "done": False})
    save_tasks(path, tasks)
    print(f"{NORD_GREEN}Успешно добавлено!{RESET}")


def complete_task(path, tasks):
    try:
        id_changed_task = int(
            input(f"{NORD_SNOW}Введите ID задачи, которую вы хотите выполнить: {RESET}")
        )
        if not tasks:
            print(f"{NORD_RED}Список пуст{RESET}")
            return

        found = False
        for task in tasks:
            if task["id"] == id_changed_task:
                task["done"] = True
                save_tasks(path, tasks)
                print(f"{NORD_GREEN}Успешно выполнено!{RESET}")
                found = True
                break
        if not found:
            print(f"{NORD_RED}Запись с таким id не найдена.{RESET}")
    except ValueError:
        print(f"{NORD_RED}Неправильный тип данных (введите число){RESET}")


def edit_task(path, tasks):
    try:
        id_edit = int(
            input(f"{NORD_SNOW}Введите ID задачи для редактирования: {RESET}")
        )
        if not tasks:
            print(f"{NORD_RED}Список пуст{RESET}")
            return

        found = False
        for task in tasks:
            if task["id"] == id_edit:
                print(f"Текущий текст: {task['title']}")
                new_title = input(
                    f"{NORD_SNOW}Введите новый текст задачи: {RESET}"
                ).strip()
                if new_title:
                    task["title"] = new_title
                    save_tasks(path, tasks)
                    print(f"{NORD_GREEN}Успешно отредактировано!{RESET}")
                else:
                    print(f"{NORD_RED}Текст не может быть пустым.{RESET}")
                found = True
                break
        if not found:
            print(f"{NORD_RED}Запись с таким id не найдена.{RESET}")
    except ValueError:
        print(f"{NORD_RED}Неправильный тип данных (введите число){RESET}")


def delete_task(path, tasks):
    try:
        id_deleted_task = int(
            input(f"{NORD_SNOW}Введите ID задачи, которую вы хотите удалить: {RESET}")
        )
        if not tasks:
            print(f"{NORD_RED}Список пуст{RESET}")
            return

        index_to_delete = None
        for i, task in enumerate(tasks):
            if task["id"] == id_deleted_task:
                index_to_delete = i
                break

        if index_to_delete is not None:
            tasks.pop(index_to_delete)
            for idx, task in enumerate(tasks, start=1):
                task["id"] = idx
            save_tasks(path, tasks)
            print(f"{NORD_GREEN}Успешно удалено!{RESET}")
        else:
            print(f"{NORD_RED}Запись с таким id не найдена.{RESET}")
    except ValueError:
        print(f"{NORD_RED}Неправильный тип данных (введите число){RESET}")


def search_task(tasks):
    part = input(f"{NORD_SNOW}Введите часть задачи для поиска: {RESET}").strip()
    if not tasks:
        print(f"{NORD_RED}Список пуст{RESET}")
        return

    found = False
    for task in tasks:
        if part.lower() in task["title"].lower():
            status = f"{NORD_GREEN}[x]{RESET}" if task["done"] else "[ ]"
            print(f"{task['id']}. {status} {task['title']}")
            found = True
    if not found:
        print(f"{NORD_YELLOW}Ничего не найдено.{RESET}")
