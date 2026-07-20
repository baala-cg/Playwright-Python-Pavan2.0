import fileoperations as fo
import os

print(os.getcwd())


# Example usage
file_path = os.getcwd() + "\\files"
file1 = file_path + "\\myfile.txt"
file2 = file_path + "\\myfile1.txt"

# Write to file
fo.write_to_file(file1, "Welcome to Python \n File Handling")

# Append to file
fo.append_to_file(file1, "\nThis line is appended.")

# Read file
print(fo.read_file(file1, "all"))

# Rename file
fo.rename_file(file1, file2)

# Delete file
fo.delete_file(file2)

# Directory operations
dir_path = file_path + "\\mydir"
fo.create_directory(dir_path)
print("Directory exists:", fo.check_directory_exists(dir_path))
fo.rename_directory(dir_path, file_path + "\\mydir1")
fo.remove_directory(file_path + "\\mydir1", force=False)

# Current working directory
print("CWD:", fo.get_current_working_directory())


