from lib import *
import requests

clearConsole()

Path("./avatars").mkdir(exist_ok=True)

list_of_category = ["male", "female", "human", "identicon", "initials", "bottts", "avataaars", "jdenticon", "gridy" , "micah"]

response = requests. get(f"https://avatars.dicebear.com/api/{list_of_category[random.randint(0,len(list_of_category)-1)]}/{str(random.randint(0,111111111111111))}.svg")

with open("./avatars/avatar.svg" , "wb") as file:
    file.write(response.content)

os.system("open avatar.svg")
