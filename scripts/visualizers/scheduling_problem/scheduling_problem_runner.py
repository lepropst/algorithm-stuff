from visualizers.scheduling_problem.scheduling_problem import schedule_tasks


def main():

    # Example Usage
    # tasks = [(1, 3), (2, 5), (2, 6), (4, 5), (5, 8), (5, 7), (7, 8), (7, 9)]
    tasks = [(4, 8), (3, 6), (7, 9), (1, 3), (8, 9), (2, 4)]
    tasks.sort()
    print(f"SORTED TASKS: {"\n".join([f"{index}, {values}" for index, values in enumerate(tasks)])}")
    scheduled_tasks = schedule_tasks(tasks.copy())

    # Print the schedule in a visual format
    print("Machine\tTime")
    print("-" * 40)  # Divider for clarity
    print(scheduled_tasks)
    for i, machine in enumerate(scheduled_tasks):
        machine_name = f"M{i+1}"
        time_slots = []  # Store formatted time slots for this machine
        for start, end in machine:
            time_slots.append(f"{start}-{end}")

        # Align machine name and time slots
        print(f"{machine_name:<8}\t{' | '.join(time_slots)}")

    print("-" * 40)  # Divider to end the visual representation

    # Extract task numbers for each machine
    task_numbers = []
    for machine in scheduled_tasks:
        task_numbers.append([task[0] for task in machine])

    # Print the task numbers
    print("\nTask Numbers on Each Machine:")
    for i, nums in enumerate(task_numbers): 
        print(f"M{i+1}: {' '.join(map(str, [f"{x}" for index, x in enumerate(nums)]))}")
