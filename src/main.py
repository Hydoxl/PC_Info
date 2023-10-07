import webhook
import subprocess

script_path = 'src/info.py'

# Define the main function that sends a webhook


def main():
    # Call the send_webhook function from the webhook module
    webhook.send_webhook()
    try:
        # Use subprocess to execute the script
        subprocess.run(['python', script_path], check=True)
    except FileNotFoundError:
        print(f"File not found: {script_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing the script: {e}")


# Entry point of the script
if __name__ == "__main__":
    # Call the main function when the script is executed
    main()
