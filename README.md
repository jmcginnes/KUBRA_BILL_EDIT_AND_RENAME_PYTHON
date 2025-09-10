
# KUBRA XML File Modifier and Renamer

## Overview

This Python script automates the process of modifying and renaming XML files in a specified directory. It:

- Searches for `.xml` files in the configured folder
- Add a comment to the XML to allow the same file to be resent to Kubra
- Renames each modified file by appending user initials and the current date (e.g., `_JM_06192025`)
- Moves the original files into an `Archive` folder to keep backups

This helps prepare files for file transfer processes that detect duplicates, by ensuring content changes and unique filenames.

---


## Usage Instructions

1. **Add your XML files**
   Place all the `.xml` files you want to modify inside the folder you set as `FOLDER_PATH` in the `.env` file (for example, the `KUBRA_BILLS_TO_EDIT` folder).

2. **Run the script**
   Double-click the `main.py` file or run it from your command line:

   ```bash
   python main.py
   ```

3. **Enter your initials**
   When prompted in the shell/console, type your initials (e.g., `JM`) and press Enter.

4. **Let the script work**
   The script will:

   * Modify each XML file by adding a comment within the XML.
   * Save the modified files with your initials and the current date appended.
   * Move the original files to an `Archive` folder located next to the script for safekeeping.

5. **Check your folder**
   After completion, the edited files will be in the original folder with new names, and originals will be safely archived.

---

## Notes

* Make sure to back up files before running the script, just in case.
* Only `.xml` files in the specified folder are processed.
* The `Archive` folder is created automatically if it does not exist.

---

## Contributing

Feel free to open issues or submit pull requests if you want to add features or fix bugs!

---

## Contact

Created by John McGinnes

```
