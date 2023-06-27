import subprocess
import os
from termcolor import colored

# ASCII art
art = colored('''                                                                                                                      
      _                    ______        ____                         _       ______        ____
    // | |     //   / /  /__  ___/     //   ) )     /|    //| |     // | |  /__  ___/     //   ) ) 
   //__| |    //   / /     / /        //   / /     //|   // | |    //__| |    / /        //___/ /  
  / ___  |   //   / /     / /        //   / /     // |  //  | |   / ___  |   / /        / ___ (    
 //    | |  //   / /     / /        //   / /     //  | //   | |  //    | |  / /        //   | |    
//     | | ((___/ /     / /        ((___/ /     //   |//    | | //     | | / /        //    | |  
''', 'red')

print(art)

print("This script automates the manual process of opening URLs.")

# Prompt the user to select an option
while True:
    print("\nOptions:")
    print("1. Open a list of social media search URLs within your browser.")
    print("2. Search for a name across social media.")
    print("3. Configure a list of social media search URLs based on an input list of names.")
    option = input("Select an option (1 or 2): ")

    if option == "1":
        subprocess.call(["python3", "runscan.py"])
        break
    elif option == "2":
        subprocess.call(["python3", "target.py"])
        break
    elif option == "3":
        subprocess.call(["python3", "createlist.py"])
        break
    else:
        print("Invalid option. Please choose 1, 2, or 3.")

