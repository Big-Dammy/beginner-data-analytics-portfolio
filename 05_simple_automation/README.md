# 5. Simple File Automation

## Goal
Practise automating a repetitive task: sorting files into folders based on their extensions.

## Safety first
This project only targets the included `demo_inbox/` folder. By default it is in **dry-run mode**, so it prints what it would do without moving anything. To actually move the sample files, run `python organise_files.py --apply`. You can recreate the original sample inbox by running `python create_demo_files.py` after manually removing the organised folders, or simply unzip a fresh copy.

## Run
```bash
python organise_files.py
python organise_files.py --apply
```

The organiser creates folders such as `CSV`, `TXT`, and `OTHER` inside the demo inbox. It never scans your home folder or your whole computer.
