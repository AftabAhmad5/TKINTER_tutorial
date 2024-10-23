# earlier if we check the previous code there was the bug one form was working while the other was not
# thats because of the straight forward code so better we should use class to avoid conflict

import tkinter as tk
from tkinter import ttk



# class Application:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("Form App")
#         self.root.mainloop()
# app = Application()

# or directly inherit from the tk class that will be conscise


def main():
    app = Application()
    app.mainloop()




class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Form App")

        # customization and configuring rows and cols of the parent window app
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=1)

        # since now we have created our InputForm class we can now create as many instances of it as we want to without any conflict
        # also as Input form is basically a frame we can create multiple frames here like before with no issue at all since each frame is specificc to its own instanes
        # such as

        frame_1 = InputForm(self)
        frame_1.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
        #create another frame for anther input form

        frame_2 = InputForm(self)
        frame_2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)


        


class InputForm(ttk.Frame):
    # this obviously will take parent window so that frame can be added then in the parent window
    def __init__(self, parent):
        super().__init__(parent)

        # configuration for the frame
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # adding entry widget into the frame
        self.entry = ttk.Entry(self)
        self.entry.grid(row=0, column=0, sticky = "ew")

        self.entry.bind("<Return>", self.add_to_list)

        # adding button for entry into frame widget

        self.entry_btn = ttk.Button(self, text="Add", command = self.add_to_list)
        self.entry_btn.grid(row=0, column=1)

        self.entry_btn2 = ttk.Button(self, text="Clear", command = self.clear_list)
        self.entry_btn2.grid(row=0, column=2)

        # adding text box to represent entered data
        self.text_list = tk.Listbox(self)
        self.text_list.grid(row=1, column = 0, columnspan=2, sticky="nsew")

        # add to list function is only active in frame so we dont have to use it in above Application class

    def add_to_list(self,event=None):
        text = self.entry.get()
        if text:
            self.text_list.insert(tk.END, text)
            self.entry.delete(0,tk.END)
    
    def clear_list(self):
        self.text_list.delete(0,tk.END)



if __name__ == "__main__":
    main()