import tkinter as tk
from tkinter import messagebox

class PhishingMain:
    """
    Form-based interface providing a clear, consistent, 
    and user-controlled experience.
    """
    def __init__(self, root, backend):
        # This now accepts 'self', 'root', and 'backend' (3 arguments total)
        self.root = root
        self.backend = backend 
        self.root.title("Phishing Detection System")
        self.root.geometry("500x350")
        self.create_widgets()

    def create_widgets(self):
        """Builds the form-based interface elements."""
        tk.Label(self.root, text="URL Scanner", font=("Arial", 16, "bold")).pack(pady=10)
        
        self.url_input = tk.Entry(self.root, width=50)
        self.url_input.pack(pady=10)
        
        # User-controlled action button
        self.scan_btn = tk.Button(self.root, text="Analyze URL", command=self.handle_scan)
        self.scan_btn.pack(pady=10)
        
        self.result_text = tk.Label(self.root, text="", font=("Arial", 12))
        self.result_text.pack(pady=20)

    def handle_scan(self):
        url = self.url_input.get()
        # Calling the backend logic
        status = self.backend.analyze_url(url)
        self.result_text.config(text=f"Result: {status}")