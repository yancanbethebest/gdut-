import copy
import tkinter as tk
from tkinter import ttk

from queue import Queue


class Process:
    def __init__(self, name, arrival_time, burst_time, priority):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.finish_time = 0


# 先来先服务（FCFS）
def FCFS(processes):
    current_time = 0
    total_turnaround_time = 0
    total_weighted_turnaround_time = 0
    processes.sort(key=lambda x: x.arrival_time)
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        current_time += process.burst_time
        process.finish_time = current_time
        turnaround_time = process.finish_time - process.arrival_time
        weighted_turnaround_time = turnaround_time / process.burst_time
        total_turnaround_time += turnaround_time
        total_weighted_turnaround_time += weighted_turnaround_time
        output.insert(tk.END, f"Process {process.name} is running\n")
        output.insert(tk.END, f"Process{process.name} Turnaround Time: {turnaround_time}|\n")
    avg_turnaround_time = total_turnaround_time / len(processes)
    avg_weighted_turnaround_time = total_weighted_turnaround_time / len(processes)
    output.insert(tk.END, f"Average Turnaround Time: {avg_turnaround_time}\n")
    output.insert(tk.END, f"Average Weighted Turnaround Time: {avg_weighted_turnaround_time}\n")


# 简单轮转法（RR）
def RR(processes, time_quantum):
    global turnaround_time
    current_time = 0
    total_turnaround_time = 0
    total_weighted_turnaround_time = 0
    q = Queue()
    for process in processes:
        q.put(process)

    while not q.empty():
        process = q.get()
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        if process.burst_time > time_quantum:
            process.burst_time -= time_quantum
            current_time += time_quantum
            output.insert(tk.END, f"Process {process.name} is running for {time_quantum} units\n")
            q.put(process)
        else:
            current_time += process.burst_time
            process.finish_time = current_time
            turnaround_time = process.finish_time - process.arrival_time
            weighted_turnaround_time = turnaround_time / process.burst_time
            total_turnaround_time += turnaround_time
            total_weighted_turnaround_time += weighted_turnaround_time
            output.insert(tk.END, f"Process {process.name} is running for {process.burst_time} units\n")
        output.insert(tk.END, f"Process{process.name} Turnaround Time: {turnaround_time}|\n")
    avg_turnaround_time = total_turnaround_time / len(processes)
    avg_weighted_turnaround_time = total_weighted_turnaround_time / len(processes)
    output.insert(tk.END, f"Average Turnaround Time: {avg_turnaround_time}\n")
    output.insert(tk.END, f"Average Weighted Turnaround Time: {avg_weighted_turnaround_time}\n")


def SJF(processes):
    current_time = 0
    total_turnaround_time = 0
    total_weighted_turnaround_time = 0
    processes.sort(key=lambda x: x.burst_time)
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        current_time += process.burst_time
        process.finish_time = current_time
        turnaround_time = process.finish_time - process.arrival_time
        weighted_turnaround_time = turnaround_time / process.burst_time
        total_turnaround_time += turnaround_time
        total_weighted_turnaround_time += weighted_turnaround_time
        output.insert(tk.END, f"进程 {process.name} 正在运行\n")
        output.insert(tk.END, f"进程 {process.name} 周转时间: {turnaround_time}\n")
    avg_turnaround_time = total_turnaround_time / len(processes)
    avg_weighted_turnaround_time = total_weighted_turnaround_time / len(processes)
    output.insert(tk.END, f"平均周转时间: {avg_turnaround_time}\n")
    output.insert(tk.END, f"加权平均周转时间: {avg_weighted_turnaround_time}\n")


# 响应比高者优先（HRN）
def HRN(processes):
    current_time = 0
    total_turnaround_time = 0
    total_weighted_turnaround_time = 0
    while processes:
        # 计算每个进程的响应比
        for process in processes:
            waiting_time = current_time - process.arrival_time
            response_ratio = (waiting_time + process.burst_time) / process.burst_time
            process.response_ratio = response_ratio
        # 选择响应比最高的进程
        processes.sort(key=lambda x: x.response_ratio, reverse=True)
        process = processes.pop(0)
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        current_time += process.burst_time
        process.finish_time = current_time
        turnaround_time = process.finish_time - process.arrival_time
        weighted_turnaround_time = turnaround_time / process.burst_time
        total_turnaround_time += turnaround_time
        total_weighted_turnaround_time += weighted_turnaround_time
        output.insert(tk.END, f"进程 {process.name} 正在运行\n")
        output.insert(tk.END, f"进程 {process.name} 周转时间: {turnaround_time}\n")
    avg_turnaround_time = total_turnaround_time / len(processes)
    avg_weighted_turnaround_time = total_weighted_turnaround_time / len(processes)
    output.insert(tk.END, f"平均周转时间: {avg_turnaround_time}\n")
    output.insert(tk.END, f"加权平均周转时间: {avg_weighted_turnaround_time}\n")


# 优先权优先（HPF）
def HPF(processes, output):
    current_time = 0
    total_turnaround_time = 0
    total_weighted_turnaround_time = 0
    processes.sort(key=lambda x: x.priority, reverse=True)  # 根据优先数排序
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        current_time += process.burst_time
        process.finish_time = current_time
        turnaround_time = process.finish_time - process.arrival_time
        weighted_turnaround_time = turnaround_time / process.burst_time
        total_turnaround_time += turnaround_time
        total_weighted_turnaround_time += weighted_turnaround_time
        output.insert(tk.END, f"进程 {process.name} 正在运行\n")
        output.insert(tk.END, f"进程 {process.name} 周转时间: {turnaround_time}\n")
    avg_turnaround_time = total_turnaround_time / len(processes)
    avg_weighted_turnaround_time = total_weighted_turnaround_time / len(processes)
    output.insert(tk.END, f"Average Turnaround Time: {avg_turnaround_time}\n")
    output.insert(tk.END, f"Average Weighted Turnaround Time: {avg_weighted_turnaround_time}\n")


def multilevel_feedback_queue(processes, output, quantum=[4, 2]):
    current_time = 0
    total_turnaround_time = 0
    total_weighted_turnaround_time = 0
    queues = [[] for _ in range(len(quantum))]

    processes.sort(key=lambda x: x.arrival_time)
    queues[0] = [copy.deepcopy(process) for process in processes]  # 使用深拷贝来保存原始的进程信息

    while any(queues):
        for i in range(len(quantum)):
            if queues[i]:
                process = queues[i].pop(0)
                if current_time < process.arrival_time:
                    current_time = process.arrival_time
                execution_time = min(process.burst_time, quantum[i])
                current_time += execution_time
                process.burst_time -= execution_time
                if process.burst_time > 0:
                    if i < len(quantum) - 1:
                        queues[i + 1].append(process)
                else:
                    process.finish_time = current_time
                    turnaround_time = process.finish_time - process.arrival_time
                    original_burst_time = next(
                        p.burst_time for p in processes if p.name == process.name)
                    weighted_turnaround_time = turnaround_time / original_burst_time
                    total_turnaround_time += turnaround_time
                    total_weighted_turnaround_time += weighted_turnaround_time
                    output.insert(tk.END, f"进程 {process.name} 正在运行\n")
                    output.insert(tk.END, f"进程 {process.name} 周转时间: {turnaround_time}\n")

    if len(processes) > 0:
        avg_turnaround_time = total_turnaround_time / len(processes)
        avg_weighted_turnaround_time = total_weighted_turnaround_time / len(processes)
    else:
        avg_turnaround_time = 0
        avg_weighted_turnaround_time = 0

    output.insert(tk.END, f"平均周转时间: {avg_turnaround_time}\n")
    output.insert(tk.END, f"加权平均周转时间: {avg_weighted_turnaround_time}\n")


# 创建主窗口
root = tk.Tk()
root.title("调度算法选择")

# 创建列表，用于存储所有的进程
processes = []

# 创建输入框，用于获取用户输入的进程名、到达时间和服务时间
name_var = tk.StringVar()
arrival_var = tk.StringVar()
burst_var = tk.StringVar()
priority_var = tk.StringVar()

name_entry = tk.Entry(root, textvariable=name_var)
arrival_entry = tk.Entry(root, textvariable=arrival_var)
burst_entry = tk.Entry(root, textvariable=burst_var)
priority_entry = tk.Entry(root, textvariable=priority_var)

name_entry.grid(row=0, column=1)
arrival_entry.grid(row=1, column=1)
burst_entry.grid(row=2, column=1)
priority_entry.grid(row=3, column=1)

# 创建标签，用于指示输入框的用途
name_label = tk.Label(root, text="进程")
arrival_label = tk.Label(root, text="到达时间")
burst_label = tk.Label(root, text="运转时间")
priority_label = tk.Label(root, text="优先数")

name_label.grid(row=0, column=0)
arrival_label.grid(row=1, column=0)
burst_label.grid(row=2, column=0)
priority_label.grid(row=3, column=0)


# 创建按钮，点击按钮时根据输入框的值创建一个进程并添加到列表中
def add_process():
    name = name_var.get()
    arrival_time = int(arrival_var.get())
    burst_time = int(burst_var.get())
    priority = int(priority_var.get())  # 获取优先数
    process = Process(name, arrival_time, burst_time, priority)
    processes.append(process)
    output.insert(tk.END, f"作业名{name} 到达时间{arrival_time} 运转时间{burst_time} 优先数{priority}\n")


add_btn = ttk.Button(root, text="添加进程", command=add_process)
add_btn.grid(column=1, row=5)

# 创建下拉菜单，让用户选择调度算法
combo = ttk.Combobox(root)
combo['values'] = ("FCFS", "RR", "SJF", "HRN", "HPF", "Multilevel_Feedback_Queue")
combo.current(0)  # 设置初始显示值，值为元组['values']的下标
combo.grid(column=0, row=5)


# 创建按钮，点击按钮时根据下拉菜单的值调用相应的函数
def call_func():
    if combo.get() == "FCFS":
        FCFS(processes)
    elif combo.get() == "RR":
        RR(processes, 2)
    elif combo.get() == "SJF":
        SJF(processes)
    elif combo.get() == "HRN":
        HRN(processes)
    elif combo.get() == "HPF":
        HPF(processes, output)
    elif combo.get() == "Multilevel_Feedback_Queue":
        multilevel_feedback_queue(processes, output, quantum=[4, 2])


run_btn = ttk.Button(root, text="运行调度", command=call_func)
run_btn.grid(column=1, row=6)

# 创建文本框，用于显示输出
output = tk.Text(root)
output.grid(row=10, column=0, columnspan=2)

root.mainloop()
