import os

def add_license(file_path, license_text):
    with open(file_path, 'r') as file:
        content = file.read()

    with open(file_path, 'w') as file:
        # Check if the license is already present
        if license_text not in content:
            # Add the license at the beginning of the file
            file.write(license_text + '\n\n' + content)
            print(f"License added to: {file_path}")
        else:
            print(f"License already present in: {file_path}")

def process_directory(directory_path, license_text):
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            if file_name.endswith(('.c', '.h')):
                file_path = os.path.join(root, file_name)
                add_license(file_path, license_text)

def main():
    # Specify your license text
    license_text = """
    license abc
    2024
    blablabla
    """

    # Get the current directory
    current_directory = os.getcwd()

    # Process the current directory and its subdirectories
    process_directory(current_directory, license_text)

if __name__ == "__main__":
    main()