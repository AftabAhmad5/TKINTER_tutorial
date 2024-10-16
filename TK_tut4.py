"""
let say what we have now we want to replicate it in a new project or different part of an application
as we have added frame in our applicatoin its makes it easier for us to replicate it and use those sets of widget inside the frame
for example let use two form now so all we have to do is to copy the existing frame and name it say frame2

"""



#now let clean up the UI for better responsiveness
import tkinter as tk

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

frame = tk.Frame(root) # here root is the main window inside which we have create a frame
# place the frame in the top left corner
# now to make the frame responsive add sticky parameter for both horizontal east west ew and vertical nw north south so that it can be expand in all directions
# add padding to the frame to both x and y direction
frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
# now to make frame responsive remember that we have two widgets there that is input field and a button
# we want to expand input field but not the button since input field is at column 0 posotion then only use that and expand the input field only horizontally that is east west ew
frame.columnconfigure(0, weight=1) # this will configure entry field which is at postion 0 line 42

frame.rowconfigure(1, weight=1) # this will configure list box field and we want to expand it in all direction so use sticky = "nsew" in the listbox grid line 59

# now creating an entry field insde the frame 
entry = tk.Entry(frame)

# now we are adjusting it inside the frame
# we are expanding only in horizontally direction so use sticky = "ew"
entry.grid(row=0, column=0, sticky="ew")

# adding keyboard bind say if someone want to enter data using enter key like not clicking on add button
entry.bind("<Return>", lambda event: add_to_list()) # with help of lambda function we added an argument to add_to_list function to take this extra key bind feature

# this button will add input text to a list
entry_btn = tk.Button(frame, text="Add", command=add_to_list)
entry_btn.grid(row=0, column=1)

# let add a listbox that will hold all the values that we have added
text_list = tk.Listbox(frame)
# now to make the text list take the whole space we need to add 
# sticky argument and passing ew meaning east west
# that way it will take whole space of the window
# and for responsiveness like if we expand the app go to main window and add 
# responsiveness there that is configure both the root and the frame for responsiveness as shown above
# text_list.grid(row=1,column=0, sticky="ew")
text_list.grid(row=1,column=0, sticky="nsew")


"""
just copied the aboveframe along with entry grid and same button as we are replicating form
"""
# copied frame will be now renamed to say frame two so we will have exact frame along with widgets 
frame2 = tk.Frame(root)
frame2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
frame2.columnconfigure(0, weight=1) # this will configure entry field which is at postion 0 line 42
frame2.rowconfigure(1, weight=1) # this will configure list box field and we want to expand it in all direction so use sticky = "nsew" in the listbox grid line 59

"""
since new frame is added now all we ahve to do is to change it position since old frame lies at row 0 col0 new frame should be place at different position
so it save us alot of work else we would have to go through each widget and adjust their rows cols position respectively now all we have done is copied the old frame
named it frame2 and we will change it position for example col 2 so it will show in next col.
"""

"""
on resizing the window the frame doesnot take the same width it is because how  we have set the weight earlier
for col0 and frame 2 is at column 1 so also configure weight = 1 for col 2 
above I have now added root.columnconfigure(1, weight=1) for frame 2 and now it will take the same space as frame1
onething more these weights are proportional so if we want to expand one column more than the other just change the weight value
say we want to expand column 1 by 75 percent of the other then change its weight value in the main root window to 3
it will exactly take 75 percent space to that of column 1

"""
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