# gui.py
import tkinter as tk
from tkinter import scrolledtext
from dialogue_manager import DialogueManager

class CampusAssistantGUI:
    """Tkinter-based Graphical User Interface for the Campus Assistant."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Campus Assistant")
        self.root.geometry("450x600")
        self.root.configure(bg="#f4f4f4")
        
        # Initialize the Dialogue Manager
        self.dm = DialogueManager()
        
        self.setup_ui()
        
        # Initial greeting
        self.display_message("Assistant", "Hello! I am your Campus Assistant.\nType 'help' to see what I can do.")
        
    def setup_ui(self):
        # Chat display area
        self.chat_area = scrolledtext.ScrolledText(
            self.root, 
            wrap=tk.WORD, 
            state=tk.DISABLED, 
            font=("Helvetica", 11),
            bg="#ffffff"
        )
        self.chat_area.pack(padx=15, pady=15, fill=tk.BOTH, expand=True)
        
        # Frame for input and buttons
        self.input_frame = tk.Frame(self.root, bg="#f4f4f4")
        self.input_frame.pack(fill=tk.X, padx=15, pady=(0, 15))
        
        # User input box
        self.entry_box = tk.Entry(self.input_frame, font=("Helvetica", 12))
        self.entry_box.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=5, padx=(0, 10))
        self.entry_box.bind("<Return>", self.send_message_event)
        
        # Send button
        self.send_button = tk.Button(
            self.input_frame, 
            text="Send", 
            command=self.send_message,
            bg="#0078D7", 
            fg="white",
            font=("Helvetica", 10, "bold"),
            relief=tk.FLAT,
            padx=15,
            pady=3
        )
        self.send_button.pack(side=tk.LEFT)
        
        # Clear Chat button
        self.clear_button = tk.Button(
            self.input_frame, 
            text="Clear", 
            command=self.clear_chat,
            bg="#d9534f", 
            fg="white",
            font=("Helvetica", 10, "bold"),
            relief=tk.FLAT,
            padx=15,
            pady=3
        )
        self.clear_button.pack(side=tk.LEFT, padx=(10, 0))
        
    def send_message_event(self, event):
        """Handler for the Enter key press."""
        self.send_message()
        
    def send_message(self):
        """Processes the user input and fetches the assistant's response."""
        user_text = self.entry_box.get().strip()
        if not user_text:
            return
            
        # Display user message
        self.display_message("You", user_text)
        self.entry_box.delete(0, tk.END)
        
        # Get response from the dialogue manager
        response = self.dm.process_input(user_text)
        
        # Display assistant message
        self.display_message("Assistant", response)
        
    def display_message(self, sender, message):
        """Appends a message to the chat display area."""
        self.chat_area.config(state=tk.NORMAL)
        
        # Format the text and display
        self.chat_area.insert(tk.END, f"{sender}:\n{message}\n\n")
            
        self.chat_area.see(tk.END)
        self.chat_area.config(state=tk.DISABLED)
        
    def clear_chat(self):
        """Clears the chat area and resets the dialogue manager state."""
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.delete(1.0, tk.END)
        self.chat_area.config(state=tk.DISABLED)
        
        # Reset the dialogue manager's state
        self.dm.reset_state()
        
        # Show greeting again
        self.display_message("Assistant", "Hello! I am your Campus Assistant.\nType 'help' to see what I can do.")
