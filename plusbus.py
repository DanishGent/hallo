import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import plusbus_data as dcd
import plusbus_sql as dcsql
import plusbus_func as dcf


padx = 8
pady = 4
rowheight = 24
treeview_background = "#eeeeee"
treeview_foreground = "black"
treeview_selected = "#206030"
oddrow = "#dddddd"
evenrow = "#cccccc"


# region container functions
def read_container_entries():  # Read content of entry boxes
    return entry_container_id.get(), entry_container_weight.get(), entry_container_destination.get(),


def clear_container_entries():  # Clear entry boxes
    entry_container_id.delete(0, tk.END)  # Delete text in entry box, beginning with the first character (0) and ending with the last character (tk.END)
    entry_container_weight.delete(0, tk.END)
    entry_container_destination.delete(0, tk.END)



def write_container_entries(values):  # Fill entry boxes
    entry_container_id.insert(0, values[0])
    entry_container_weight.insert(0, values[1])
    entry_container_destination.insert(0, values[2])


def edit_container(_, tree):  # Copy selected tuple into entry boxes. First parameter is mandatory but we don't use it.
    index_selected = tree.focus()  # Index of selected tuple
    values = tree.item(index_selected, 'values')  # Values of selected tuple
    clear_container_entries()  # Clear entry boxes
    write_container_entries(values)  # Fill entry boxes


def create_container(tree, record):  # add new tuple to database
    container = dcd.Container.convert_from_tuple(record)  # Convert tuple to Container
    dcsql.create_record(container)  # Update database
    clear_container_entries()  # Clear entry boxes
    refresh_treeview(tree, dcd.Container)  # Refresh treeview table


def update_container(tree, record):  # update tuple in database
    container = dcd.Container.convert_from_tuple(record)  # Convert tuple to Container
    dcsql.update_container(container)  # Update database
    clear_container_entries()  # Clear entry boxes
    refresh_treeview(tree, dcd.Container)  # Refresh treeview table


def delete_container(tree, record):  # delete tuple in database
    container = dcd.Container.convert_from_tuple(record)  # Convert tuple to Container
    dcsql.delete_soft_container(container)  # Update database
    clear_container_entries()  # Clear entry boxes
    refresh_treeview(tree, dcd.Container)  # Refresh treeview table


# def copy_container_id(event):  #
#     entry_transport_container_id.delete(0, tk.END)
#     entry_transport_container_id.insert(0, entry_container_id.get())
# endregion container functions


# region aircraft functions
def read_aircraft_entries():  # Read content of entry boxes
    return entry_aircraft_id.get(), entry_aircraft_max_cargo_weight.get(), entry_aircraft_registration.get(),


def clear_aircraft_entries():  # Clear entry boxes
    entry_aircraft_id.delete(0, tk.END)  # Delete text in entry box, beginning with the first character (0) and ending with the last character (tk.END)
    entry_aircraft_max_cargo_weight.delete(0, tk.END)
    entry_aircraft_registration.delete(0, tk.END)


def write_aircraft_entries(values):  # Fill entry boxes
    entry_aircraft_id.insert(0, values[0])
    entry_aircraft_max_cargo_weight.insert(0, values[1])
    entry_aircraft_registration.insert(0, values[2])


def edit_aircraft(_, tree):  # Copy selected tuple into entry boxes. First parameter is mandatory but we don't use it.
    index_selected = tree.focus()  # Index of selected tuple
    values = tree.item(index_selected, 'values')  # Values of selected tuple
    clear_aircraft_entries()  # Clear entry boxes
    write_aircraft_entries(values)  # Fill entry boxes


def create_aircraft(tree, record):  # add new tuple to database
    aircraft = dcd.Aircraft.convert_from_tuple(record)  # Convert tuple to Aircraft
    dcsql.create_record(aircraft)  # Update database
    clear_aircraft_entries()  # Clear entry boxes
    refresh_treeview(tree, dcd.Aircraft)  # Refresh treeview table


def update_aircraft(tree, record):  # update tuple in database
    aircraft = dcd.Aircraft.convert_from_tuple(record)  # Convert tuple to Aircraft
    dcsql.update_aircraft(aircraft)  # Update database
    clear_aircraft_entries()  # Clear entry boxes
    refresh_treeview(tree, dcd.Aircraft)  # Refresh treeview table


def delete_aircraft(tree, record):  # delete tuple in database
    aircraft = dcd.Aircraft.convert_from_tuple(record)  # Convert tuple to Aircraft
    dcsql.delete_soft_aircraft(aircraft)  # Update database
    clear_aircraft_entries()  # Clear entry boxes
    refresh_treeview(tree, dcd.Aircraft)  # Refresh treeview table


# def copy_aircraft_id(event):
#     entry_transport_aircraft_id.delete(0, tk.END)
#     entry_transport_aircraft_id.insert(0, entry_aircraft_id.get())
# endregion aircraft functions


# region transport functions
def read_transport_entries():  # Read content of entry boxes
    return entry_transport_id.get(), entry_transport_date.get(), entry_transport_container_id.get(),


def clear_transport_entries():  # Clear entry boxes
    entry_transport_id.delete(0, tk.END)  # Delete text in entry box, beginning with the first character (0) and ending with the last character (tk.END)
    entry_transport_date.delete(0, tk.END)
    entry_transport_container_id.delete(0, tk.END)
    entry_transport_aircraft_id.delete(0, tk.END)


def write_transport_entries(values):  # Fill entry boxes
    entry_transport_id.insert(0, values[0])
    entry_transport_date.insert(0, values[1])
    entry_transport_container_id.insert(0, values[2])
    entry_transport_aircraft_id.insert(0, values[3])


def edit_transport(_, tree):  # Copy selected tuple into entry boxes. First parameter is mandatory but we don't use it.
    index_selected = tree.focus()  # Index of selected tuple
    values = tree.item(index_selected, 'values')  # Values of selected tuple
    clear_transport_entries()  # Clear entry
    # boxes
    write_transport_entries(values)  # Fill entry boxes


def create_transport(tree, record):  # add new tuple to database
    transport = dcd.Transport.convert_from_tuple(record)  # Convert tuple to Transport
    capacity_ok = dcf.capacity_available(dcsql.get_record(dcd.Aircraft, transport.aircraft_id), transport.date, dcsql.get_record(dcd.Container, transport.container_id))
    destination_ok = dcf.max_one_destination(dcsql.get_record(dcd.Aircraft, transport.aircraft_id), transport.date, dcsql.get_record(dcd.Container, transport.container_id))
    if destination_ok:
        if capacity_ok:
            dcsql.create_record(transport)  # Update database
            clear_transport_entries()  # Clear entry boxes
            refresh_treeview(tree, dcd.Transport)  # Refresh treeview table
        else:
            # global INTERNAL_ERROR_CODE
            # INTERNAL_ERROR_CODE = 1
            messagebox.showwarning("", "Not enough room on bus!")
    else:
        messagebox.showwarning("", "bus already has another destination!")


def update_transport(tree, record):  # update tuple in database
    transport = dcd.Transport.convert_from_tuple(record)  # Convert tuple to Transport
    capacity_ok = dcf.capacity_available(dcsql.get_record(dcd.Aircraft, transport.aircraft_id), transport.date, dcsql.get_record(dcd.Container, transport.container_id))
    destination_ok = dcf.max_one_destination(dcsql.get_record(dcd.Aircraft, transport.aircraft_id), transport.date, dcsql.get_record(dcd.Container, transport.container_id))
    if destination_ok:
        if capacity_ok:
            dcsql.update_transport(transport)  # Update database
            clear_transport_entries()  # Clear entry boxes
            refresh_treeview(tree, dcd.Transport)  # Refresh treeview table
        else:
            # global INTERNAL_ERROR_CODE
            # INTERNAL_ERROR_CODE = 1
            messagebox.showwarning("", "Not enough room on bus!")
    else:
        messagebox.showwarning("", "bus already has another destination!")


def delete_transport(tree, record):  # delete tuple in database
    transport = dcd.Transport.convert_from_tuple(record)  # Convert tuple to Transport
    dcsql.delete_hard_transport(transport)  # Update database
    clear_transport_entries()  # Clear entry boxes
    refresh_treeview(tree, dcd.Transport)  # Refresh treeview table
# endregion transport functions


# region common functions
def read_table(tree, class_):  # fill tree from database
    count = 0  # Used to keep track of odd and even rows, because these will be colored differently.
    result = dcsql.select_all(class_)  # Read all containers from database
    for record in result:
        if record.valid():  # this condition excludes soft deleted records from being shown in the data table
            if count % 2 == 0:  # even
                tree.insert(parent='', index='end', iid=str(count), text='', values=record.convert_to_tuple(), tags=('evenrow',))  # Insert one row into the data table
            else:  # odd
                tree.insert(parent='', index='end', iid=str(count), text='', values=record.convert_to_tuple(), tags=('oddrow',))  # Insert one row into the data table
            count += 1


def refresh_treeview(tree, class_):  # Refresh treeview table
    empty_treeview(tree)  # Clear treeview table
    read_table(tree, class_)  # Fill treeview from database


def empty_treeview(tree):  # Clear treeview table
    tree.delete(*tree.get_children())
# endregion common functions


# region common widgets
main_window = tk.Tk()  # Define the main window
main_window.title('plusbus Gent')  # Text shown in the top window bar
main_window.geometry("1200x500")  # window size

style = ttk.Style()  # Add style
style.theme_use('default')  # Pick theme

# Configure treeview colors and formatting. A treeview is an object that can contain a data table.
style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, rowheight=rowheight, fieldbackground=treeview_background)
style.map('Treeview', background=[('selected', treeview_selected)])  # Define color of selected row in treeview
# endregion common widgets


# region container widgets
# Define Labelframe which contains all container related GUI objects (data table, labels, buttons, ...)
frame_container = tk.LabelFrame(main_window, text="kunder")  # https://www.tutorialspoint.com/python/tk_labelframe.htm
frame_container.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)  # https://www.tutorialspoint.com/python/tk_grid.htm

# Define data table (Treeview) and its scrollbar. Put them in a Frame.
tree_frame_container = tk.Frame(frame_container)  # https://www.tutorialspoint.com/python/tk_frame.htm
tree_frame_container.grid(row=0, column=0, padx=padx, pady=pady)
tree_scroll_container = tk.Scrollbar(tree_frame_container)
tree_scroll_container.grid(row=0, column=1, padx=0, pady=pady, sticky='ns')
tree_container = ttk.Treeview(tree_frame_container, yscrollcommand=tree_scroll_container.set, selectmode="browse")  # https://docs.python.org/3/library/tkinter.ttk.html#treeview
tree_container.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_container.config(command=tree_container.yview)

# Define the data table's formatting and content
tree_container['columns'] = ("kund nummer", "tf", "E-mail")  # Define columns
tree_container.column("#0", width=0, stretch=tk.NO)  # Format columns. Suppress the irritating first empty column.
tree_container.column("kund nummer", anchor=tk.E, width=80)
tree_container.column("tf", anchor=tk.E, width=70)  # "E" stands for East, meaning Right. Possible anchors are N, NE, E, SE, S, SW, W, NW and CENTER
tree_container.column("E-mail", anchor=tk.E, width=150)
tree_container.heading("#0", text="", anchor=tk.W)  # Create column headings
tree_container.heading("kund nummer", text="kund nummer", anchor=tk.CENTER)
tree_container.heading("tf", text="tf", anchor=tk.CENTER)
tree_container.heading("E-mail", text="E-mail", anchor=tk.CENTER)
tree_container.tag_configure('oddrow', background=oddrow)  # Create tags for rows in 2 different colors
tree_container.tag_configure('evenrow', background=evenrow)

tree_container.bind("<ButtonRelease-1>", lambda event: edit_container(event, tree_container))  # Define function to be called, when an item is selected.
# tree_container.bind("<Double-Button-1>", copy_container_id)  # Define function to be called after double click.

# Define Frame which contains labels, entries and buttons
controls_frame_container = tk.Frame(frame_container)
controls_frame_container.grid(row=3, column=0, padx=padx, pady=pady)

# Define Frame which contains labels (text fields) and entries (input fields)
edit_frame_container = tk.Frame(controls_frame_container)  # Add tuple entry boxes
edit_frame_container.grid(row=0, column=0, padx=padx, pady=pady)
# label and entry for container id
label_container_id = tk.Label(edit_frame_container, text="kund nummer")  # https://www.tutorialspoint.com/python/tk_label.htm
label_container_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_container_id = tk.Entry(edit_frame_container, width=4, justify="right")  # https://www.tutorialspoint.com/python/tk_entry.htm
entry_container_id.grid(row=1, column=0, padx=padx, pady=pady)
# label and entry for container weight
label_container_weight = tk.Label(edit_frame_container, text="tf")
label_container_weight.grid(row=0, column=1, padx=padx, pady=pady)
entry_container_weight = tk.Entry(edit_frame_container, width=8, justify="right")
entry_container_weight.grid(row=1, column=1, padx=padx, pady=pady)
# label and entry for container destination
label_container_destination = tk.Label(edit_frame_container, text="E-mail")
label_container_destination.grid(row=0, column=2, padx=padx, pady=pady)
entry_container_destination = tk.Entry(edit_frame_container, width=20)
entry_container_destination.grid(row=1, column=2, padx=padx, pady=pady)


# Define Frame which contains buttons
button_frame_container = tk.Frame(controls_frame_container)
button_frame_container.grid(row=1, column=0, padx=padx, pady=pady)
# Define buttons
button_create_container = tk.Button(button_frame_container, text="Create", command=lambda: create_container(tree_container, read_container_entries()))
button_create_container.grid(row=0, column=1, padx=padx, pady=pady)
button_update_container = tk.Button(button_frame_container, text="Update", command=lambda: update_container(tree_container, read_container_entries()))
button_update_container.grid(row=0, column=2, padx=padx, pady=pady)
button_delete_container = tk.Button(button_frame_container, text="Delete", command=lambda: delete_container(tree_container, read_container_entries()))
button_delete_container.grid(row=0, column=3, padx=padx, pady=pady)
button_clear_boxes = tk.Button(button_frame_container, text="Clear Entry Boxes", command=clear_container_entries)
button_clear_boxes.grid(row=0, column=4, padx=padx, pady=pady)
# endregion container widgets


# region aircraft widgets
# Define Labelframe which contains all aircraft related GUI objects (data table, labels, buttons, ...)
frame_aircraft = tk.LabelFrame(main_window, text="bookinger")  # https://www.tutorialspoint.com/python/tk_labelframe.htm
frame_aircraft.grid(row=0, column=1, padx=padx, pady=pady, sticky=tk.N)  # https://www.tutorialspoint.com/python/tk_grid.htm

# Define data table (Treeview) and its scrollbar. Put them in a Frame.
tree_frame_aircraft = tk.Frame(frame_aircraft)  # https://www.tutorialspoint.com/python/tk_frame.htm
tree_frame_aircraft.grid(row=0, column=0, padx=padx, pady=pady)
tree_scroll_aircraft = tk.Scrollbar(tree_frame_aircraft)
tree_scroll_aircraft.grid(row=0, column=1, padx=0, pady=pady, sticky='ns')
tree_aircraft = ttk.Treeview(tree_frame_aircraft, yscrollcommand=tree_scroll_aircraft.set, selectmode="browse")  # https://docs.python.org/3/library/tkinter.ttk.html#treeview
tree_aircraft.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_aircraft.config(command=tree_aircraft.yview)

# Define the data table's formatting and content
tree_aircraft['columns'] = ("Kunde Id", "Pladser", "Rejse Id")  # Define columns
tree_aircraft.column("#0", width=0, stretch=tk.NO)  # Format columns. Suppress the irritating first empty column.
tree_aircraft.column("Kunde Id", anchor=tk.E, width=80)  # "E" stands for East, meaning Right. Possible anchors are N, NE, E, SE, S, SW, W, NW and CENTER
tree_aircraft.column("Pladser", anchor=tk.E, width=100)
tree_aircraft.column("Rejse Id", anchor=tk.W, width=100)
tree_aircraft.heading("#0", text="", anchor=tk.W)  # Create column headings
tree_aircraft.heading("Kunde Id", text="Kunde Id", anchor=tk.CENTER)
tree_aircraft.heading("Pladser", text="Pladser", anchor=tk.CENTER)
tree_aircraft.heading("Rejse Id", text="Rejse Id", anchor=tk.CENTER)
tree_aircraft.tag_configure('oddrow', background=oddrow)  # Create tags for rows in 2 different colors
tree_aircraft.tag_configure('evenrow', background=evenrow)

tree_aircraft.bind("<ButtonRelease-1>", lambda event: edit_aircraft(event, tree_aircraft))  # Define function to be called, when an item is selected.
# tree_aircraft.bind("<Double-Button-1>", copy_aircraft_id)  # Define function to be called after double click.

# Define Frame which contains labels, entries and buttons
controls_frame_aircraft = tk.Frame(frame_aircraft)
controls_frame_aircraft.grid(row=3, column=0, padx=padx, pady=pady)

# Define Frame which contains labels (text fields) and entries (input fields)
edit_frame_aircraft = tk.Frame(controls_frame_aircraft)  # Add tuple entry boxes
edit_frame_aircraft.grid(row=0, column=0, padx=padx, pady=pady)
# label and entry for aircraft id
label_aircraft_id = tk.Label(edit_frame_aircraft, text="Kunde Id")  # https://www.tutorialspoint.com/python/tk_label.htm
label_aircraft_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_aircraft_id = tk.Entry(edit_frame_aircraft, width=4, justify="right")  # https://www.tutorialspoint.com/python/tk_entry.htm
entry_aircraft_id.grid(row=1, column=0, padx=padx, pady=pady)
# label and entry for aircraft weight
label_aircraft_max_cargo_weight = tk.Label(edit_frame_aircraft, text="Pladser")
label_aircraft_max_cargo_weight.grid(row=0, column=1, padx=padx, pady=pady)
entry_aircraft_max_cargo_weight = tk.Entry(edit_frame_aircraft, width=8, justify="right")
entry_aircraft_max_cargo_weight.grid(row=1, column=1, padx=padx, pady=pady)
# label and entry for aircraft destination
label_aircraft_registration = tk.Label(edit_frame_aircraft, text="Rejse Id")
label_aircraft_registration.grid(row=0, column=2, padx=padx, pady=pady)
entry_aircraft_registration = tk.Entry(edit_frame_aircraft, width=9)
entry_aircraft_registration.grid(row=1, column=2, padx=padx, pady=pady)

# Define Frame which contains buttons
button_frame_aircraft = tk.Label(controls_frame_aircraft)
button_frame_aircraft.grid(row=1, column=0, padx=padx, pady=pady)
# Define buttons
button_create_aircraft = tk.Button(button_frame_aircraft, text="Create", command=lambda: create_aircraft(tree_aircraft, read_aircraft_entries()))
button_create_aircraft.grid(row=0, column=1, padx=padx, pady=pady)
button_update_aircraft = tk.Button(button_frame_aircraft, text="Update", command=lambda: update_aircraft(tree_aircraft, read_aircraft_entries()))
button_update_aircraft.grid(row=0, column=2, padx=padx, pady=pady)
button_delete_aircraft = tk.Button(button_frame_aircraft, text="Delete", command=lambda: delete_aircraft(tree_aircraft, read_aircraft_entries()))
button_delete_aircraft.grid(row=0, column=3, padx=padx, pady=pady)
button_clear_boxes = tk.Button(button_frame_aircraft, text="Clear Entry Boxes", command=clear_aircraft_entries)
button_clear_boxes.grid(row=0, column=4, padx=padx, pady=pady)
# endregion aircraft widgets


# region transport widgets
# Define Labelframe which contains all transport related GUI objects (data table, labels, buttons, ...)
frame_transport = tk.LabelFrame(main_window, text="rejser")  # https://www.tutorialspoint.com/python/tk_labelframe.htm
frame_transport.grid(row=0, column=2, padx=padx, pady=pady, sticky=tk.N)  # https://www.tutorialspoint.com/python/tk_grid.htm

# Define data table (Treeview) and its scrollbar. Put them in a Frame.
tree_frame_transport = tk.Frame(frame_transport)  # https://www.tutorialspoint.com/python/tk_frame.htm
tree_frame_transport.grid(row=0, column=0, padx=padx, pady=pady)
tree_scroll_transport = tk.Scrollbar(tree_frame_transport)
tree_scroll_transport.grid(row=0, column=1, padx=0, pady=pady, sticky='ns')
tree_transport = ttk.Treeview(tree_frame_transport, yscrollcommand=tree_scroll_transport.set, selectmode="browse")
tree_transport.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_transport.config(command=tree_transport.yview)


tree_transport['columns'] = ("Rute", "Dato", "PladsKapacitet")
tree_transport.column("#0", width=0, stretch=tk.NO)
tree_transport.column("Rute", anchor=tk.E, width=80)
tree_transport.column("Dato", anchor=tk.E, width=100)
tree_transport.column("PladsKapacitet", anchor=tk.E, width=140)
tree_transport.heading("#0", text="", anchor=tk.W)
tree_transport.heading("Rute", text="Rute", anchor=tk.CENTER)
tree_transport.heading("Dato", text="Dato", anchor=tk.CENTER)
tree_transport.heading("PladsKapacitet", text="PladsKapacitet", anchor=tk.CENTER)
tree_transport.tag_configure('oddrow', background=oddrow)
tree_transport.tag_configure('evenrow', background=evenrow)

tree_transport.bind("<ButtonRelease-1>", lambda event: edit_transport(event, tree_transport))


controls_frame_transport = tk.Frame(frame_transport)
controls_frame_transport.grid(row=3, column=0, padx=padx, pady=pady)


edit_frame_transport = tk.Frame(controls_frame_transport)
edit_frame_transport.grid(row=0, column=0, padx=padx, pady=pady)

label_transport_id = tk.Label(edit_frame_transport, text="Rute")
label_transport_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_transport_id = tk.Entry(edit_frame_transport, width=4, justify="right")
entry_transport_id.grid(row=1, column=0, padx=padx, pady=pady)

label_transport_date = tk.Label(edit_frame_transport, text="Dato")
label_transport_date.grid(row=0, column=1, padx=padx, pady=pady)
entry_transport_date = tk.Entry(edit_frame_transport, width=10)
entry_transport_date.grid(row=1, column=1, padx=padx, pady=pady)

label_transport_container_id = tk.Label(edit_frame_transport, text="PladsKapacitet")
label_transport_container_id.grid(row=0, column=2, padx=padx, pady=pady)
entry_transport_container_id = tk.Entry(edit_frame_transport, width=4, justify="right")
entry_transport_container_id.grid(row=1, column=2, padx=padx, pady=pady)



button_frame_transport = tk.Frame(controls_frame_transport)
button_frame_transport.grid(row=1, column=0, padx=padx, pady=pady)

button_create_transport = tk.Button(button_frame_transport, text="Create", command=lambda: create_transport(tree_transport, read_transport_entries()))
button_create_transport.grid(row=0, column=1, padx=padx, pady=pady)
button_update_transport = tk.Button(button_frame_transport, text="Update", command=lambda: update_transport(tree_transport, read_transport_entries()))
button_update_transport.grid(row=0, column=2, padx=padx, pady=pady)
button_delete_transport = tk.Button(button_frame_transport, text="Delete", command=lambda: delete_transport(tree_transport, read_transport_entries()))
button_delete_transport.grid(row=0, column=3, padx=padx, pady=pady)
button_clear_boxes = tk.Button(button_frame_transport, text="Clear Entry Boxes", command=clear_transport_entries)
button_clear_boxes.grid(row=0, column=4, padx=padx, pady=pady)



if __name__ == "__main__":
    refresh_treeview(tree_container, dcd.Container)
    refresh_treeview(tree_aircraft, dcd.Aircraft)
    refresh_treeview(tree_transport, dcd.Transport)
    main_window.mainloop()