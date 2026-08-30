# main.py
import tkinter as tk
from gui import CampusAssistantGUI

def main():
    """Entry point for the Campus Assistant application."""
    root = tk.Tk()
    app = CampusAssistantGUI(root)
    
    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
