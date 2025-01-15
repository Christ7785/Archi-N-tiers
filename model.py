import random  

class Game:
    def __init__(self, nb_max_turn):
        self.__nb_max_turn = nb_max_turn  
        self.__players = []  
        self.__roles = {}  
        self.__alive_players = []  
        self.__current_turn = 0  

    @property
    def nb_max_turn(self):
        return self.__nb_max_turn

    @property
    def current_turn(self):
        return self.__current_turn

    def add_player(self, name):
        """Ajoute un joueur à la liste des joueurs."""
        self.__players.append(name)
 
    def assign_roles(self):
        """Assigne les rôles de manière aléatoire."""
        if len(self.__players) < 4:
            raise ValueError("Le nombre minimum de joueurs est 4.")
        
        roles = ["Loup-Garou", "Loup-Garou"] + ["Villageois"] * (len(self.__players) - 2)
        random.shuffle(roles)  
        self.__roles = dict(zip(self.__players, roles))
        self.__alive_players = self.__players[:]

    def night_phase(self):
        """Phase de nuit où les loups-garous choisissent une victime."""
        print("\n--- Nuit ---")
        wolves = [player for player, role in self.__roles.items() if role == "Loup-Garou" and player in self.__alive_players]
        print(f"Les loups-garous sont : {', '.join(wolves)}")

        victim = random.choice([player for player in self.__alive_players if player not in wolves])
        print(f"Les loups-garous ont choisi de tuer : {victim}")
        self.__alive_players.remove(victim)

    def day_phase(self):
        """Phase de jour où les joueurs votent pour éliminer un suspect."""
        print("\n--- Jour ---")
        print(f"Joueurs encore en vie : {', '.join(self.__alive_players)}")
        vote = input("Votez pour éliminer un joueur : ").strip()
        if vote in self.__alive_players:
            self.__alive_players.remove(vote)
            print(f"{vote} a été éliminé par le village.")
        else:
            print("Vote invalide. Personne n'a été éliminé aujourd'hui.")

    def check_victory(self):
        """Vérifie si une équipe a gagné."""
        wolves = [player for player, role in self.__roles.items() if role == "Loup-Garou" and player in self.__alive_players]
        villagers = [player for player in self.__alive_players if player not in wolves]

        if not wolves:
            print("Les villageois ont gagné !")
            return True
        if len(villagers) <= len(wolves):
            print("Les loups-garous ont gagné !")
            return True
        return False

    def play(self):
        """Lance le jeu."""
        self.assign_roles()
        print("\nLes rôles ont été attribués. Chaque joueur connaît son rôle.")
        for player, role in self.__roles.items():
            print(f"{player}, votre rôle est : {role}")
        
        while self.__current_turn < self.__nb_max_turn:
            print(f"\n--- Tour {self.__current_turn + 1} ---")
            self.night_phase()
            if self.check_victory():
                break
            self.day_phase()
            if self.check_victory():
                break
            self.__current_turn += 1

        if self.__current_turn == self.__nb_max_turn:
            print("Le jeu atteint le nombre maximum de tours. Personne ne gagne.")


if __name__ == "__main__":
    game = Game(nb_max_turn=10)
    nb_players = int(input("Entrez le nombre de joueurs : "))
    for i in range(nb_players):
        player_name = input(f"Nom du joueur {i + 1} : ")
        game.add_player(player_name)
    
    game.play()
