"""
helpers.py
----------
Author  : Dnyaneshwari Sonawane
College : DYPCOEI, SPPU, Pune

CLI display utilities used across all menus.
"""

import os


def print_banner():
    print("""
╔══════════════════════════════════════════════════════════╗
║           HOSPITAL MANAGEMENT SYSTEM                     ║
║           Developed by Dnyaneshwari Sonawane             ║
║           DYPCOEI, SPPU, Pune                            ║
╚══════════════════════════════════════════════════════════╝
""")


def print_divider():
    print("\n" + "=" * 60 + "\n")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
