# argparse lets us add a clear --apply option to the command line.
# pathlib provides safer, readable ways to work with file paths.
from pathlib import Path
import argparse
import shutil

# Find the demo inbox that belongs to this project.
HERE = Path(__file__).resolve().parent
INBOX = HERE / "demo_inbox"

# Map some file extensions to easy-to-understand folder names.
FOLDER_NAMES = {
    ".csv": "CSV",
    ".txt": "TXT",
    ".pdf": "PDF",
    ".png": "IMAGES",
    ".jpg": "IMAGES",
    ".jpeg": "IMAGES",
}

def main():
    # Explain the available command-line option to the user.
    parser = argparse.ArgumentParser(description="Organise files in this project's demo inbox only.")
    parser.add_argument(
        "--apply", action="store_true",
        help="Actually move files. Without this option, only preview the changes."
    )
    args = parser.parse_args()

    # Stop safely if the expected demo folder is missing.
    if not INBOX.exists():
        print("Demo inbox does not exist. Please check the project folder.")
        return

    # Look at files directly inside the demo inbox, not the rest of your computer.
    files = [item for item in INBOX.iterdir() if item.is_file()]
    if not files:
        print("No files to organise in the demo inbox.")
        return

    # Print each planned move so the user can review it first.
    for file_path in files:
        folder_name = FOLDER_NAMES.get(file_path.suffix.lower(), "OTHER")
        destination_folder = INBOX / folder_name
        destination_file = destination_folder / file_path.name
        print(f"{file_path.name} -> {folder_name}/{file_path.name}")

        # Only create folders and move files when --apply was explicitly supplied.
        if args.apply:
            destination_folder.mkdir(exist_ok=True)
            # Avoid accidentally overwriting a file with the same name.
            if destination_file.exists():
                print(f"Skipped because destination already exists: {destination_file.name}")
                continue
            shutil.move(str(file_path), str(destination_file))

    # Make the current safety mode clear in the terminal.
    if args.apply:
        print("Files moved inside the demo inbox.")
    else:
        print("DRY RUN: nothing was moved. Add --apply to move these demo files.")

# Run main only when this file is executed directly.
if __name__ == "__main__":
    main()
