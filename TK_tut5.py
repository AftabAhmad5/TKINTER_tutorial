
"""
let add themed widget that comes with tkinter library for that
import ttk that is theme tkinter for visual difference
"""
import tkinter as tk
from tkinter import ttk
# creating a window name it root
root = tk.Tk()
# name the app
root.title("Form App")

def add_to_list():
    #getting input data
    text = entry.get()
    # checking to avoid blank field entered
    if text:
        text_list.insert(tk.END, text)
        # to make the entry field empty after entering data use delete method
        entry.delete(0,tk.END) # 0 mean start from the very first till END of the letter 


# adding responsiveness, configuring column 0 with weight equal to 1 similary we going do the same for row with weight equal to 1
# that just means when the app expand the root will take all the space 
root.columnconfigure(0, weight = 1)

#configuring column for frame2 which is at column 1 in the root window that is main window
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)


# creating a frame its a container which has its own grid layout its like a box in a box which can be arranged and what ever data in the second box can be arranged with it.
# applying ttk on frame1
frame = ttk.Frame(root) # here root is the main window inside which we have create a frame
frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
frame.columnconfigure(0, weight=1) # this will configure entry field which is at postion 0 line 42

frame.rowconfigure(1, weight=1) # this will configure list box field and we want to expand it in all direction so use sticky = "nsew" in the listbox grid line 59

# now creating an entry field insde the frame 
# also applying the themed version on entry 
entry = ttk.Entry(frame)

# now we are adjusting it inside the frame
# we are expanding only in horizontally direction so use sticky = "ew"
entry.grid(row=0, column=0, sticky="ew")

# adding keyboard bind say if someone want to enter data using enter key like not clicking on add button
entry.bind("<Return>", lambda event: add_to_list()) # with help of lambda function we added an argument to add_to_list function to take this extra key bind feature

# this button will add input text to a list
entry_btn = ttk.Button(frame, text="Add", command=add_to_list)
entry_btn.grid(row=0, column=1)

# let add a listbox that will hold all the values that we have added
text_list = tk.Listbox(frame)

text_list.grid(row=1,column=0, sticky="nsew")


"""
just copied the aboveframe along with entry grid and same button as we are replicating form
"""
# copied frame will be now renamed to say frame two so we will have exact frame along with widgets 
frame2 = tk.Frame(root)
frame2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
frame2.columnconfigure(0, weight=1) # this will configure entry field which is at postion 0 line 42
frame2.rowconfigure(1, weight=1) # this will configure list box field and we want to expand it in all direction so use sticky = "nsew" in the listbox grid line 59


# now creating an entry field insde the frame2 
entry = tk.Entry(frame2)

# now we are adjusting it inside the frame
# we are expanding only in horizontally direction so use sticky = "ew"
entry.grid(row=0, column=0, sticky="ew")

# adding keyboard bind say if someone want to enter data using enter key like not clicking on add button
entry.bind("<Return>", lambda event: add_to_list()) # with help of lambda function we added an argument to add_to_list function to take this extra key bind feature

# entry button added to frame2 
entry_btn = tk.Button(frame2, text="Add", command=add_to_list)
entry_btn.grid(row=0, column=1)

# listbox added to frame2
text_list = tk.Listbox(frame2)

text_list.grid(row=1,column=0, sticky="nsew")


root.mainloop()