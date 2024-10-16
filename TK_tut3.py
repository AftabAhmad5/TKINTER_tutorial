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
root.rowconfigure(0, weight=1)


# creating a frame its a container which has its own grid layout its like a box in a box which can be arranged and what ever data in the second box can be arranged with it.

frame = tk.Frame(root) # here root is the main window inside which we have create a frame
# place the frame in the top left corner
# now to make the frame responsive add sticky parameter for both horizontal east west ew and vertical nw north south so that it can be expand in all directions
frame.grid(row=0, column=0, sticky="nsew")
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



root.mainloop()