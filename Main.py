import json
import os
from datetime import datetime

TODO_FILE = 'tasks.json'

def charger_taches():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

def sauvegarder_taches(taches):
    with open(TODO_FILE, 'w') as file:
        json.dump(taches, file, indent=4)

def afficher_taches(taches):
    if not taches:
        print("Aucune tache a afficher.")
        return
    for idx, tache in enumerate(taches, start=1):
        status = "[x]" if tache['completed'] else "[ ]"
        priority = f"(Priorite: {tache['priority']})"
        due_date = f"(Date d'echeance: {tache['due_date']})" if tache['due_date'] else ""
        category = f"(Categorie: {tache['category']})" if tache['category'] else ""
        tags = f"(Etiquettes: {', '.join(tache['tags'])})" if tache['tags'] else ""
        print(f"{idx}. {status} {tache['description']} {priority} {due_date} {category} {tags}")

def ajouter_tache(taches, description, priority, due_date=None, category=None, tags=None):
    tache = {
        'description': description,
        'completed': False,
        'priority': priority,
        'due_date': due_date,
        'category': category,
        'tags': tags or []
    }
    taches.append(tache)
    sauvegarder_taches(taches)
    print(f"Tache ajoutee : {description} (Priorite: {priority})")

def completer_tache(taches, numero_tache):
    if 1 <= numero_tache <= len(taches):
        taches[numero_tache - 1]['completed'] = True
        sauvegarder_taches(taches)
        print(f"Tache {numero_tache} marquee comme terminee.")
    else:
        print("Numero de tache invalide.")

def supprimer_tache(taches, numero_tache):
    if 1 <= numero_tache <= len(taches):
        tache_supprimee = taches.pop(numero_tache - 1)
        sauvegarder_taches(taches)
        print(f"Tache supprimee : {tache_supprimee['description']}")
    else:
        print("Numero de tache invalide.")

def rechercher_taches(taches, mot_cle):
    return [tache for tache in taches if mot_cle.lower() in tache['description'].lower()]

def filtrer_taches(taches, filtre):
    if filtre == 'completed':
        return [tache for tache in taches if tache['completed']]
    elif filtre == 'incomplete':
        return [tache for tache in taches if not tache['completed']]
    elif filtre == 'high_priority':
        return [tache for tache in taches if tache['priority'] == '++']
    elif filtre == 'medium_priority':
        return [tache for tache in taches if tache['priority'] == '+']
    elif filtre == 'low_priority':
        return [tache for tache in taches if tache['priority'] == '-']
    else:
        return taches

def afficher_statistiques(taches):
    total_taches = len(taches)
    taches_completes = len([tache for tache in taches if tache['completed']])
    taches_incompletes = total_taches - taches_completes
    print(f"Taches effectuees : {taches_completes}")
    print(f"Taches non effectuees : {taches_incompletes}")
    print(f"Total des taches : {total_taches}")

def afficher_bienvenue():
    print(r"""

  _____    _______        _    __  __
 |  __ \  |__   __|      | |  |  \/  |
 | |__) |   _| | __ _ ___| | _| \  / | __ _ _ __   __ _
 |  ___/ | | | |/ _` / __| |/ / |\/| |/ _` | '_ \ / _` |
 | |   | |_| | | (_| \__ \   <| |  | | (_| | | | | (_| |
 |_|    \__, |_|\__,_|___/_|\_\_|  |_|\__,_|_| |_|\__,_|
         __/ |
        |___/
    """)
    print("Bienvenue dans PyTaskMana !")

def main():
    taches = charger_taches()
    afficher_bienvenue()
    afficher_statistiques(taches)
    while True:
        print("\n1. Afficher les taches")
        print("2. Ajouter une tache")
        print("3. Marquer une tache comme terminee")
        print("4. Supprimer une tache")
        print("5. Rechercher une tache")
        print("6. Filtrer les taches")
        print("7. Quitter")
        choix = input("Choisissez une option : ")
        if choix == '1':
            afficher_taches(taches)
        elif choix == '2':
            description = input("Entrez la description de la tache : ")
            priority = input("Entrez la priorite de la tache (++, +, -) : ")
            due_date = input("Entrez la date d'echeance : ")
            category = input("Entrez la categorie (facultatif) : ")
            tags = input("Entrez les etiquettes (separees par des virgules, facultatif) : ").split(',')
            ajouter_tache(taches, description, priority, due_date, category, tags)
        elif choix == '3':
            numero_tache = int(input("Entrez le numero de la tache a marquer comme terminee : "))
            completer_tache(taches, numero_tache)
        elif choix == '4':
            numero_tache = int(input("Entrez le numero de la tache a supprimer : "))
            supprimer_tache(taches, numero_tache)
        elif choix == '5':
            mot_cle = input("Entrez le mot-cle a rechercher : ")
            resultats = rechercher_taches(taches, mot_cle)
            afficher_taches(resultats)
        elif choix == '6':
            filtre = input("Entrez le filtre (completed, incomplete, high_priority, medium_priority, low_priority) : ")
            resultats = filtrer_taches(taches, filtre)
            afficher_taches(resultats)
        elif choix == '7':
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez reessayer.")

if __name__ == "__main__":
    main()
