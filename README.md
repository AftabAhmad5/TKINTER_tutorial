# Tkinter tutorial
## notes taken from Corey Schafer youtube channel link given below
## source: 
https://www.youtube.com/watch?v=epDKamC-V-8&t=135s

This project demonstrates how to create a simple form application using Python's Tkinter library, with a focus on organizing widgets using frames and making the UI responsive. The app allows users to input text into a list, and it includes the option to use themed widgets from the ttk module.

### Features
- Two form sections created with reusable frames
- Responsive UI using grid layout with weight configuration
- Ability to add text to a Listbox via both a button click and the Enter key
- Themed widgets for a cleaner visual experience (using ttk)

## Requirements
- Python 3.x

### Code Breakdown
First, we set up the main application window (root) using tk.Tk() and give the app a title:
```
root = tk.Tk()
root.title("Form App")
```
We define a function **add_to_list** to handle adding text input to the list. This function clears the input field after submitting to the Listbox:

```
def add_to_list():
    text = entry.get()
    if text:
        text_list.insert(tk.END, text)
        entry.delete(0, tk.END)
```

To ensure that the UI adjusts as the window is resized, we configure the row and column weights. This gives the widgets flexibility to expand:

```
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
```
We also make the individual frames responsive by configuring their rows and columns, and using sticky="nsew":

```
frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
frame.columnconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)

```
## Organizing Widgets with Frames

Frames are useful for organizing the layout. Here, we created two frames: one for each form section. Each frame has its own grid layout and widgets:

```
frame = ttk.Frame(root)
frame2 = tk.Frame(root)
```
By copying the frame structure, we can easily replicate the form in a different part of the application. For example, frame2 is positioned in column 1, creating two sections side by side:

```
frame2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
```
## Input Field and Button Functionality
Inside each frame, we create an entry field for user input, a button to trigger adding text to the list, and bind the Enter key to the same functionality:

```
entry = ttk.Entry(frame)
entry.bind("<Return>", lambda event: add_to_list())

entry_btn = ttk.Button(frame, text="Add", command=add_to_list)
entry_btn.grid(row=0, column=1)
```
## Listbox for Displaying Entries
Finally, we add a Listbox in each frame to display the text entries. For the Listbox, we use tk.Listbox as ttk does not have a themed version:

```
text_list = tk.Listbox(frame)
text_list.grid(row=1, column=0, sticky="nsew")
```
```
Themed Widgets
To enhance the look of the app, we replace the standard tk widgets with their themed counterparts from ttk, which is a themed variant of Tkinter:

from tkinter import ttk
frame = ttk.Frame(root)
entry = ttk.Entry(frame)
entry_btn = ttk.Button(frame, text="Add", command=add_to_list)
```
## Replicating the Form
The app shows how easy it is to replicate the form by simply copying the original frame setup:


`frame2 = tk.Frame(root)`
With just minor changes, we now have two form sections, both fully responsive and functional.

Part 1 completed