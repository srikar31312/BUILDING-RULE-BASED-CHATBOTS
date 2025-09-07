import re, random
from colorama import Fore, init

# Initialize colorama (auto reset ensures each print resets after use)
init(autoreset=True)

# Destination and joke data
destinations= {
    "beaches": ["Bali","Maldives","phuket"],
    "mountains":["Swiss alps","Rocky mountains","Himalayas"],
    "cities": ["Tokyo","California","newyork"]
}
jokes= [
    "why dont programmers like nature? Too many bugs"
    "why did the computer go to the doctor? Because it had virus"
    "Why do travellers always feel warn? Beacuse of all their hot spots!"
]

# Helper function to normalize user input (remove extra spaces ,make lowercase)
def normalize_input(text):
    return re.sub(r"\s+"," ",text.strip().lower())

# provide travel recommendationb(recursive if user rejects the suggestions)
def recommend():
    print(Fore.CYAN + "TravelBot: Beaches, mountains,or cities??")
    preference =input(Fore.YELLOW + "You: ")
    preference =normalize_input(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN +f"TravelBot: How about {suggestion}?")
        print(Fore.CYAN + "TravelBot: Do you like it?? (yes/no)")
        answer = input(Fore.YELLOW + "You: ")

        if answer =="yes":
            print(Fore.GREEN + f"TravelBot: Awesome! Enjoy {suggestion}!")
        elif answer == "no":
            print(Fore.RED + "TravelBot: Lets try another.")
            recommend()
        else:
            print(Fore.RED + "TravelBot:I'll suggest again.")
            recommend()
    else:
        print(Fore.RED + "TravelBot: Sorry, I dont have that type of destination.")

    show_help()
    
# Offer packing tips based on user's destination and duration
def packing_tips():
    print(Fore.CYAN +"TravelBot:Where to??")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TravelBot: HOw many days?")
    days = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"TravelBot: packing tips for {days} days in {location}:")
    print(Fore.GREEN + "- Pack versatile cloths.")
    print(Fore.GREEN + "- Bring chargers/adapters.")
    print(Fore.GREEN + "- check the weather forecast.")

# Tell a random joke
def tell_joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")

# Display Help Menu
def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- suggest travel spots (say 'recommendation')")
    print(Fore.GREEN + "- offer packing tips(say'packing')")
    print(Fore.GREEN + "-Tell a joke (say 'joke')")
    print(Fore.CYAN + "Type 'exit'or byr to end.\n")

# Main chat loop
def chat():
    print(Fore.CYAN + "Hello! I'm Travel bot.")
    name = input(Fore.YELLOW + "Your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}!")

    show_help()

    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input =normalize_input(user_input)

        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack"in user_input or "packing" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break
        else:
            print(Fore.RED + "TravelBot: Could you rephrase?")

# Run the chatbot
if __name__ == "__main__":
    chat()
    