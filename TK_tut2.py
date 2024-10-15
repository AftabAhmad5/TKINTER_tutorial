# since now the basic is learned let create a simple form app now
import tkinter as tk

# create a window known by root variable
root = tk.Tk()
# name the app
root.title("Form App")

def add_to_list(event=None):
    # once the button is clicked we going to grab data from the entry box
    text = entry.get()
    if text: # if there is text and not just a blank line 
        text_list.insert(tk.END, text)# tk.END is a special tk constant that represent end of a current content in a widget
        # to remove the previous data from the entry field to enter new data we going to use delete method to do that that is
        entry.delete(0,tk.END) # meaning 0 from start to the end of content tk.END it will delete it


"""
to make the content a bit origanized we going to use frame in the window so each frame will have its own widget etc and can 
similarly be controller with grid layout but plus point is that if we move the single frame whwatever that frame contain will move along with it
"""
# frame is just a container that oragnize the layout more easily
frame = tk.Frame(root)
frame.grid(row=0,column=0)

# text input 
entry = tk.Entry(frame) # mind out frame will have its own mini layout in the main window called root so we can move limit within the frame and then can move frame in the main window aloing with those elements

entry.grid(row=0, column=0)

"""
how about we add a keyboard event meaning rather clicking add button again and again to add data to a list if we hit enter 
it should do the same to do that we going to bind entry with a button say enter here denoted by Return
but since add_to_list function does not take any arguemnt than just pass an argument tthere name event=None to avoid arg error
we can also use lambda function but for simplicity let go with event=None arg
"""
entry.bind("<Return>",add_to_list)
# with lambda function it will look like this that we dont have touse event=None in the add_to_list function
# entry.bind("<Return>", lambda event: add_to_list())


# this button will add input text to a list
entry_btn = tk.Button(frame, text="Add", command=add_to_list)
entry_btn.grid(row=0, column=1)

# let add a listbox that will hold all the values that we have added
text_list = tk.Listbox(frame)
text_list.grid(row=1,column=0)

# now let call a function that will add stuffs to the list once Add button is clicked



root.mainloop()
