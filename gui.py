import tkinter as tk
from tkinter import ttk

def empty_entry():
    print("your next")
    entry_1.delete(0, tk.END)


def read_table(tree):
    count = 0
    for record in test_data_list:
        if count % 2 == 0:  # even
            tree.insert(parent='', index='end', text='', values=record, tags=('evenrow',))
        else:  # odd
            tree.insert(parent='', index='end', text='', values=record, tags=('oddrow',))
        count += 1


def edit_record(event, tree):
    index_selected = tree.focus()
    values = tree.item(index_selected, 'values')
    entry_1.delete(0, tk.END)
    entry_1.insert(0, values[1])


padx = 8
pady = 4
rowheight = 24
treeview_background = "#000080"
treeview_foreground = "black"
treeview_selected = "#0000FF"
oddrow = "#00FFFF"
evenrow = "#0000FF"


test_data_list = []
test_data_list.append(("1", "hello", 7000))
test_data_list.append(("2", "data!", 3000))
test_data_list.append(("3", "tests", 3000))
test_data_list.append(("4", "users", 8000))
test_data_list.append(("1", "hello", 6000))
test_data_list.append(("2", "data!", 2000))
test_data_list.append(("3", "tests", 1000))
test_data_list.append(("4", "users", 3000))
test_data_list.append(("1", "hello", 4000))
test_data_list.append(("2", "data!", 5000))
test_data_list.append(("3", "tests", 9000))
test_data_list.append(("4", "users", 7000))

main_window = tk.Tk()
main_window.title('my first GUI')
main_window.geometry("900x500")

style = ttk.Style()
style.theme_use('default')
style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, rowheight=rowheight, fieldbackground=treeview_background)
style.map('Treeview', background=[('selected', treeview_selected)])

tree_1_scrollbar = tk.Scrollbar(main_window)
tree_1_scrollbar.grid(row=5, column=6, padx=padx, pady=pady, sticky='ns')
tree_1 = ttk.Treeview(main_window, yscrollcommand=tree_1_scrollbar.set, selectmode="browse")
tree_1.grid(row=5, column=5, padx=0, pady=pady)
tree_1_scrollbar.config(command=tree_1.yview)

tree_1['columns'] = ("col1", "col2", "col3")
tree_1.column("#0", width=0, stretch=tk.NO)
tree_1.column("col1", anchor=tk.E, width=90)
tree_1.column("col2", anchor=tk.W, width=130)
tree_1.column("col3", anchor=tk.W, width=180)

tree_1.heading("#0", text="", anchor=tk.W)
tree_1.heading("col1", text="col1 heading", anchor=tk.CENTER)
tree_1.heading("col2", text="col2 heading", anchor=tk.CENTER)
tree_1.heading("col3", text="col3 heading", anchor=tk.CENTER)

tree_1.tag_configure('oddrow', background=oddrow)
tree_1.tag_configure('evenrow', background=evenrow)

tree_1.bind("<ButtonRelease-1>", lambda event: edit_record(event, tree_1))

frame_1 = tk.LabelFrame(main_window, text="AAAAAAAAAAAAAAA")
frame_1.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

empty_entry_button = tk.Button(main_window, text="yo", command=empty_entry)
empty_entry_button.grid(row=0, column=1, padx=padx, pady=pady)

label_1 = tk.Label(frame_1, text="this world is fake")
label_1.grid(row=2, column=3, padx=padx, pady=pady)

entry_1 = tk.Entry(frame_1, width=24, justify="right")
entry_1.grid(row=1, column=2, padx=padx, pady=pady)
entry_1.insert(0, "This is an entry. Edit me!")

read_table(tree_1)
if __name__ == "__main__":
    main_window.mainloop()
