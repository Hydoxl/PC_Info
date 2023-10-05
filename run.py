import subprocess

main_script_path = "src/main.py"

try:
    subprocess.run(["python", main_script_path])
except FileNotFoundError:
    print(f"Error: The file {main_script_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")