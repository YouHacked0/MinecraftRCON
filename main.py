from tkinter import *
from tkinter import messagebox
try:
    from mcrcon import MCRcon
except ImportError:
    print("Не установлена библиотека mcrcon. Установка!")
    import os
    os.system("pip install mcrcon")


def connect():
    def connect_():
        global connected
        global mcr
        mcr = MCRcon(str(inp1.get()), str(inp2.get()))
        try:
            mcr.connect()
            messagebox.showinfo("Подключение", "Подключено!")
            status.configure(text="Подключено", fg="green")
            sendcommand()
            connected = True
        except Exception:
            messagebox.showerror("Подключение", "Пароль неверный!")
            connected = False
            status.configure("Не подключено", fg="red")
        login.destroy()
    login = Toplevel(root)
    login.title("Ввод данных")
    login['bg'] = "snow"
    text1 = Label(login, text="IP адрес:")
    text1.grid(column=0, row=0)
    inp1 = Entry(login, width=15)
    inp1.grid(column=1, row=0)
    text2 = Label(login, text="Пароль: ")
    inp2 = Entry(login, width=15)
    text2.grid(column=0, row=1)
    inp2.grid(column=1, row=1)
    btn = Button(login, text="Подключиться", command=connect_)
    btn.grid(column=2, row=1)


def disconnect():
    if connected == True:
        mcr.disconnect()
        status.configure(text="Не подключено", fg="red")
        messagebox.showinfo("Подключение", "Отключено!")


def sendcommand():
    def send():
        resp = mcr.command(str(input1.get()))
        messagebox.showinfo("Ответ от сервера", resp)
    win = Toplevel(root)
    text = Label(win, text="Введите команду без /:")
    input1 = Entry(win, width=10)
    text.grid(column=0, row=0)
    input1.grid(column=1, row=0)
    btn3 = Button(win, text="Отправить", bg="gold2", command=send)
    btn3.grid(column=2, row=0)


root = Tk()
root.title("MinecraftRCON")
connected = False
status_ = Label(root, text="Статус:")
status_.grid(column=0, row=0)
status = Label(root, text="Не подключено", fg="red")
status.grid(column=1, row=0)
btn1 = Button(root, text="Подключиться", command=connect)
btn1.grid(column=0, row=1)
btn2 = Button(root, text="Отключиться", command=disconnect)
btn2.grid(column=0, row=2)
root.mainloop()
