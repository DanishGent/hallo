import tkinter as tk
from tkinter import ttk
import TEST_data as dcd
import TEST_sql as dcsql


padx = 8
pady = 4
rowheight = 24
treeview_background = "#eeeeee"
treeview_foreground = "black"
treeview_selected = "#206030"
oddrow = "#dddddd"
evenrow = "#cccccc"



def read_container_entries():
    return entry_container_id.get(), entry_container_weight.get(), entry_container_destination.get(),


def clear_container_entries():
    entry_container_id.delete(0, tk.END)
    entry_container_weight.delete(0, tk.END)
    entry_container_destination.delete(0, tk.END)
    entry_container_weather.delete(0, tk.END)


def write_container_entries(values):
    entry_container_id.insert(0, values[0])
    entry_container_weight.insert(0, values[1])
    entry_container_destination.insert(0, values[2])


def edit_container(_, tree):
    index_selected = tree.focus()
    values = tree.item(index_selected, 'values')
    clear_container_entries()
    write_container_entries(values)


def read_table(tree, class_):
    count = 0
    result = dcsql.select_all(class_)
    for record in result:
        if record.valid():
            if count % 2 == 0:  #
                tree.insert(parent='', index='end', iid=str(count), text='', values=record.convert_to_tuple(), tags=('evenrow',))
            else:  # odd
                tree.insert(parent='', index='end', iid=str(count), text='', values=record.convert_to_tuple(), tags=('oddrow',))
            count += 1




def refresh_treeview(tree, class_):
    empty_treeview(tree)
    read_table(tree, class_)


def empty_treeview(tree):
    tree.delete(*tree.get_children())




main_window = tk.Tk()
main_window.title('TEST')
main_window.geometry("1200x500")

style = ttk.Style()
style.theme_use('default')


style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, rowheight=rowheight, fieldbackground=treeview_background)
style.map('Treeview', background=[('selected', treeview_selected)])




frame_container = tk.LabelFrame(main_window, text="Hold")
frame_container.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)


tree_frame_container = tk.Frame(frame_container)
tree_frame_container.grid(row=0, column=0, padx=padx, pady=pady)
tree_scroll_container = tk.Scrollbar(tree_frame_container)
tree_scroll_container.grid(row=0, column=1, padx=0, pady=pady, sticky='ns')
tree_container = ttk.Treeview(tree_frame_container, yscrollcommand=tree_scroll_container.set, selectmode="browse")
tree_container.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_container.config(command=tree_container.yview)


tree_container['columns'] = ("id", "Erfaring", "Størrelse")
tree_container.column("#0", width=0, stretch=tk.NO)
tree_container.column("id", anchor=tk.E, width=40)
tree_container.column("Erfaring", anchor=tk.E, width=80)
tree_container.column("Størrelse", anchor=tk.W, width=200)
tree_container.heading("#0", text="", anchor=tk.W)
tree_container.heading("id", text="Id", anchor=tk.CENTER)
tree_container.heading("Erfaring", text="Erfaring", anchor=tk.CENTER)
tree_container.heading("Størrelse", text="Størrelse", anchor=tk.CENTER)
tree_container.tag_configure('oddrow', background=oddrow)
tree_container.tag_configure('evenrow', background=evenrow)
tree_container.bind("<ButtonRelease-1>", lambda event: edit_container(event, tree_container))


controls_frame_container = tk.Frame(frame_container)
controls_frame_container.grid(row=3, column=0, padx=padx, pady=pady)


edit_frame_container = tk.Frame(controls_frame_container)
edit_frame_container.grid(row=0, column=0, padx=padx, pady=pady)

label_container_id = tk.Label(edit_frame_container, text="Id")
label_container_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_container_id = tk.Entry(edit_frame_container, width=4, justify="right")
entry_container_id.grid(row=1, column=0, padx=padx, pady=pady)

label_container_weight = tk.Label(edit_frame_container, text="Erfaring")
label_container_weight.grid(row=0, column=1, padx=padx, pady=pady)
entry_container_weight = tk.Entry(edit_frame_container, width=8, justify="right")
entry_container_weight.grid(row=1, column=1, padx=padx, pady=pady)

label_container_destination = tk.Label(edit_frame_container, text="Størrelse")
label_container_destination.grid(row=0, column=2, padx=padx, pady=pady)
entry_container_destination = tk.Entry(edit_frame_container, width=20)
entry_container_destination.grid(row=1, column=2, padx=padx, pady=pady)


button_frame_container = tk.Frame(controls_frame_container)
button_frame_container.grid(row=1, column=0, padx=padx, pady=pady)

button_create_container = tk.Button(button_frame_container, text="Create")
button_create_container.grid(row=0, column=1, padx=padx, pady=pady)
button_update_container = tk.Button(button_frame_container, text="Update")
button_update_container.grid(row=0, column=2, padx=padx, pady=pady)
button_delete_container = tk.Button(button_frame_container, text="Delete")
button_delete_container.grid(row=0, column=3, padx=padx, pady=pady)

button_clear_boxes = tk.Button(button_frame_container, text="Clear Entry Boxes", command=clear_container_entries)
button_clear_boxes.grid(row=0, column=4, padx=padx, pady=pady)



frame_container = tk.LabelFrame(main_window, text="Bane")
frame_container.grid(row=0, column=1, padx=padx, pady=pady, sticky=tk.N)


tree_frame_container = tk.Frame(frame_container)
tree_frame_container.grid(row=0, column=0, padx=padx, pady=pady)
tree_scroll_container = tk.Scrollbar(tree_frame_container)
tree_scroll_container.grid(row=0, column=1, padx=0, pady=pady, sticky='ns')
tree_container = ttk.Treeview(tree_frame_container, yscrollcommand=tree_scroll_container.set, selectmode="browse")
tree_container.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_container.config(command=tree_container.yview)


tree_container['columns'] = ("id", "Kapacitet", "Sværhedsgrad")
tree_container.column("#0", width=0, stretch=tk.NO)
tree_container.column("id", anchor=tk.E, width=40)
tree_container.column("Kapacitet", anchor=tk.E, width=80)
tree_container.column("Sværhedsgrad", anchor=tk.W, width=200)
tree_container.heading("#0", text="", anchor=tk.W)
tree_container.heading("id", text="Id", anchor=tk.CENTER)
tree_container.heading("Kapacitet", text="Kapacitet", anchor=tk.CENTER)
tree_container.heading("Sværhedsgrad", text="Sværhedsgrad", anchor=tk.CENTER)
tree_container.tag_configure('oddrow', background=oddrow)
tree_container.tag_configure('evenrow', background=evenrow)
tree_container.bind("<ButtonRelease-1>", lambda event: edit_container(event, tree_container))


controls_frame_container = tk.Frame(frame_container)
controls_frame_container.grid(row=3, column=0, padx=padx, pady=pady)


edit_frame_container = tk.Frame(controls_frame_container)
edit_frame_container.grid(row=0, column=0, padx=padx, pady=pady)

label_container_id = tk.Label(edit_frame_container, text="Id")
label_container_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_container_id = tk.Entry(edit_frame_container, width=4, justify="right")
entry_container_id.grid(row=1, column=0, padx=padx, pady=pady)

label_container_weight = tk.Label(edit_frame_container, text="Kapacitet")
label_container_weight.grid(row=0, column=1, padx=padx, pady=pady)
entry_container_weight = tk.Entry(edit_frame_container, width=8, justify="right")
entry_container_weight.grid(row=1, column=1, padx=padx, pady=pady)

label_container_destination = tk.Label(edit_frame_container, text="Sværhedsgrad")
label_container_destination.grid(row=0, column=2, padx=padx, pady=pady)
entry_container_destination = tk.Entry(edit_frame_container, width=20)
entry_container_destination.grid(row=1, column=2, padx=padx, pady=pady)


button_frame_container = tk.Frame(controls_frame_container)
button_frame_container.grid(row=1, column=0, padx=padx, pady=pady)

button_create_container = tk.Button(button_frame_container, text="Create")
button_create_container.grid(row=0, column=1, padx=padx, pady=pady)
button_update_container = tk.Button(button_frame_container, text="Update")
button_update_container.grid(row=0, column=2, padx=padx, pady=pady)
button_delete_container = tk.Button(button_frame_container, text="Delete")
button_delete_container.grid(row=0, column=3, padx=padx, pady=pady)

button_clear_boxes = tk.Button(button_frame_container, text="Clear Entry Boxes", command=clear_container_entries)
button_clear_boxes.grid(row=0, column=4, padx=padx, pady=pady)



frame_container = tk.LabelFrame(main_window, text="Booking")
frame_container.grid(row=0, column=2, padx=padx, pady=pady, sticky=tk.N)


tree_frame_container = tk.Frame(frame_container)
tree_frame_container.grid(row=0, column=0, padx=padx, pady=pady)
tree_scroll_container = tk.Scrollbar(tree_frame_container)
tree_scroll_container.grid(row=0, column=1, padx=0, pady=pady, sticky='ns')
tree_container = ttk.Treeview(tree_frame_container, yscrollcommand=tree_scroll_container.set, selectmode="browse")
tree_container.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_container.config(command=tree_container.yview)


tree_container['columns'] = ("id", "Dato", "HoldId", "BaneID")
tree_container.column("#0", width=0, stretch=tk.NO)
tree_container.column("id", anchor=tk.E, width=40)
tree_container.column("Dato", anchor=tk.E, width=80)
tree_container.column("HoldId", anchor=tk.W, width=200)
tree_container.column("BaneID", anchor=tk.E, width=80)
tree_container.heading("#0", text="", anchor=tk.W)
tree_container.heading("id", text="Id", anchor=tk.CENTER)
tree_container.heading("Dato", text="Dato", anchor=tk.CENTER)
tree_container.heading("HoldId", text="HoldId", anchor=tk.CENTER)
tree_container.heading("BaneID", text="BaneID", anchor=tk.CENTER)
tree_container.tag_configure('oddrow', background=oddrow)
tree_container.tag_configure('evenrow', background=evenrow)
tree_container.bind("<ButtonRelease-1>", lambda event: edit_container(event, tree_container))


controls_frame_container = tk.Frame(frame_container)
controls_frame_container.grid(row=3, column=0, padx=padx, pady=pady)


edit_frame_container = tk.Frame(controls_frame_container)
edit_frame_container.grid(row=0, column=0, padx=padx, pady=pady)

label_container_id = tk.Label(edit_frame_container, text="Id")
label_container_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_container_id = tk.Entry(edit_frame_container, width=4, justify="right")
entry_container_id.grid(row=1, column=0, padx=padx, pady=pady)

label_container_weight = tk.Label(edit_frame_container, text="Dato")
label_container_weight.grid(row=0, column=1, padx=padx, pady=pady)
entry_container_weight = tk.Entry(edit_frame_container, width=8, justify="right")
entry_container_weight.grid(row=1, column=1, padx=padx, pady=pady)

label_container_destination = tk.Label(edit_frame_container, text="HoldId")
label_container_destination.grid(row=0, column=2, padx=padx, pady=pady)
entry_container_destination = tk.Entry(edit_frame_container, width=20)
entry_container_destination.grid(row=1, column=2, padx=padx, pady=pady)

label_container_weather = tk.Label(edit_frame_container, text="BaneID")
label_container_weather.grid(row=0, column=3, padx=padx, pady=pady)
entry_container_weather = tk.Entry(edit_frame_container, width=14)
entry_container_weather.grid(row=1, column=3, padx=padx, pady=pady)


button_frame_container = tk.Frame(controls_frame_container)
button_frame_container.grid(row=1, column=0, padx=padx, pady=pady)

button_create_container = tk.Button(button_frame_container, text="Create")
button_create_container.grid(row=0, column=1, padx=padx, pady=pady)
button_update_container = tk.Button(button_frame_container, text="Update")
button_update_container.grid(row=0, column=2, padx=padx, pady=pady)
button_delete_container = tk.Button(button_frame_container, text="Delete")
button_delete_container.grid(row=0, column=3, padx=padx, pady=pady)

button_clear_boxes = tk.Button(button_frame_container, text="Clear Entry Boxes", command=clear_container_entries)
button_clear_boxes.grid(row=0, column=4, padx=padx, pady=pady)



if __name__ == "__main__":
    refresh_treeview(tree_container, dcd.Container)
    main_window.mainloop()
