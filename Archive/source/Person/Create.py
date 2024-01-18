import tkinter as tk
from typing import Literal

from Setup import Constants as c


def new_person(window, callback) -> dict[Literal['first_name', 'last_name', 'gender'], str]:
    # Shared variable to hold the data
    person_data: dict[Literal['first_name', 'last_name', 'gender'], str] = \
        {'first_name': '', 'last_name': '', 'gender': ''}

    def on_submit():
        # Update the shared variable with the latest values
        person_data['first_name']: str = first_name_entry.get()
        person_data['last_name']: str = last_name_entry.get()
        person_data['gender']: str = gender.get()
        callback(person_data)  # Use the callback to return data
        np_window.destroy()

    def __check_conditions(*args):
        # Check if the textbox is not empty and an item is selected in the dropdown
        if first_name_entry.get() and last_name_entry.get() and gender.get() != "Select gender":
            submit_button.config(state=tk.NORMAL)
        else:
            submit_button.config(state=tk.DISABLED)

    np_window: tk.Toplevel = tk.Toplevel(window)
    np_window.title("Create New Person")
    np_window.geometry(f"{c.NEW_PERS_WINDOW_SIZE[0]}x{c.NEW_PERS_WINDOW_SIZE[1]}")

    gender: tk.StringVar = tk.StringVar(np_window)
    gender.set("Select gender")  # default value
    gender.trace("w", __check_conditions)  # Call __check_conditions when gender changes

    tk.Label(np_window, text='First Name:', padx=10, pady=5).grid(row=0)
    tk.Label(np_window, text='Last Name:', padx=10, pady=5).grid(row=1)
    tk.Label(np_window, text='Gender:', padx=10, pady=10).grid(row=2)

    first_name_entry: tk.Entry = tk.Entry(np_window)
    last_name_entry: tk.Entry = tk.Entry(np_window)
    gender_dropdown: tk.OptionMenu = \
        tk.OptionMenu(np_window, gender, "Male", "Female")  # , "Other")

    submit_button: tk.Button = tk.Button(np_window, text="Create", command=on_submit, state=tk.DISABLED)

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

    # Return the collected data after the window is closed
    return person_data
