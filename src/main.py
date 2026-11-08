tasks = []
print("Программа «Планировщик задач")
while True:
    choice = input("Выберите действие (1-3): ").strip()
    if choice == "1":
        print("\n Добавление задачи")
        title = input("Название: ")
        deadline = input("Дедлайн: ")
        priorit = int(input("Приоритет: "))
        new_task = {
            "title": title,
            "deadline": deadline,
            "priority": priorit}
        tasks.append(new_task)
        print("Задача добавлена")
    elif choice == "2":
        print("\n Список задач")
        if not tasks:
            print("Задач нет")
        else:
            sorted_tasks = sorted(tasks, key=lambda x: x["priority"])
            for task in sorted_tasks:
                print(f"Приоритет: {task['priority']} | {task['title']} (До: {task['deadline']})")
    elif choice == "3":
        print("Завершение работы")
        break
    else:
        print("Ошибка")