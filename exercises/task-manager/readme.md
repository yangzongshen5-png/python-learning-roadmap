Python Task Manager
这是一个使用Python开发的命令行任务管理器。用户可以通过终端添加、查看、完成和删除任务。
任务数据会保存在本地的tasks.json文件中。因此，即使关闭程序，下次运行时也可以继续查看之前保存的任务。


项目功能
程序目前支持以下功能：
添加任务
查看任务
程序会显示所有任务的编号、名称和完成状态。
1. Finish assignment - Not completed
2. Review Python - Completed
完成任务
用户输入任务编号后，对应任务的状态会变成Completed。
删除任务
用户可以根据任务编号删除不再需要的任务。
自动保存数据
添加、完成或删除任务后，程序会自动更新tasks.json。
处理部分错误输入
程序可以处理以下情况：
输入不存在的任务编号
输入字母而不是数字
添加空白任务
没有任务时进行查看、完成或删除操作


使用的Python知识
本项目使用了以下Python知识：
变量和数据类型
使用字符串、整数和布尔值保存任务信息和用户选择。
task = {
    "name": "Finish assignment",
    "completed": False
}
列表
使用列表保存所有任务。
tasks = []
字典
每个任务都使用字典保存任务名称和完成状态。
{
    "name": "Review Python"
    "completed": True
}
函数
程序被拆分成多个函数，每个函数负责一个具体功能：
loadTask()       读取任务
saveTasks()      保存任务
showMenu()       显示菜单
addTask()        添加任务
listTasks()      查看任务
completeTask()   完成任务
deleteTask()     删除任务
main()           控制程序运行

条件判断
使用if、elif和else判断用户选择以及任务状态。
循环
使用while循环让程序持续运行，直到用户选择退出。
使用for循环遍历并显示任务。
enumerate()
使用enumerate()为任务生成从1开始的显示编号。
JSON文件
使用Python的json模块读取和保存任务数据。
json.load(file)
json.dump(tasks, file, indent=4)
异常处理
使用try和except处理文件不存在和用户输入错误的情况。
except FileNotFoundError:
    return []
except ValueError:
    print("无效任务编号")
字符串处理
使用strip()删除用户输入前后的空格，避免添加空白任务。





如何运行

运行条件
电脑需要安装Python 3。
可以使用以下命令检查Python是否安装：
python3 --version
下载项目
可以从GitHub下载项目，或者使用Git克隆：
git clone 你的GitHub仓库地址
进入项目文件夹：
cd python-learning-roadmap/task-manager
启动程序
如果文件名是main.py，运行：
python3 main.py
Windows也可能使用：
python main.py
启动后会显示：
===== Task Manager =====
1. Add task
2. List tasks
3. Complete tasks
4. Delete task
5. Exit

输入对应数字即可使用功能。

第一次添加任务后，程序会自动创建tasks.json文件。请不要随意修改或删除该文件，否则保存的任务可能会丢失。

项目文件

task-manager/
├── main.py
├── tasks.json
└── README.md

main.py：程序主要代码
tasks.json：保存任数据
README.md：项目介绍和使用方法



目前存在的问题
菜单只在程序启动时显示一次
用户完成一次操作后，菜单不会再次显示，只会继续要求输入选项。
完成任务后可能显示None
completeTask()成功时只打印结果，没有返回内容，但main()又使用了print(completeTask(tasks))，因此可能额外显示None。
删除任务后编号会变化
目前使用任务在列表中的位置作为编号。删除一个任务后，后面的任务编号会自动改变。
没有永久任务ID
每个任务只有名称和完成状态，没有唯一且固定的ID。
无法修改任务名称
添加任务后只能完成或删除，不能编辑任务内容。
无法恢复已完成任务
任务被标记为完成后，目前不能改回未完成状态。
没有处理损坏的JSON文件
如果tasks.json内容格式错误，程序可能因为JSONDecodeError而停止运行。
可能添加重复任务
程序没有检查任务名称是否已经存在。
缺少自动化测试
当前主要依靠手动运行程序进行测试，还没有使用pytest编写自动化测试。



后续改进计划
操作完成后重新显示菜单
修复额外显示None的问题
为每个任务增加永久ID
增加修改任务功能
增加恢复未完成状态的功能
处理损坏的JSON文件
防止添加重复任务
使用pytest编写自动化测试
为JSON文件增加UTF-8编码支持
将程序拆分成多个Python模块