class Brain:
    def __init__(self, quiz):
        self.quiz = quiz
        self.scores = {}
        self.time_limit = 12

    def ask_question(self):
        total_quiz = len(self.quiz)
        num_players = int(input("How many players? "))
        self.calculate_scores(num_players, total_quiz)
        self.time_limit -= 1

    def calculate_scores(self, num_players, total_quiz):
        highest_score = 0
        highest_scorer = None
        for player in range(num_players):
            player_name = input(f"Enter your name (Player {player + 1}): ")
            player_score = 0
            time_left = self.time_limit
            for question_number in range(total_quiz):
                print(f"Question {question_number + 1}: {self.quiz[question_number].text}")
                player_answer = input(f"Player {player + 1}, enter your answer (True/False): ").lower()
                while player_answer not in ['true', 'false']:
                    player_answer = input("Invalid answer. Please enter your answer (True/False): ").lower()
                if player_answer == self.quiz[question_number].answer.lower():
                    player_score += 1
                    print("Correct!")
                else:
                    print("Incorrect!")
                if time_left == 0:
                    break
            self.scores[player_name] = player_score
            if player_score > highest_score:
                highest_score = player_score
                highest_scorer = player_name
        self.print_scores()
        print("Time is up!")
        print(f"The highest scorer is {highest_scorer} with a score of {highest_score}!")

    def print_scores(self, player_name=None):
        if player_name:
            print(f"{player_name} - {self.scores[player_name]}")
        else:
            for player, score in self.scores.items():
                print(f"{player} - {score}")
