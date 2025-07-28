# main.py
"""
Main entry point for the Login System.
Allows user to select and launch the desired UI (Tkinter or Flet).
"""
import sys

# Import UI module (make sure the file is named 'login_ui.py')
import login_ui


def main():
    print("Launching Login System (Tkinter UI)...")
    login_ui.run_tkinter_ui()

if __name__ == "__main__":
    main()
