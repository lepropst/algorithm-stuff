def schedule_tasks(tasks):
    """
    Schedules tasks on the minimum number of machines using the specified algorithm.

    Args:
        tasks: A list of tuples, where each tuple represents a task (start_time, end_time).

    Returns:
        A list of lists, where each sublist represents the tasks scheduled on a machine.
    """

    m = 0  # Current number of machines
    machines = []  # List to store tasks scheduled on each machine

    while tasks:  # While T is not empty
        # Find the task with the earliest start time and remove it
        earliest_task = min(tasks, key=lambda x: x[0])
        tasks.remove(earliest_task)
        start, end = earliest_task
        found_machine = False
        for j, machine_tasks in enumerate(machines):
            if not any(start < task[1] for task in machine_tasks):
                print("DONT NEED AOTHER MACHINE")
                machines[j].append(earliest_task)
                found_machine = True
                break
        if not found_machine:
            print("NEed another machine")
            m += 1  # Add another machine
            machines.append([(start, end)])  # Schedule task on new machine

        #     if not any(
        #         end <= task[0] for task in machine_tasks
        #     ):  # if the end time is not before the start of any tasks in the machine
        #         machines[j].append((start, end))  # Schedule task on machine j
        #         found_machine = True
        #         break

        # if not found_machine:
        #     m += 1  # Add another machine
        #     machines.append([(start, end)])  # Schedule task on new machine

    return machines
