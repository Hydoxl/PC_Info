import subprocess

# Define the path to the main.py file in the src subfolder
main_script_path = "src/main.py"

# Use subprocess to run the main.py script
try:
    subprocess.run(["python", main_script_path])
except FileNotFoundError:
    print(f"Error: The file {main_script_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
