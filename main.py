# AIM: Task List Manager
# Coder:Khan Ayaan Shakeel
# Date:26/1/26

# Write your code here
tasks = ["Sleep", "Getup", "Brush"]
print(f"Original Tasks: {tasks}")
tasks.append(input())
print(f"Tasks after Adding: {tasks}")
edit_index = int(input())
tasks[edit_index] = input()
print(f"Tasks after Editing: {tasks}")
tasks.pop(0)
print(f"Tasks after Removing: {tasks}")
tasks.sort()
print(f"Tasks after Sorting: {tasks}")
