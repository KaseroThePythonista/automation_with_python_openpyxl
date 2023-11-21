# this is the program to run.


import _main 

task_manager = _main.TasksManager('Developer', 'kasero_the_pythonista.')

print()


while True:

    print('|---------------------------------------------------|')
    print('|                                                   |')
    print('| THIS IS A TO-DO-LIST APP.                         |')
    print('|                                                   |')
    print('| 1. Add a task.                                    |')
    print('| 2. View all task.                                 |')
    print('| 3. Delete all task.                               |')
    print('| 4. Update a task.                                 |')
    print('| 5. Delete a task.                                 |')
    print('| 6. EXIT.                                          |')
    print('|                                                   |')
    print('|---------------------------------------------------|')

    choice = int(input('Choose 1/2/3: '))

    if choice == 1:
        print()
        print('ADD A TASK HERE: ')
        _title = input('1. Title: ')
        _description = input('2. Description: ')
        _dute_date = input('3. date(dd/mm/year): ')

        task_manager.add_task(_title, _description, _dute_date)
        print()

        print('----------DONE-----------')
        print()

    elif choice == 2:
        print()
        print('VIEW ALL TASKS.')
        print()
        print('Bellow are your tasks:')
        print()
        task_manager.view_tasks()
        print()


    elif choice == 3:
        print()
        print('DELETE ALL TASK AVAILABLE.')
        task_manager.delete_task('')
        print()
        print('---------DONE----------')
        print()

    elif choice == 4:
        print()
        print('UPDATE A TASK')
        value1 = input('Enter the task that you wish to update: ')
        task_manager.update_task(value1)
        print()
        print('---------UPDATED SUCCESSFULLY----------')
        print()

    elif choice == 5:
        print()
        print('---------DELETE A TASK-----------')
        print()
        value_del = input('Enter the task to delete: ')
        task_manager.delete_task(value_del)
        print()
        print('----------TASK DELETED------------')

    elif choice == 6:
        print()
        print('---------PROGRAM TERMINATED-----------')
        print()
        break

    else:
        print()
        print('---------INVALID INPUT-----------')
        print()

