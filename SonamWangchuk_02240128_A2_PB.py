class PokemonCardBinder:
    def __init__(self):
        self.binder = {}
        self.binder_row = 9
        self.binder_column = 9
        self.cards_per_page = self.binder_row * self.binder_column
        self.max_pokedex = 1000

    def add_pokemon_card(self):
        try:
            pokedex = int(input("Enter the number of Pokedex (1-1000): "))
            if not (1 <= pokedex <= self.max_pokedex):
                print("Invalid Pokedex number. It must be between 1 and 1000.")
                return

            if pokedex in self.binder:
                page, row, col = self.binder[pokedex]
                print(f"Page: {page}")
                print(f"Status: Pokedex #{pokedex} already exists in the binder.")
                return

            index = len(self.binder)
            page = index // self.cards_per_page + 1
            pops_on_page = index % self.cards_per_page
            row = pops_on_page // self.binder_column + 1
            col = pops_on_page % self.binder_column + 1

            self.binder[pokedex] = (page, row, col)
            print(f"Page: {page}")
            print(f"Position: Row {row}, Column {col}")
            print(f"Status: Added Pokedex #{pokedex} to binder.")

        except ValueError:
            print("Please enter a valid integer.")

    def reset_binder(self):
        confirm = input('''WARNING: THIS WILL DELETE ALL POKEMON CARDS FROM THE BINDER. Type "CONFIRM" to reset or "EXIT" to cancel: ''')
        if confirm.strip().upper() == "CONFIRM":
            self.binder.clear()
            print("The binder reset was successful! All cards have been removed.")
        else:
            print("Reset canceled. Returning to main menu.")

    def view_binder(self):
        if not self.binder:
            print("The binder is empty.")
        else:
            for pokedex in sorted(self.binder):
                page, row, col = self.binder[pokedex]
                print(f"Pokedex #{pokedex}: Page {page}, Position: Row {row}, Column {col}")

            total = len(self.binder)
            percent = (total / self.max_pokedex) * 100
            print(f"Total cards in binder: {total}")
            print(f"% completion: {percent:.2f}%")
            if total == self.max_pokedex:
                print("You have caught them all!")

    def binder_menu(self):
        while True:
            print("\nWelcome to Pokemon Card Binder Manager!")
            print("Main Menu")
            print("1. Add Pokemon Card")
            print("2. Reset Binder")
            print("3. View Current Placements")
            print("4. Exit")

            choice = input("Select option: ")
            if choice == "1":
                self.add_pokemon_card()
            elif choice == "2":
                self.reset_binder()
            elif choice == "3":
                self.view_binder()
            elif choice == "4":
                print("Thank you for using Pokemon Card Binder Manager!")
                break
            else:
                print("Invalid option. Please select 1-4.")


if __name__ == "__main__":
    binder_manager = PokemonCardBinder()
    binder_manager.binder_menu()