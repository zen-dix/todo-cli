import tools as s

path = "tasks.json"
tasks = s.open_json(path)

while True:
    s.menu()
    try:
        num = int(input(f"\n{s.NORD_SNOW}Введите число для выбора: {s.RESET}"))
        if num == 1:
            s.show_tasks(tasks)
            tasks = s.open_json(path)
        elif num == 2:
            s.add_task(path, tasks)
            tasks = s.open_json(path)
        elif num == 3:
            s.complete_task(path, tasks)
            tasks = s.open_json(path)
        elif num == 4:
            s.edit_task(path, tasks)
            tasks = s.open_json(path)
        elif num == 5:
            s.delete_task(path, tasks)
            tasks = s.open_json(path)
        elif num == 6:
            s.search_task(tasks)
            tasks = s.open_json(path)
        elif num == 7:
            print(f"{s.NORD_BLUE}До свидания!{s.RESET}")
            break
        else:
            print(f"{s.NORD_RED}Неверный выбор, попробуйте число от 1 до 7.{s.RESET}")

    except ValueError:
        print(f"{s.NORD_RED}Введите корректное число{s.RESET}")
