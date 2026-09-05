import json
def loadTask():
     try:
          with open ("tasks.json","r") as file:
               return json.load(file)
     except FileNotFoundError:
          return []
def saveTasks(tasks):
     with open("tasks.json","w") as file:
          json.dump(tasks,file,indent=4)
def showMenu():
    print("===== Task Manager =====")
    print("1. Add task")
    print("2. List tasks")
    print("3. Complete tasks")
    print("4. Delete task")
    print("5. Exit")

def addTask(tasks):
    task = input("New task: ").strip()
    if task:
        newTask = {"name":task,
                   "completed":False
        }
        tasks.append(newTask)
        saveTasks(tasks)
        print("任务已添加")
    else:
        print("请输入有效任务")

def listTasks(tasks):
    if not tasks:
        print("暂无任务")
    else:
        for numbers,task in enumerate(tasks,start=1):
            if task["completed"]:
                status = "Completed"
            else:
                status = "Not completed"
            print(f"{numbers}.{task['name']} - {status}")
        return
def completeTask(tasks):
    if not tasks:
        print("暂无任务")
        return
    listTasks(tasks)
    try:
        x = int(input("请输入已完成任务的编号： "))
        if x<1 or x>len(tasks):
                    return "请输入有效任务编号!"
        tasks[x-1]["completed"]=True
        saveTasks(tasks)
        print(f"第{x}个任务已完成")
    except ValueError:
            return("无效任务编号")
def deleteTask(tasks):
    if not tasks:
        return "暂无任务可删除"
    listTasks(tasks)
    try:
        x = int(input("请输入想要删除任务的编号： "))
        if x<1 or x>len(tasks):
            return "请输入有效任务编号!"
        tasks.pop(x-1)
        saveTasks(tasks)
        return f"已删除第{x}个任务"
    except ValueError:
        return("无效任务编号")
def main():
    tasks = loadTask()
    showMenu()
    while True:
        choice = (input("请输入菜单选项： "))
        if choice =="1":
            addTask(tasks)
        elif choice =="2":
            listTasks(tasks)
        elif choice =="3":
                    print(completeTask(tasks))
        elif choice =="4":
            print(deleteTask(tasks))
        elif choice =="5":
            print("已退出")
            break
        else:
            print("无效选择")

if __name__ =="__main__":
    main()


