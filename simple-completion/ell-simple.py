from dotenv import load_dotenv
import ell
import random

# Load environment variables from a .env file
load_dotenv()

# Define a function to generate a haiku using ell
@ell.simple(model="gpt-4o")
def write_a_haiku(name: str, temperature: float=0.3):
    """ You are a helpful assistant. """ # System Prompt
    return f"Say hello to {name} and write a short positive haiku for them" # User prompt

# Alternative Message Formats
# Define a function to generate a DnD monster sheet using ell
@ell.simple(model="gpt-4o")
def write_dnd_monster_sheet(name: str, temperature: float=0.3):
    """You are math calculator only knowning numbers""" 
    # Docstring doesn't matter if ell.system is specified explicitly
    return [
        ell.system("You are a dnd 5th edition monster generator"),
        ell.user(f"Generate a monster character sheet for dnd campaign with name as {name}"),
        ell.assistant("Hello! I'd happy to mould the monster for you"),
        ell.user("Great, Could you create a tragic back story of monster of level 2 in 20 words.")
    ]

# Prompting as Language Model Programming
# Define a function to get a random culture with rich mythology
def get_random_choice() -> str:
    """Returns a random culture with rich mythology."""
    cultures_with_rich_mythology = [
        "Egyptian",
        "Japanese",
        "Indian",
        "Greek",
        "Norse",
        "Celtic",
        "Mayan"
    ]
    return random.choice(cultures_with_rich_mythology)

# Define a function to name a deity from a random culture
@ell.simple(model="gpt-4o")
def name_a_deity(name: str, temperature: float=0.3):
    culture = get_random_choice()
    return [
        ell.system("You are a expert in mythology from various cultures"),
        ell.user(f"Could you name the diety of {name} from the {culture} culture")
    ]

# Initialize ell with verbose output for debugging
ell.init(verbose=True)

# # Generate a haiku for Sam Altman
# greeting = write_a_haiku("Sam Altman")
# print(greeting)

# Generate a DnD monster character sheet for Shiv
monster_dnd_maker = write_dnd_monster_sheet("Shiv")
print(monster_dnd_maker)

# Generate a deity name for the element 'Wind' from a random culture
diety_seeker = name_a_deity("Wind")
print(diety_seeker)


"""
a regular Python function into a Language Model Program (LMP). Here's what's happening:

The function's docstring becomes the system message.
The return value of the function becomes the user message.
The decorator handles the API call and returns the model's response as a string.

This encapsulation allows for cleaner, more reusable code. You can now call your LMP like any other Python function.
"""

"""
SECOND APPROACH specified ell.user and ell.system

This approach allows you to construct more complex conversations within your LMP. Importantly, you'll want to use this approach when you have a variable system prompt because python only allows you to have a static docstring.
"""

"""
One of ell's most powerful features is its treatment of prompts as programs rather than simple strings
"""