import tkinter as tk

from Setup import Constants as c


def new_person():
    np_window: tk.Tk = tk.Tk()
    np_window.title("Create New Person")
    np_window.geometry(f"{c.NEW_PERS_WINDOW_SIZE[0]}x{c.NEW_PERS_WINDOW_SIZE[1]}")

    gender = tk.StringVar(np_window)
    gender.set("Select gender")  # default value

    tk.Label(np_window, text='First Name:', padx=10, pady=5).grid(row=0)
    tk.Label(np_window, text='Last Name:', padx=10, pady=5).grid(row=1)
    tk.Label(np_window, text='Gender:', padx=10, pady=10).grid(row=2)

    first_name_entry = tk.Entry(np_window)
    last_name_entry = tk.Entry(np_window)
    gender_dropdown = tk.OptionMenu(np_window, gender, "Male", "Female")  # , "Other")
    submit_button = tk.Button(
        np_window,
        text="Create",
        command=lambda: __enter(
            np_window,
            first_name_entry,
            last_name_entry,
            gender
        )
    )

    first_name_entry.grid(row=0, column=1)
    last_name_entry.grid(row=1, column=1)
    gender_dropdown.grid(row=2, column=1)
    gender_dropdown.config(width=10)
    submit_button.grid(row=3, column=1)

    first_name_entry.bind(
        '<KeyRelease>',
        lambda event: __check_conditions(
            submit_button,
            first_name_entry,
            last_name_entry,
            gender
        )
    )

    np_window.mainloop()


def __enter(np_window, first_name_entry, last_name_entry, gender_text):
    return first_name_entry.get(), last_name_entry.get(), gender_text.get()


def __check_conditions(submit_button, first_name_entry, last_name_entry, gender_text):
    # Check if the textbox is not empty and an item is selected in the dropdown
    if first_name_entry.get() and last_name_entry.get() and gender_text.get() != "Select gender":
        submit_button.config(state=tk.NORMAL)
    else:
        submit_button.config(state=tk.DISABLED)
