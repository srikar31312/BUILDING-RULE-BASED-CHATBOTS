import re, random
from colorama import Fore, init

init(autoreset=True)

destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "California", "New York"]
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travellers always feel warm? Because of all their hot spots!"
]

memory = {
    "name": None,
    "last_destination": None
}

def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

def save_history(user, bot):
    with open("chat_history.txt", "a", encoding="utf-8") as f:
        f.write(f"User: {user}\n")
        f.write(f"Bot: {bot}\n")

def load_history():
    try:
        with open("chat_history.txt", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""

def recommend():
    print(Fore.CYAN + "TravelBot: Beaches, mountains, or cities??")
    preference = input(Fore.YELLOW + "You: ")
    preference = normalize_input(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        memory["last_destination"] = suggestion
        print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
        print(Fore.CYAN + "TravelBot: Do you like it?? (yes/no)")
        answer = input(Fore.YELLOW + "You: ")

        if answer == "yes":
            reply = f"Awesome! Enjoy {suggestion}!"
            print(Fore.GREEN + f"TravelBot: {reply}")
            save_history(answer, reply)
        elif answer == "no":
            print(Fore.RED + "TravelBot: Let's try another.")
            recommend()
        else:
            print(Fore.RED + "TravelBot: I'll suggest again.")
            recommend()
    else:
        reply = "Sorry, I don't have that type of destination."
        print(Fore.RED + "TravelBot: " + reply)
        save_history(preference, reply)

    show_help()

def packing_tips():
    print(Fore.CYAN + "TravelBot: Where to??")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TravelBot: How many days?")
    days = input(Fore.YELLOW + "You: ")

    reply = f"Packing tips for {days} days in {location}:"
    print(Fore.GREEN + f"TravelBot: {reply}")
    print(Fore.GREEN + "- Pack versatile clothes.")
    print(Fore.GREEN + "- Bring chargers/adapters.")
    print(Fore.GREEN + "- Check the weather forecast.")

    save_history(location, reply)

def tell_joke():
    joke = random.choice(jokes)
    print(Fore.YELLOW + f"TravelBot: {joke}")
    save_history("joke", joke)

def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- Suggest travel spots (say 'recommendation')")
    print(Fore.GREEN + "- Offer packing tips (say 'packing')")
    print(Fore.GREEN + "- Tell a joke (say 'joke')")
    print(Fore.GREEN + "- Recall last destination (say 'memory')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")

def recall_memory():
    if memory["last_destination"]:
        reply = f"Last time I suggested {memory['last_destination']}!"
    else:
        reply = "I don’t remember any past destination yet."
    print(Fore.CYAN + "TravelBot: " + reply)
    save_history("memory check", reply)

def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot.")
    name = input(Fore.YELLOW + "Your name? ")
    memory["name"] = name
    print(Fore.GREEN + f"Nice to meet you, {name}!")

    history = load_history()
    if history:
        print(Fore.MAGENTA + "\n--- Past Conversations ---")
        print(history)
        print(Fore.MAGENTA + "--\n")

    show_help()

    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        norm_input = normalize_input(user_input)
        save_history(user_input, "")

        if "recommend" in norm_input or "suggest" in norm_input:
            recommend()
        elif "pack" in norm_input or "packing" in norm_input:
            packing_tips()
        elif "joke" in norm_input or "funny" in norm_input:
            tell_joke()
        elif "memory" in norm_input:
            recall_memory()
        elif "help" in norm_input:
            show_help()
        elif "exit" in norm_input or "bye" in norm_input:
            reply = "Safe travels! Goodbye!"
            print(Fore.CYAN + "TravelBot: " + reply)
            save_history(user_input, reply)
            break
        else:
            reply = "Could you rephrase?"
            print(Fore.RED + "TravelBot: " + reply)
            save_history(user_input, reply)

if __name__ == "__main__":
    chat()