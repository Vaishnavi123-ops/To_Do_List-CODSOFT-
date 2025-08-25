task=[]

def add_task():
    value=input("enter your task: ")
    task.append(value)
    print("---success---")
    print("Task is addded")

def view_task():
    if not task:
        print("no task yet")
    else:
        print("---your list---")
        for i, value in enumerate(task,start=1):
            print(f"{i}. {value}")
             

def delete_task():
    delete_index = int(input("enter no to delete:"))
    if 1<=delete_index<=len(task):
        task.pop(delete_index-1)
        print("----success----")
        print("task deleted")
    else:
        print("invalid input.")


def update():
    value=int(input("enter task no to update: "))
    if 1<=value<=len(task):
        new_task=input("enter new text: ")
        task[value-1]=new_task
        print("---success----")
        print("task updated")
    else:
        print("invalid number")



def main():
    while True:
        print("------To-Do List-----")
        print("1.Add task")
        print("2.View task")
        print("3.Delete task")
        print("4.update task")
        print("5.Exit")

        choice=input("Enter choice:")

        if choice=="1":
            add_task()
        elif choice=="2":
            view_task()
        elif choice=="3":
            delete_task()
        elif choice=="4":
            update()
        elif choice=="5":
            print("-------Done---------")
            print("thank you!")
            break
        else:
            print("invalid choice")


if __name__=="__main__":
    main()