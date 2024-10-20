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