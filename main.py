import tkinter as tk
from backend.backendlogic import PhishingBackend
from backend.detectorlogic import AdvancedAlgorithm
from frontend.frontendlogic import PhishingMain

def main():
    # 1. Initialize Algorithm
    engine = AdvancedAlgorithm()
    
    # 2. Initialize Backend
    # Pass engine to Backend
    backend = PhishingBackend(engine)
    
    # 3. Initialize Frontend
    root = tk.Tk()
    # Pass backend to Frontend
    app = PhishingMain(root, backend)
    
    root.mainloop()

if __name__ == "__main__":
    main()