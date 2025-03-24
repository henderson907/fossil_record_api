from operator import truediv

import requests
from datetime import date
import json
from colorama import Fore, Style

def display_fossils_nicely(fossils_dict):
    print(f"{fossils_dict[1]} ({fossils_dict[5]}, {'complete' if fossils_dict[6] == 0 else 'incomplete'}) - "
          f"{fossils_dict[2]}, {fossils_dict[4]} ({fossils_dict[3][5:16]})")

def get_all_fossils_f_e():
    endpoint = "http://127.0.0.1:5000/fossils"
    result = requests.get(endpoint).json()
    return result

def collect_fossil_info():
    # Use of title helps keep database consistent
    new_species = input("Enter species name: ").strip().title()
    new_country = input("Enter country of origin: ").strip().title()
    new_discovered_by = input("Who is to be credited with the discovery?: ").strip().title()
    new_fossil_type = input("Enter fossil type: ").strip()
    new_complete = input("Is the fossil complete? (y/n): ").strip()
    new_complete_bool = True if new_complete == 'y' else False
    new_period = input("Enter period in which fossil belongs (triassic/jurassic/cretaceous): ").strip().title()

    new_fossil_dictionary = {
        "species": new_species,
        "country": new_country,
        "discovered_on": date.today().strftime('%Y-%m-%d'),
        "discovered_by": new_discovered_by,
        "fossil_type": new_fossil_type,
        "complete": new_complete_bool,
        "period": new_period
    }

    return new_fossil_dictionary

def add_new_fossil_f_e(new_fossil_dictionary):
    endpoint = "http://127.0.0.1:5000/fossils/add"
    result = requests.post(
        endpoint,
        headers={'content-type': 'application/json'},
        data=json.dumps(new_fossil_dictionary)
    )

    return result.json()

def find_fossil_by_country_f_e(country):
    endpoint = f"http://127.0.0.1:5000/fossils/{country}"
    result = requests.get(endpoint).json()
    return result



def run():
    running = True
    while running:
        print("\nWelcome esteemed paleontologist to the fossil record!")
        print("-----------------------------------------------------")
        print("Please choose from the following:")
        print("A - View all fossil records")
        print("B - Add a new fossil to the record")
        print("C - View fossils found in specific country")
        print("D - Exit application")
        print("-----------------------------------------------------")

        answer = input("Please select your choice (A/B/C/D): ").strip().upper()

        if answer == "A":
            if get_all_fossils_f_e() is None:
                print(Fore.YELLOW + "Something went wrong. Failed to retrieve records.")
                print(Style.RESET_ALL)
            fossils = get_all_fossils_f_e()
            for x in fossils:
                display_fossils_nicely(x)

        elif answer == "B":
            new_fossil_info = collect_fossil_info()
            fossils = add_new_fossil_f_e(new_fossil_info)
            print(Fore.GREEN + "Congratulations, your fossil has been added!")
            print(Style.RESET_ALL)
            for x in fossils:
                display_fossils_nicely(x)

        elif answer == "C":
            desired_country = input("Please enter your country of interest: ")
            fossils = find_fossil_by_country_f_e(desired_country)
            if fossils:
                for x in fossils:
                    display_fossils_nicely(x)
            else:
                print(Fore.YELLOW + f"Unfortunately we do not have any fossil records from {desired_country}")
                print(Style.RESET_ALL)

        elif answer == "D":
            print(Fore.MAGENTA + "Thank you for using my application")
            print(Style.RESET_ALL)
            running = False

        else:
            print(Fore.RED + "Invalid option. Please try again")
            print(Style.RESET_ALL)



if __name__ == "__main__":
    run()