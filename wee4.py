def read_and_modify_file(input_filename, output_filename):
    try:
       
        with open(input_filename, "r") as infile:
          
            content = infile.read()

        
        modified_content = content.upper()

        
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)
        
        print(f"File has been successfully modified and saved to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError:
        print(f"Error: The file '{input_filename}' could not be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


input_filename = input("Enter the name of the input file: ")
output_filename = input("Enter the name of the output file: ")


read_and_modify_file(input_filename, output_filename)
