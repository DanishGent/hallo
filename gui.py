import tkinter as tk


def empty_entry():
    entry_1.delete(0, tk.END)


padx = 8
pady = 4

main_window = tk.Tk()
main_window.title('my first GUI')
main_window.geometry("500x500")


frame_1 = tk.LabelFrame(main_window, text="this world is fake")
frame_1.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)


empty_entry_button = tk.Button(main_window, text="button", command=empty_entry)
empty_entry_button.grid(row=0, column=1, padx=padx, pady=pady)


label_1 = tk.Label(frame_1, text="yo")
label_1.grid(row=2, column=3, padx=padx, pady=pady)


entry_1 = tk.Entry(frame_1, width=24, justify="right")
entry_1.grid(row=1, column=2, padx=padx, pady=pady)
entry_1.insert(0, "This is an entry. Edit me!")


if __name__ == "__main__":
    main_window.mainloop()
