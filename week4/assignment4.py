
def read_and_modify_file():
    try:
        # Ask user for input file name
        input_filename = input("Enter the filename to read from: ")

        # Try to open and read the file
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Ask user for output file name
        output_filename = input("Enter the filename to write the modified content to: ")

        # Write the modified content to a new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"sFile successfully written to '{output_filename}'")

    except FileNotFoundError:
        print(" Error: The file you entered does not exist.")
    except PermissionError:
        print("Error: Permission denied when trying to read/write the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()
