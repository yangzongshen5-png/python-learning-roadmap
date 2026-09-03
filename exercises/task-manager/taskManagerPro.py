def showMenu():
    print("===== Task Manager =====")
    print("1. Add task")
    print("2. List tasks")
    print("3. Delete task")
    print("4. Exit")

def addTask(tasks):
    task = input("New task: ").strip()
    if task:
        tasks.append(task)
        print("任务已添加")
    else:
        print("请输入有效任务")

def listTasks(tasks):
    if not tasks:
        print("暂无任务")
    else:
        for numbers,task in enumerate(tasks,start=1):
            print(f"{numbers}.{task}")
        return
def deleteTask(tasks):
    if not tasks:
        return "暂无任务可删除"
    listTasks(tasks)
    try:
        x = int(input("请输入想要删除任务的编号： "))
        if x<1 or x>len(tasks):
            return "请输入有效任务编号!"
        tasks.pop(x-1)
        return f"已删除第{x}个任务"
    except ValueError:
        return("无效任务编号")
def main():
    tasks = []
    showMenu()
    while True:
        choice = (input("请输入菜单选项： "))
        if choice =="1":
            addTask(tasks)
        elif choice =="2":
            listTasks(tasks)
        elif choice =="3":
            print(deleteTask(tasks))
        elif choice =="4":
            print("已退出")
            break
        else:
            print("无效选择")

if __name__ =="__main__":
    main()


