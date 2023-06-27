import webbrowser
import urllib.parse

def create_and_open_urls():
    name = input("Enter a name: ")

    # Create and open Facebook URL
    facebook_url = f"https://www.facebook.com/search/top/?q={urllib.parse.quote(name)}"
    webbrowser.open(facebook_url)

    # Create and open Nitter URL
    nitter_url = f"https://nitter.net/search?f=users&q={urllib.parse.quote(name)}"
    webbrowser.open(nitter_url)

    # Create and open Picuki URL
    picuki_url = f"https://www.picuki.com/search/{urllib.parse.quote(name)}"
    webbrowser.open(picuki_url)

# Call the function to create and open URLs
create_and_open_urls()
