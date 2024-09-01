import os
import time
import win32com.client
import pythoncom
import gc  # Garbage collector interface

def protect_excel(file_path, password):
    # Check if the file exists
    if not os.path.isfile(file_path):
        print("File does not exist.")
        return

    excel = None
    workbook = None
    try:
        # Initialize the COM environment
        pythoncom.CoInitialize()

        # Start Excel application with a new instance
        excel = win32com.client.DispatchEx("Excel.Application")

        # Open the workbook in read/write mode
        workbook = excel.Workbooks.Open(os.path.abspath(file_path))

        # Define a temporary file path for saving the password-protected file
        directory, filename = os.path.split(file_path)
        temp_file_path = os.path.join(directory, "protected_" + filename)

        # Save the workbook with password protection
        workbook.SaveAs(Filename=os.path.abspath(temp_file_path), FileFormat=51, Password=password)

        # Close the workbook
        workbook.Close(SaveChanges=True)
        time.sleep(1)  # Small delay to ensure the file is released

        # Quit Excel application
        excel.Quit()

        # Force garbage collection to release COM objects
        del workbook
        del excel







