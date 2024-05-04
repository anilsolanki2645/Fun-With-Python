""" PDF Password Cracking For 4 Digit password """

import pikepdf
from tqdm import tqdm
import random
from datetime import datetime
import time

start_time = datetime.now()

# Set the range for random passwords
password_range = (1000, 9999+1)

# Specify the PDF file path
pdf_file_path = "PDF-protected.pdf"

while True:
    # Generate a random password within the specified range
    password_to_find = random.randint(*password_range)

    # Use tqdm with a range of 1 to show progress (1 iteration for trying one password)
    for _ in tqdm(range(1), desc="Decrypting PDF", unit="password"):
        try:
            # open PDF file
            with pikepdf.open(pdf_file_path, password=str(password_to_find)) as pdf:
                # Password decrypted successfully, break out of the loop
                print("[+] Password found:", password_to_find)
                with open('pssp_found.txt', 'w') as file:
                  file.write(str(password_to_find))
                break
            
        except pikepdf._core.PasswordError as e:
            # wrong password, just continue in the loop
            print("[-] Incorrect password:", password_to_find)
            continue

end_time = datetime.now()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the start and end times, as well as the elapsed time
print("Start Time:", start_time.strftime("%H:%M:%S"))
print("End Time:", end_time.strftime("%H:%M:%S"))
print("Elapsed Time:", str(elapsed_time))
