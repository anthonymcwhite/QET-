import os

def main():
    print("Welcome to EditPy ==> by: anthony mcwhite")
    print("a simple script used for editing text files quickly")
   
    file_name = input("What file are we modifying? ")

    # Check if the file exists
    if not os.path.isfile(file_name):
        print(f"File '{file_name}' does not exist. Please try again.")
        return

    # Open the file in Mousepad editor
    os.system(f"mousepad {file_name}")

    # Ask for the string to be replaced and the replacement
    original_string = input("String to be replaced: ")
    replacement_string = input("Replace with: ")

    # Read the content of the file
    with open(file_name, 'r') as file:
        content = file.read()

    # Replace the string
    content = content.replace(original_string, replacement_string)

    # Write the changes back to the file
    with open(file_name, 'w') as file:
        file.write(content)

    print(f"Replaced '{original_string}' with '{replacement_string}' in '{file_name}'.")

if __name__ == "__main__":
    main()
             
