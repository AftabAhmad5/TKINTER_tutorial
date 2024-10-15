# bultin gui library comes with python
import tkinter as tk

# first let run a basic test if library is working
# tk._test()

# to make a simple application we need a window for it to do that we have a command for it called tk.TK() and we going to name it root
root = tk.Tk()
"""
by running this code we would see nothing as this happen so instantly
meaning the app open and closes pretty quickly that cant be observed so to make the app stay
we need to use loop to do that we going to call mainloop() method on root
"""
# root.mainloop() # now we get this blank window currently nothing in it

"""
now let add some widgets and title etc to our first app but above I havec commented out loop 
because everythin is going to be sandwich in between tk.Tk() that is root and root.mainloop()
"""

root.title("App")

def on_click():
    # print("Testing")
    # we can also change the lable with it do something in gui forexample
    lbl.config(text = "Button 1 clicked")


# using a label to display something for the button below it
lbl = tk.Label(root, text = "Lable 1")
# beside text alots of other functionality label have such which can be shown by
print(lbl.config().keys())

lbl.grid()
# let create a button by passing in our root variable we are passing it as its going to be the parent window in which widget will
# displayed on such as button etc
# btn = tk.Button(root, text = "button 1")
# adding a function as explained in line 47
btn = tk.Button(root, text = "Button 1", command = on_click) # dont execute the function inside the parenthesis as it will do it itself execute mean calling function with parenthesis like on_click()
# now to show this button we going to use grid layout which is mostly used and will also helps us arrange it in different position
btn.grid() # by default it appears in the top left corner but since grid layout consist of rows and column we can easily arrange that button where ever we want to


"""
let arrange both label and button to our desired position since grid layout based on rows and columns configuration and here 
row one actually starts from 0 so let for now choose row 0 and column zero for lable and row 1 column 0 for button 
so that way button will appear below the lable as shown below
"""
lbl.grid(row=0,column=0)
btn.grid(row=1,column=0)

# now let add some functionality to the button meaning if the button is clicked its going to let say call
# a function to do some job to that let create a function for it called on_click() first to handle that event later on


root.mainloop()