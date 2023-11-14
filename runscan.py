import webbrowser
import random
import time

BATCH_SIZE = 3


def open_urls_from_file(file_name):
    with open(file_name, 'r') as file:
        urls = file.readlines()

        num_urls = len(urls)
        num_batches = num_urls // BATCH_SIZE

        for i in range(num_batches):
            batch_urls = urls[i * BATCH_SIZE: (i + 1) * BATCH_SIZE]

            for url in batch_urls:
                webbrowser.open(url.strip())

            if i < num_batches - 1:
                # Randomized delay between batches
                delay = random.uniform(2, 5)  # Adjust the range as needed
                time.sleep(delay)

        remaining_urls = urls[num_batches * BATCH_SIZE:]
        for url in remaining_urls:
            webbrowser.open(url.strip())


# Prompt the user to sign in to Facebook
print("Please sign in to Facebook within your web browser.")

# Prompt the user to confirm sign-in
while True:
    confirm_sign_in = input("Have you signed in to Facebook? (Y/N): ")
    if confirm_sign_in.lower() == 'y':
        break
    elif confirm_sign_in.lower() == 'n':
        print("Please sign in to Facebook before proceeding.")
    else:
        print("Invalid input. Please enter Y or N.")

# Prompt the user to input the file name
file_name = input("Enter the file name (TXT) with URLs: ")

# Call the function to open URLs from the file
open_urls_from_file(file_name)
