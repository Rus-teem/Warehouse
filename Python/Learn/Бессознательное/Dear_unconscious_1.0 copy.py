import random
import tkinter as tk
from tkinter import messagebox

# Функция для генерации готовности бессознательного
def unconscious_ready():
    return random.choice(["Да", "Нет"])

# Функция, которая отвечает на вопрос пользователя
def unconscious_answer():
    return random.choice([
        "Да", "Нет", "Попробуй позже", "Не сейчас",
        "Ответ скрыт", "Это важно для тебя", "Доверься интуиции"
    ])


# Собственная функция запроса строки, чтобы обеспечить видимый Entry
def ask_question():
    dialog = tk.Toplevel(root)
    dialog.configure(bg=root.cget('bg'))
    dialog.title("Вопрос")
    dialog.transient(root)
    dialog.grab_set()
    tk.Label(dialog, text="Задай свой вопрос:", fg='white', bg=dialog.cget('bg')).pack(padx=10, pady=10)
    entry = tk.Entry(dialog, fg='black', bg='white', insertbackground='black')
    entry.pack(padx=10)
    entry.focus_set()
    result = []
    def on_ok():
        result.append(entry.get())
        dialog.destroy()
    def on_cancel():
        dialog.destroy()
    btn_frame = tk.Frame(dialog, bg=dialog.cget('bg'))
    btn_frame.pack(pady=10)
    tk.Button(btn_frame, text="OK", command=on_ok).pack(side=tk.LEFT, padx=5)
    tk.Button(btn_frame, text="Cancel", command=on_cancel).pack(side=tk.LEFT, padx=5)
    root.wait_window(dialog)
    return result[0] if result else None

# Создаем графический интерфейс
def start_dialog():
    readiness = unconscious_ready()
    if readiness == "Да":
        question = ask_question()
        if question:
            answer = unconscious_answer()
            messagebox.showinfo("Ответ бессознательного", answer)
    else:
        wait_minutes = random.randint(1, 3)
        messagebox.showinfo("Ожидание", f"Бессознательное не готово. Следующая попытка через {wait_minutes} минут.")
        root.after(wait_minutes * 60000, start_dialog)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Диалог с бессознательным")
    # Текстовая метка с инструкцией
    label = tk.Label(root, text="Нажмите 'Начать сеанс', чтобы начать диалог с бессознательным.")
    label.pack(pady=(10, 0))
    # Настраиваем палитру для видимости текста в диалогах
    bg = root.cget('bg'); root.tk_setPalette(background=bg, foreground='black')
    start_button = tk.Button(root, text="Начать сеанс", command=start_dialog)
    start_button.pack(padx=20, pady=20)
    exit_button = tk.Button(root, text="Выход", command=root.destroy)
    exit_button.pack(padx=20, pady=(0,20))

    root.mainloop()
