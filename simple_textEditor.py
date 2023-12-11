from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os

# Initialize the app title
app_title = "simple_text_editor"

# Function to update the app title
def update_app_title(file_title=None):
    if file_title:
        filename = os.path.basename(file_title)  # Extract only the filename
        window.title(f"{app_title} - {filename}")
    else:
        window.title(app_title)


# OPEN FILE FUNCTION
def open_file():
    try:
        filepath = filedialog.askopenfilename(title="Open File", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        
        if not filepath:  # User canceled the file dialog
            return

        with open(filepath, 'r') as file:
            content = file.read()

        # Update the Text widget with the file content
        text_area.delete(1.0, END)  # Clear existing content
        text_area.insert(INSERT, content)
        update_app_title(file_title=filepath)

        messagebox.showinfo("File Opened", f"File '{filepath}' opened successfully.")
    except FileNotFoundError:
        messagebox.showerror("File Not Found", "The selected file does not exist.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while opening the file: {str(e)}")


# SAVE AS FILE FUNCTION
def save_as_file():
    try:
        # Always prompts the user to choose a file location
        file_save = filedialog.asksaveasfile(
            defaultextension='.txt',
            filetypes=[("Text file", ".txt"), ("HTML", ".html"), ("All files", ".*")]
        )

        if file_save:
            try:
                content_to_save = text_area.get("1.0", END)
                file_save.write(content_to_save)
                file_save.close()
                update_app_title(file_title=file_save.name)
                messagebox.showinfo("File Saved", "File saved successfully")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


# SAVE FILE FUNCTION
def save_file():
    # Ask the user if they want to save the file
    answer = messagebox.askquestion(title="Save file", message="Do you want to save the file")

    if answer == "yes":
        # Prompt the user to choose a file name and location
        file_save = filedialog.asksaveasfile(
            defaultextension='.txt',
            filetypes=[("Text file", ".txt"), ("HTML", ".html"), ("All files", ".*")]
        )

        if file_save:
          try:
               # Get the content from your Text widget (replace 'text_widget' with your actual Text widget reference)
               content_to_save = text_area.get("1.0", END)

               # Write the content to the selected file
               file_save.write(content_to_save)
               file_save.close()

               messagebox.showinfo("File Saved", "File saved successfully")
          except Exception as e:
               messagebox.showerror("Error", f"An error occurred: {str(e)}")
          else:
               messagebox.showinfo("Info", "File not saved")


# COPY TEXT FUNCTION
def copy_text():
    # Get the selected text from the Text widget
    selected_text = text_area.get(SEL_FIRST, SEL_LAST)

    # Copy the selected text to the clipboard
    if selected_text:
        window.clipboard_clear()
        window.clipboard_append(selected_text)
        window.update()


# CUT SELECTED TEXT FUNCTION
def cut_text():
    # Get the selected text from the Text widget
    selected_text = text_area.get(SEL_FIRST, SEL_LAST)

    # Copy the selected text to the clipboard
    if selected_text:
        window.clipboard_clear()
        window.clipboard_append(selected_text)

        # Delete the selected text from the Text widget
        text_area.delete(SEL_FIRST,SEL_LAST)

def delete_text():
    text_area.delete(1.0, END)



window=Tk()
window.title("simple_text_editor")
menu_bar = Menu(window)
window.config(menu=menu_bar)

# FILE MENU
fileMenu = Menu(menu_bar, tearoff=0, font=("Constantia",15))
menu_bar.add_cascade(label="FILE", menu=fileMenu)
fileMenu.add_command(label="Open", command=open_file)
fileMenu.add_command(label="Save",command=save_file)
fileMenu.add_command(label="Save as",command=save_as_file)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit)

# EDIT MENU
editMenu = Menu(menu_bar, tearoff=0, font=("Constantia",15))
menu_bar.add_cascade(label="EDIT", menu=editMenu)
editMenu.add_command(label="Copy",command=copy_text)
editMenu.add_command(label="Cut", command=cut_text)
editMenu.add_command(label="Delete", command=delete_text)


# Create a Text widget
text_area = Text(window, font=("Constantia", 15))
text_area.grid(row=0, column=0, sticky="nsew")  # Use grid with sticky to fill both directions

# Configure grid weights to make the Text widget expand
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Start the main event loop
window.mainloop()