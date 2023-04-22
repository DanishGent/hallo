import tkinter as tk


def empty_entry():
    print("button_1 was pressed")
    entry_1.delete(0, tk.END)


padx = 8
pady = 4

main_window = tk.Tk()
main_window.title('my first GUI')
main_window.geometry("680x800")


frame_1 = tk.LabelFrame(main_window, text="Container")
frame_1.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)


empty_entry_button = tk.Button(frame_1, text="Create", command=empty_entry)
empty_entry_button.grid(row=2, column=0, padx=padx, pady=pady)


label_1 = tk.Label(frame_1, text="id")
label_1.grid(row=0, column=0, padx=padx, pady=pady)


entry_1 = tk.Entry(frame_1, width=24, justify="right")
entry_1.grid(row=1, column=0, padx=padx, pady=pady)
entry_1.insert(0, "")

empty_entry_button = tk.Button(frame_1, text="Update", command=empty_entry)
empty_entry_button.grid(row=2, column=1, padx=padx, pady=pady)


label_1 = tk.Label(frame_1, text="Weight")
label_1.grid(row=0, column=1, padx=padx, pady=pady)


entry_1 = tk.Entry(frame_1, width=24, justify="right")
entry_1.grid(row=1, column=1, padx=padx, pady=pady)
entry_1.insert(0, "")

empty_entry_button = tk.Button(frame_1, text="Delete", command=empty_entry)
empty_entry_button.grid(row=2, column=2, padx=padx, pady=pady)


label_1 = tk.Label(frame_1, text="Destination")
label_1.grid(row=0, column=2, padx=padx, pady=pady)


entry_1 = tk.Entry(frame_1, width=24, justify="right")
entry_1.grid(row=1, column=2, padx=padx, pady=pady)
entry_1.insert(0, "")

empty_entry_button = tk.Button(frame_1, text="Clear Entry Boxes", command=empty_entry)
empty_entry_button.grid(row=2, column=3, padx=padx, pady=pady)


label_1 = tk.Label(frame_1, text="Weather")
label_1.grid(row=0, column=3, padx=padx, pady=pady)


entry_1 = tk.Entry(frame_1, width=24, justify="right")
entry_1.grid(row=1, column=3, padx=padx, pady=pady)
entry_1.insert(0, "")

if __name__ == "__main__":
    main_window.mainloop()
