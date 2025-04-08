def read_and_modify_file(input_filename, output_filename):
    try:
        # Try to open the input file and read the content
        with open(input_filename, 'r') as file:
            content = file.read()
        
        # Modify the content (for example, converting it to uppercase)
        modified_content = content.upper()
        
        # Write the modified content to a new output file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        
        print(f"Content has been successfully modified and written to {output_filename}")

    except FileNotFoundError:
        # Handle the case where the input file does not exist
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        # Handle any IO related errors (e.g., permission issues)
        print(f"Error: There was an issue reading or writing to the file.")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")

def main():
    # Ask the user for the input filename
    input_filename = input("Please enter the input file name: ")
    
    # Ask for the output filename
    output_filename = input("Please enter the output file name: ")

    # Call the function to read, modify, and write the file
    read_and_modify_file(input_filename, output_filename)

# Run the program
if __name__ == "__main__":
    main()
