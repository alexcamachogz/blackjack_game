# Blackjack Game

This is a simple text-based implementation of the Blackjack game. The game allows you to play against a computer-controlled dealer.

## How to Play
1. Run the script.
2. Follow the prompts in the console to play the game.
3. At the beginning of each round, you will be dealt two cards, and the dealer will be dealt one visible card and one hidden card.
4. You can choose to draw additional cards (hit) or stop drawing cards (stand).
5. The objective of the game is to get as close to 21 as possible without going over. Face cards are worth 10, and the Ace can be worth 1 or 11, depending on which value is more advantageous.
6. Once you decide to stand, the dealer will reveal their hidden card and draw additional cards until they have a score of 17 or higher.
7. The winner is determined by comparing the scores of the player and the dealer. The player with the score closest to 21 without going over wins.
8. After each round, you have the option to play again or exit the game.

## Example Output
```
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           

Welcome to the BlackJack Game

Your initial hand is 10 and 2
CPU initial hand is 6 and X

Do you want another card? Type 'y' or 'n': y
User hand: [10, 2, 9]
User score is 21

=== Final result ===
User hand: [10, 2, 9]
CPU hand: [6, 10, 10]
CPU score is 26 and user score is 21
User wins!

Do you want to play again? Type 'y' or 'n': n
Goodbye
```

## License
This project is licensed under the MIT License. Feel free to use and modify the code for your own purposes.

## Acknowledgements
This project was inspired by the Blackjack game and is based on the Python programming language.
