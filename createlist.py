import csv
import urllib.parse


def generate_urls(name):
    encoded_name = urllib.parse.quote(name)
    facebook_url = f"https://www.facebook.com/search/people/?q={encoded_name}"
    nitter_url = f"https://nitter.net/search?f=users&q={encoded_name}"
    picuki_url = f"https://www.picuki.com/search/{encoded_name}"
    return [facebook_url, nitter_url, picuki_url]


def process_file(input_file, output_file):
    with open(input_file, 'r') as file:
        reader = csv.reader(file) if input_file.endswith('.csv') else file.readlines()
        urls = []
        for row in reader:
            name = row.strip() if isinstance(row, str) else row[0].strip()
            generated_urls = generate_urls(name)
            urls.extend(generated_urls)

    with open(output_file, 'w') as file:
        for url in urls:
            file.write(url + '\n')

    print(f"URLs generated and saved to {output_file}")


# Prompt the user to input the source file name
input_file = input("Enter the source file name (CSV or TXT): ")

# Prompt the user to input the output file name
output_file = input("Enter the output file name (TXT): ")

process_file(input_file, output_file)
