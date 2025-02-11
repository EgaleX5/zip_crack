import os
import time
import zipfile
import multiprocessing
from tqdm import tqdm  # For progress bar
import logging

# ANSI color codes for styling
GREEN = "\033[1;32m"
RED = "\033[1;31m"
CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"

# Set up logging
logging.basicConfig(level=logging.INFO)

# Banner with red color and center alignment
banner = """
\033[1;31m
===========================================🦅
           E G A L E X 5
     --- Hacking is not a crime, it's skills ---
===========================================
    EgaleX5 - Zip Password Cracker
===========================================
\033[0m
"""

# Function to create a typewriter effect for the banner
def print_banner_with_effect():
    os.system('clear')  # Clear the terminal screen before displaying the banner
    for char in banner:
        print(char, end='', flush=True)
        time.sleep(0.05)  # Delay between each character to create animation effect

# Function to display a loading animation
def loading_animation(text):
    for i in range(3):
        print(f"{CYAN}{text}{'.' * (i + 1)}{RESET}", end="\r")
        time.sleep(0.5)

# Function to attempt opening the ZIP file with a password
def try_password(zip_path, password):
    try:
        with zipfile.ZipFile(zip_path) as zf:
            zf.setpassword(password.encode())  # Set password and try to extract
            if zf.testzip() is None:
                return password  # Return password if the extraction is successful
    except Exception:
        pass
    return None

# Function to attempt cracking a chunk of passwords
def crack_chunk(zip_path, chunk, result_queue):
    for password in tqdm(chunk, desc="Cracking", unit="password"):
        found_password = try_password(zip_path, password)
        if found_password:
            result_queue.put(found_password)  # If password is found, add it to the queue
            break

# Function to manage multiprocessing and distribute workload
def start_cracking(zip_path, wordlist):
    start_time = time.time()
    result_queue = multiprocessing.Queue()

    # Read the wordlist in chunks and distribute to processes
    with open(wordlist, 'r') as file:
        wordlist_lines = [line.strip() for line in file.readlines()]

    num_processes = multiprocessing.cpu_count()  # Use as many processes as CPU cores
    chunk_size = len(wordlist_lines) // num_processes
    chunks = [wordlist_lines[i:i + chunk_size] for i in range(0, len(wordlist_lines), chunk_size)]

    # Set up and start processes
    processes = []
    for chunk in chunks:
        process = multiprocessing.Process(target=crack_chunk, args=(zip_path, chunk, result_queue))
        processes.append(process)
        process.start()

    # Wait for processes to finish
    for process in processes:
        process.join()

    # Check if any password was found
    if not result_queue.empty():
        password = result_queue.get()
        logging.info(f"{GREEN}SUCCESS: Found your password: {password}{RESET}")
    else:
        logging.error(f"{RED}FAILED: Password not found in the wordlist.{RESET}")

    end_time = time.time()
    logging.info(f"{CYAN}Completed in {end_time - start_time:.2f} seconds{RESET}")

# Main function to get user input and start the cracking process
def main():
    # Display banner with typewriter effect
    print_banner_with_effect()

    # Display loading animation
    loading_animation("Initializing")
    time.sleep(0.5)

    # Taking input from the user
    zip_file_path = input(f"{CYAN}Enter the path to the ZIP file: {RESET}")  # Path to the ZIP file
    wordlist_file = input(f"{CYAN}Enter the path to the wordlist file: {RESET}")  # Path to the wordlist file

    # Validate the ZIP file and wordlist path
    if not os.path.isfile(zip_file_path):
        logging.error(f"{RED}Error: ZIP file not found.{RESET}")
        return
    if not os.path.isfile(wordlist_file):
        logging.error(f"{RED}Error: Wordlist file not found.{RESET}")
        return

    logging.info(f"{YELLOW}Starting the password cracking process...{RESET}")
    loading_animation("Processing")
    print("\n")
    start_cracking(zip_file_path, wordlist_file)

# Run the script
if __name__ == "__main__":
    main()
