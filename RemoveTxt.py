import os

def remove_txt_files(directory):
    # Loop through each file in the directory
    for filename in os.listdir(directory):
        # Check if the file has a .txt extension
        if filename.endswith(".txt"):
            # Create the file path
            file_path = os.path.join(directory, filename)
            # Remove the file
            os.remove(file_path)
            print(f"Removed: {file_path}")

# Example usage
directory_path = "DatasetNotScaled"
remove_txt_files(directory_path)