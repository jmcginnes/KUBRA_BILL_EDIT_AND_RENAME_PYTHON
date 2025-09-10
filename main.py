############################
#
#  Kubra Bill Edit and Rename
#  Created by: John McGinnes
#
############################

# %%
#############################
# 
# Imports and Environment
#
#############################
import os
import re
import shutil
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# %%
#############################
# 
# Get Config from .env and user input
#
#############################
folder_path = os.getenv('FOLDER_PATH')

if not folder_path or not os.path.isdir(folder_path):
    raise Exception(f"Invalid or missing FOLDER_PATH: {folder_path}")

# Prompt the user for initials
initials = input("Please enter your initials: ").strip().upper()
if not initials.isalpha():
    raise Exception("Initials must be alphabetic characters only.")

# Get current date in MMDDYYYY format
date_suffix = datetime.now().strftime("%m%d%Y")
file_suffix = f"_{initials}_{date_suffix}"

# Get path to this script and set Archive folder
script_dir = os.path.dirname(os.path.abspath(__file__))
archive_dir = os.path.join(script_dir, "Archive")
os.makedirs(archive_dir, exist_ok=True)

# %%
#############################
# 
# Process and Modify Files with Debugging
#
#############################
for filename in os.listdir(folder_path):
    if filename.lower().endswith('.xml'):
        print(f"Processing file: {filename}")

        original_path = os.path.join(folder_path, filename)
        base, ext = os.path.splitext(filename)
        new_filename = f"{base}{file_suffix}{ext}"
        new_path = os.path.join(folder_path, new_filename)
        archived_path = os.path.join(archive_dir, filename)

        # Read original file content
        try:
            with open(original_path, 'r', encoding='utf-8') as file:
                content = file.read()
            print("  Read file successfully")
        except Exception as e:
            print(f"  Failed to read file '{filename}': {e}")
            continue

        # Add XML comment before the closing root tag
        resubmit_comment = f"<!-- Resubmitted on {datetime.now().strftime('%m/%d/%Y')} by {initials} -->"

        # Try to find the closing root tag and insert the comment before it
        closing_tag_match = re.search(r'(</\s*BILLPRINTEXTRACTS\s*>)', content, re.IGNORECASE)

        if closing_tag_match:
            closing_tag = closing_tag_match.group(1)
            modified_content = content.replace(closing_tag, f"{resubmit_comment}\n{closing_tag}")
            print("  Added resubmission comment.")
        else:
            print("  Could not find closing BILLPRINTEXTRACTS tag — skipping comment.")
            modified_content = content


        # Write modified content to new file
        try:
            with open(new_path, 'w', encoding='utf-8') as file:
                file.write(modified_content)
            print(f"  Wrote modified file: {new_filename}")
        except Exception as e:
            print(f"  Failed to write modified file '{new_filename}': {e}")
            continue

        # Move original file to Archive folder
        try:
            shutil.move(original_path, archived_path)
            print(f"  Moved original file to archive: {archived_path}")
        except Exception as e:
            print(f"  Failed to move original file '{filename}': {e}")

print("Processing complete.")
