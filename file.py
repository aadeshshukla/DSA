import os
import shutil
from pathlib import Path


def create_file(filename: str):
    """Creates a new empty file if it doesn't already exist."""
    path = Path(filename)
    try:
        with open(path, "x", encoding="utf-8"):
            print(f"[SUCCESS] File '{filename}' created successfully.")
    except FileExistsError:
        print(f"[ERROR] File '{filename}' already exists.")
    except OSError as err:
        print(f"[ERROR] Could not create file: {err}")


def write_file(filename: str, content: str):
    """Overwrites or creates a file with new content."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"[SUCCESS] Content written to '{filename}'.")
    except OSError as err:
        print(f"[ERROR] Failed to write to file: {err}")


def append_file(filename: str, content: str):
    """Appends content to the end of a file."""
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(content + "\n")
        print(f"[SUCCESS] Content appended to '{filename}'.")
    except OSError as err:
        print(f"[ERROR] Failed to append to file: {err}")


def read_file(filename: str):
    """Reads and displays the content of a file."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            print(f"\n--- Content of '{filename}' ---")
            print(file.read())
            print("--- End of File ---\n")
    except FileNotFoundError:
        print(f"[ERROR] File '{filename}' not found.")
    except PermissionError:
        print(f"[ERROR] Permission denied to read '{filename}'.")
    except OSError as err:
        print(f"[ERROR] Failed to read file: {err}")


def rename_file(old_name: str, new_name: str):
    """Renames an existing file."""
    old_path, new_path = Path(old_name), Path(new_name)
    try:
        if not old_path.exists():
            print(f"[ERROR] File '{old_name}' does not exist.")
            return
        if new_path.exists():
            print(f"[ERROR] Target name '{new_name}' already exists.")
            return
        old_path.rename(new_path)
        print(f"[SUCCESS] Renamed '{old_name}' to '{new_name}'.")
    except OSError as err:
        print(f"[ERROR] Failed to rename: {err}")


def copy_file(source: str, destination: str):
    """Copies a file to a new location or name."""
    try:
        shutil.copy2(source, destination)
        print(f"[SUCCESS] Copied '{source}' to '{destination}'.")
    except FileNotFoundError:
        print(f"[ERROR] Source file '{source}' not found.")
    except OSError as err:
        print(f"[ERROR] Failed to copy file: {err}")


def move_file(source: str, destination: str):
    """Moves a file to a new location."""
    try:
        shutil.move(source, destination)
        print(f"[SUCCESS] Moved '{source}' to '{destination}'.")
    except FileNotFoundError:
        print(f"[ERROR] Source file '{source}' not found.")
    except OSError as err:
        print(f"[ERROR] Failed to move file: {err}")


def delete_file(filename: str):
    """Deletes a file permanently."""
    path = Path(filename)
    try:
        path.unlink()
        print(f"[SUCCESS] File '{filename}' deleted.")
    except FileNotFoundError:
        print(f"[ERROR] File '{filename}' not found.")
    except PermissionError:
        print(f"[ERROR] Permission denied to delete '{filename}'.")
    except OSError as err:
        print(f"[ERROR] Failed to delete file: {err}")


def list_files(directory: str = "."):
    """Lists all files in the specified directory."""
    path = Path(directory)
    if not path.is_dir():
        print(f"[ERROR] '{directory}' is not a valid directory.")
        return

    print(f"\nFiles in '{path.resolve()}':")
    items = list(path.iterdir())
    if not items:
        print("  (Empty directory)")
        return

    for item in sorted(items):
        item_type = "DIR " if item.is_dir() else "FILE"
        size = f"{item.stat().st_size:,} bytes" if item.is_file() else "-"
        print(f"  [{item_type}] {item.name:<30} {size}")
    print()


def main():
    menu = """
========================================
       FILE MANAGEMENT SYSTEM
========================================
1. Create a new file
2. Write (overwrite) to a file
3. Append content to a file
4. Read a file
5. Rename a file
6. Copy a file
7. Move a file
8. Delete a file
9. List files in directory
0. Exit
========================================
"""
    while True:
        print(menu)
        choice = input("Enter your choice (0-9): ").strip()

        if choice == "1":
            name = input("Enter file name to create: ").strip()
            create_file(name)
        elif choice == "2":
            name = input("Enter file name: ").strip()
            text = input("Enter text to write: ")
            write_file(name, text)
        elif choice == "3":
            name = input("Enter file name: ").strip()
            text = input("Enter text to append: ")
            append_file(name, text)
        elif choice == "4":
            name = input("Enter file name to read: ").strip()
            read_file(name)
        elif choice == "5":
            old_name = input("Enter current file name: ").strip()
            new_name = input("Enter new file name: ").strip()
            rename_file(old_name, new_name)
        elif choice == "6":
            src = input("Enter source file path: ").strip()
            dst = input("Enter destination path: ").strip()
            copy_file(src, dst)
        elif choice == "7":
            src = input("Enter source file path: ").strip()
            dst = input("Enter destination path: ").strip()
            move_file(src, dst)
        elif choice == "8":
            name = input("Enter file name to delete: ").strip()
            confirm = input(f"Are you sure you want to delete '{name}'? (y/n): ").lower()
            if confirm == "y":
                delete_file(name)
            else:
                print("Deletion cancelled.")
        elif choice == "9":
            dir_path = input("Enter directory path (leave blank for current folder): ").strip()
            list_files(dir_path if dir_path else ".")
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("[ERROR] Invalid choice. Please enter a number from 0 to 9.")


if __name__ == "__main__":
    main()
