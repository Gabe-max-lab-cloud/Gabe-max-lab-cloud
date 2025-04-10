import easygui
easygui.buttonbox("Do you want to continue?", choices = ["Yes", "No"])

# Initial monster catalogue
monster_catalogue = {
    "Stoneling": {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
    "Vexscream": {"Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
    "Dawnmirage": {"Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22},
    "Blazegolem": {"Strength": 15, "Speed": 20, "Stealth": 23, "Cunning": 6},
    "Websnake": {"Strength": 7, "Speed": 15, "Stealth": 10, "Cunning": 5},
    "Moldvine": {"Strength": 21, "Speed": 18, "Stealth": 14, "Cunning": 5},
    "Vortexwing": {"Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2},
    "Rotthing": {"Strength": 16, "Speed": 7, "Stealth": 4, "Cunning": 12},
    "Froststep": {"Strength": 14, "Speed": 14, "Stealth": 17, "Cunning": 4},
    "Wispghoul": {"Strength": 17, "Speed": 19, "Stealth": 3, "Cunning": 2},
}

CATEGORY_NAMES = ["Strength", "Speed", "Stealth", "Cunning"]

def get_monster_stats():
    stats = {}
    for category in CATEGORY_NAMES:
        while True:
            value = easygui.integerbox(f"Enter {category} (1-25):", lowerbound=1, upperbound=25)
            if value is None:
                return None
            stats[category] = value
            break
    return stats

def add_monster():
    name = easygui.enterbox("Enter monster name:")
    if name:
        if name in monster_catalogue:
            easygui.msgbox(f"{name} already exists.")
            return
        stats = get_monster_stats()
        if stats is None:
            return
        confirm = easygui.ynbox(f"Add {name} with stats: {stats}?", choices=["Yes", "No"])
        if confirm:
            monster_catalogue[name] = stats
            easygui.msgbox(f"{name} added successfully!")

def search_monster():
    name = easygui.enterbox("Enter monster name to search/edit:")
    if name in monster_catalogue:
        stats = monster_catalogue[name]
        change = easygui.ynbox(f"{name} stats: {stats}\nEdit?", choices=["Yes", "No"])
        if change:
            new_stats = get_monster_stats()
            if new_stats:
                monster_catalogue[name] = new_stats
                eeasygui.msgbox(f"{name} updated.")
    else:
        easygui.msgbox(f"{name} not found.")

def delete_monster():
    name = easygui.enterbox("Enter monster name to delete:")
    if name in monster_catalogue:
        confirm = easygui.ynbox(f"Delete {name}?", choices=["Yes", "No"])
        if confirm:
            del monster_catalogue[name]
            easygui.msgbox(f"{name} deleted.")
    else:
        easygui.msgbox(f"{name} not found.")

def show_catalogue():
    if not monster_catalogue:
        easygui.msgbox("The catalogue is currently empty.")
    else:
        output = "\n".join([f"{name}: {stats}" for name, stats in monster_catalogue.items()])
        easygui.codebox("Full Catalogue", text=output)

def main_menu():
    while True:
        choice = easygui.buttonbox(
            "Choose an action:",
            choices=["Add Monster", "Search/Edit Monster", "Delete Monster", "Show Catalogue", "Exit"]
        )
        if choice == "Add Monster":
            add_monster()
        elif choice == "Search/Edit Monster":
            search_monster()
        elif choice == "Delete Monster":
            delete_monster()
        elif choice == "Show Catalogue":
            show_catalogue()
        elif choice == "Exit":
            break

if __name__ == "__main__":
    main_menu()

