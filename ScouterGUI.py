import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from tests.benchmark import benchmark
from tests.cpu_test import cpu_test 
from tests.mem_test import mem_test
from tests.disk_test import disk_test

WIDTH = 600
HEIGHT = 450

app = tk.Tk()
app.title('Scouter')
app.geometry(f'{WIDTH}x{HEIGHT}')

bg_1 = Image.open('assets/bg1.png')
bg_1 = bg_1.resize((WIDTH, HEIGHT))
bg_1 = ImageTk.PhotoImage(bg_1)

bg_2 = Image.open('assets/bg2.png')
bg_2 = bg_2.resize((WIDTH, HEIGHT))
bg_2 = ImageTk.PhotoImage(bg_2)

bg = tk.Label(app, image=bg_1)
bg.place(x=0, y=0)

cpu_label = tk.Label(app, text='cpu : ####', font=('monofur for Powerline', 16))
cpu_label.place(x=20, y=20)
mem_label = tk.Label(app, text='mem : ####', font=('monofur for Powerline', 16))
mem_label.place(x=20, y=60)
disk_label = tk.Label(app, text='disk : ####', font=('monofur for Powerline', 16))
disk_label.place(x=20, y=100)
avg_label = tk.Label(app, text='avg. : ####', font=('monofur for Powerline', 16))
avg_label.place(x=20, y=140)
vegeta_dialog = tk.Label(app, text='', font=('monofur for Powerline', 36))
vegeta_dialog.place(x=80, y=350)

s = ttk.Style()
s.theme_use('classic')
s.configure("green.Horizontal.TProgressbar", foreground='green', background='green')
progress_bar = ttk.Progressbar(style='green.Horizontal.TProgressbar')
progress_bar.pack(side='bottom', fill='x')
    
def start():
    # reset progress bar and background
    bg.config(image=bg_1)
    progress_bar['value'] = 0
    cpu_label.config(text='cpu : loading..')
    mem_label.config(text='mem : loading..')
    disk_label.config(text='disk : loading..')
    avg_label.config(text='avg. : loading..')
    vegeta_dialog.config(text='Wait!??')
    app.update_idletasks()

    cpu_score = benchmark(func=cpu_test, n_warm_up=1, n_test=3)
    progress_bar['value'] = 33
    cpu_label.config(text=f'cpu : {cpu_score:.0f} %')
    vegeta_dialog.config(text='What, Really!??')
    app.update_idletasks()

    mem_score = benchmark(func=mem_test, n_warm_up=1, n_test=3)
    progress_bar['value'] = 66
    mem_label.config(text=f'mem : {mem_score:.0f} %')
    vegeta_dialog.config(text='Naniiiiiii!!')
    app.update_idletasks()

    disk_score = benchmark(func=disk_test, n_warm_up=1, n_test=3)
    progress_bar['value'] = 99
    disk_label.config(text=f'disk : {disk_score:.0f} %')
    app.update_idletasks()

    avg_score = (cpu_score + mem_score + disk_score) / 3
    avg_label.config(text=f'avg. : {avg_score:.0f} %')
    vegeta_dialog.config(text=f"It's over {avg_score:.0f} % !!!")
    bg.config(image=bg_2)

start_button = tk.Button(app, text='Run Benchmark', command=start, font=('monofur for Powerline', 16))
start_button.place(x=455, y=395)

app.mainloop()