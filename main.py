import os
import time
from yaspin import yaspin
from rich.console import Console
from pyfiglet import Figlet

console = Console()
f = Figlet(font='colossal', width=80)
os.system('cls' if os.name == 'nt' else 'clear')

def wait_and_clear(t):
    time.sleep(t)
    os.system('cls' if os.name == 'nt' else 'clear')

for text in ['b', 'br', 'bra', 'brag', 'bragi']:
    console.print(f.renderText(text))
    wait_and_clear(0.1)

for i in range(3):
    for color in ['blue', 'yellow', 'red']:
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print(f.renderText('bragi'), style = color)
        wait_and_clear(0.1)

console.print(f.renderText('bragi'), style = 'red')

with yaspin(text='Initialisation...', color = 'green') as sp:
    time.sleep(1)
    sp.ok("✔")

with yaspin(text='Chargement des commandes de création...', color = 'green') as sp:
    time.sleep(1)
    sp.ok("✔")

console.print('> [bold green]Sélectionner une action :[/bold green] synthèse(s), apprentissage(a), evaluation(a)')
console.print('$ ', end='')
input() # rentrer "synthese"
console.print('')

with yaspin(text='Synthèse sélectionnée, calcul des paramètres de génération...', color = 'green') as sp:
    time.sleep(1)
    sp.ok("✔")

console.print('> [bold green]Spécifier arguments :[/bold green] timbre --cible, harmonie(harm), percussions(perc)')
console.print('$ ', end='', style = "")
input() # rentrer "timbre sigrid"

os.system('cls' if os.name == 'nt' else 'clear')
console.print('------------------------------', style="cyan")
console.print('Synthèse avec timbre de [bold cyan]Sigrid[/bold cyan]')
console.print('------------------------------', style="cyan")
console.print('')

time.sleep(1.2)
console.print('Initialisation du modèle : ', style = 'bold yellow')
with yaspin(text='Instanciation du modèle sigrid_transformer_latest_v_3_2_3.', color = 'green') as sp:
    time.sleep(0.8); sp.ok("✔")
with yaspin(text='Allocation de l\'espace mémoire.', color = 'green') as sp:
    time.sleep(0.3); sp.ok("✔")
with yaspin(text='Chargement des poids sigrid_weights_v_6.h5 ', color = 'green') as sp:
    time.sleep(0.8); sp.ok("✔")
with yaspin(text='Copie du modèle sur l\'accélérateur GPU ', color = 'green') as sp:
    time.sleep(0.3); sp.ok("✔")
with yaspin(text='Entrée base_harmonique détectée : IN piano_Baard_wg78 ', color = 'green') as sp:
    time.sleep(0.3); sp.ok("✔")
with yaspin(text='En attente du module d\'inférence. ', color = 'green') as sp:
    time.sleep(1.5); sp.ok("✔")

console.print('')
console.print('> Synthèse prête, appuyez sur une touche pour commencer.', style = 'bold green')
input()