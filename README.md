### Purpose
This script separates and saves SDL (Skills Development Levy) PDF files locally.

Manually, the workflow would look like such:
1. Manually scrutinize and separate PDFs in ilovepdf
2. Manually click into and rename PDFs individually

Which sounds simple, but consider the fact that together, the pdfs consist of ~1500 pages.

This script automates the process. It is functional enough to run on my work laptop.

### Technologies
- tesseract (tesserocr) <br>
A relatively lightweight OCR engine. After all, the documents are scanned and relatively readable.
- opencv (cv2) <br>
Used in the preprocessing pipeline. Helps to increase the accuracy of tesseract's results.

### Acknowledged limitations
- No error handling <br>
I physically opened and scanned all of the physical letters, personally validating all the input.
- Long processing time <br>
It took about ~50 minutes to process 1498 pages. This could be resolved by parallel processing, but for a one-off script I thought it unnecessary.
- No tests <br>
The script is functionally simple and short. Furthermore, it will be run yearly at most.

### Setup
I cannot imagine why anyone aside from me would need to run this script. The following instructions are for beginners (or for Kat if she eventually finds this in coming years)

0. Install git
    Open Windows Powershell and copy paste this into the terminal
    ```bash
    winget install --id Git.Git -e --source winget
    ```

1. Clone the repo
    ```bash
    git clone <https://github.com/Fury1755/SDLFileSplitter>
    ```

2. Install dependencies (tesseract wheel is automatically handled)
    ```bash
    uv sync
    ```

3. Download and run the tesseract installer from
    ```bash
    https://github.com/UB-Mannheim/tesseract/wiki
    ```

4. Find the path pointing to the folder 'tessdata'

    If you installed it globally it should be in "C:\Program Files\Tesseract-OCR\tessdata".

    If you installed it on your user profile (if you have no admin perms) it should be in "C:\Users\YOUR_WINDOWS_USERNAME_HERE\AppData\Local\Programs\Tesseract-OCR\tessdata".

5. Create a .env file in the project root (copy paste into powershell)
    ```bash
    cd (Get-ChildItem -Directory -Filter "*SDLUploader").FullName
    New-Item -Path .env -ItemType File -Force
    ```

6. Using the tessdata path, configure .env and other variables

    Open the.env file with Notepad (assuming you don't use any other text editors) and type in your environment variables using '.env.example' as an example.

7. Go back to powershell and run the script
    ```bash
    uv run python -m src.main
    ```
