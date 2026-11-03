from colorama import Fore, Style, Init 
import random

init = Init(autoreset=True)

niveis = ["Nível 1", "Nível 2", "Nível 3", "Nível 4", "Nível 5"]

print("Níveis do reservatório:")

for nivel in niveis:
    print(f"{Fore.GREEN}{nivel}{Style.RESET_ALL}")