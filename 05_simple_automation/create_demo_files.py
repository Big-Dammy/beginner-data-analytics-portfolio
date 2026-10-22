# This helper recreates the small, harmless sample files for practice.
from pathlib import Path

# Keep all files inside this project's demo inbox.
INBOX = Path(__file__).resolve().parent / "demo_inbox"
INBOX.mkdir(exist_ok=True)

# Create a few plain-text examples. These are not real business documents.
sample_files = {
    "sales_january.csv": "month,sales\nJanuary,120\n",
    "meeting_notes.txt": "Demo meeting notes.\n",
    "chart.png.txt": "This is a placeholder file, not an image.\n",
    "report_final.pdf.txt": "This is a placeholder file, not a PDF.\n",
    "readme.txt": "A harmless sample file for the organiser.\n",
}

# Write each example file to disk.
for file_name, file_content in sample_files.items():
    file_path = INBOX / file_name
    file_path.write_text(file_content, encoding="utf-8")
    print(f"Created: {file_path.name}")

print("Demo files are ready. The organiser defaults to preview mode.")
