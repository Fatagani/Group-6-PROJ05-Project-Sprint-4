# main.py
"""
Main entry point for the Login System.
Allows user to select and launch the desired UI (Tkinter or Flet).
"""
from view.login_ui import run_tkinter_ui

if __name__ == "__main__":
    run_tkinter_ui()
