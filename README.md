# Welcome to IonQ + Microsoft Joint Challenge @ MIT iQuHACK 2022!

<p align="left">
  <a href="https://azure.microsoft.com/en-us/solutions/quantum-computing/" target="_blank"><img src="https://user-images.githubusercontent.com/10100490/151488491-609828a4-cd1f-4076-b5b2-a8d9fc2d0fa4.png" width="30%"/> </a>
  <a href="https://ionq.com/" target="_blank"><img src="https://user-images.githubusercontent.com/10100490/151488159-da95eb05-9277-4abe-b1ba-b49871d563ed.svg" width="20%" style="padding: 1%;padding-left: 5%"/></a>
  <a href="https://iquhack.mit.edu/" target="_blank"><img src="https://user-images.githubusercontent.com/10100490/151647370-d161d5b5-119c-4db9-898e-cfb1745a8310.png" width="8%" style="padding-left: 5%"/> </a>
  
</p>

Welcome to Quantum Auto-Chess. This is the simplified version of the auto-chess game that we are aiming to develop.

Auto-Chess, one of the most popular game types on in the internet as of now, can be described as a 8-player chess game featuring a shared pool of chess pieces. Every round, all players go through the “prepare phase” and the “battle phase”. In “prepare phase”, you buy, sell or upgrade your chess pieces to form a stronger team. In the “battle phase”, your chess pieces match another player, and through an automated fight one player will deal damage to another. [Here](https://playhearthstone.com/en-us/news/23156373) are more information on the general rules.

In quantum auto-chess, we employ quantum algorithms for automated fights. Every player will be equipped with a quantum circuit of two qubits, and the chess pieces they can buy are logic gates that can be applied to the qubits. The end goal of the player is to flip their initial state (from 0 to 1). In addition to the capability of team of gates, certain combo of gates grants extra special power in the form of multi-quit gates. (which will be available in a more advanced version)

# Gameplay in Quantum Logic

The impedance you face is your opponent. In quantum auto-chess, every round the player will face two fights. First, A player’s circuit output will become B player’s input. Then we measure B circuit’s outfits, which decides game result ( how many 1 digit were measured). This is the AB fight. Then the BA fight happens, and whoever won more 1 digit in the eventual output wins the round and deals damage to the other player. This process is highly unpredictable, but generally a circuit that’s designed to turn the 0 state into 1 will also turn the state 1 into 0. Hence, your opponent will block your circuit from achieving 1, but process is way more complex than that, which is the fun of quantum mechanics; you never know for certain!

# Future and Plans

Ideally, the game would be equipped with multi-player support, a health and damage system, a currency system, animations and more and more. But in this very simple Unity UI, we present the core quantum algorithm: Two players get involved in an interactive fight where the probabilistic distribution of their quantum circuit output determines the game result. In the game, each player will be able to select from the shop what they wish to buy and place them in order; then they battle, and the damage one has dealt to another is revealed.

