"""
Script: recycle_bin.py
Description: Tool for recycle bin
Category: Utilities
"""
import ctypes

def clear_recycle_bin():
    SHELL32 = ctypes.windll.shell32
    SHELL32.SHEmptyRecycleBinW(None, None, 1)

# Example usage:
clear_recycle_bin()
