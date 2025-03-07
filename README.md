# Chrome Dinosaur with NEAT AI

This project is a Chrome Dinosaur clone built with Python and Pygame, featuring both a player-controlled mode and an AI mode powered by the NEAT (NeuroEvolution of Augmenting Topologies) algorithm.

## Features

- **Player Mode:** Control the Dino manually using the keyboard up and down.
- **AI Mode:** Train an AI to play Chrome Dinosaur using NEAT.

## Installation

1. Clone the repository:

```sh
git clone https://github.com/RezaTaheri01/chrome-dinosaur-ai.git
```
```
cd chrome-dinosaur-ai
```

2. Install the required packages:

```sh
pip install pygame neat-python
```

3. Set up the project structure:

```
flappy-bird-neat/
├── Assets/
│   ├── Bird
│   ├── Cactus
│   ├── Dino
│   └── Other
├── src/
│   ├── cloud.py
│   ├── player.py
│   ├── constants.py
│   └── obstacles.py
├── config-feedforward.txt
└── main.py
```

## How to Run

- **Player Mode:**

In `src/constants.py`, set `PLAYER_MODE` to `True`:

```python
PLAYER_MODE = True
```

Then run the game:

```sh
python main.py
```

- **AI Mode:**

Set `PLAYER_MODE` to `False`:

```python
PLAYER_MODE = False
```

Run the NEAT training:

```sh
python main.py
```

## Controls

- **UP and Down:** Make the Dino Jump or Duck

## NEAT Configuration

The NEAT algorithm's settings are in the `config-feedforward.txt` file. You can tweak parameters like population size, mutation rates, and more to optimize training.

## Saving the Best Model

When the AI reaches a specific score(defined in src/constants.py), the best-performing neural network is saved as `best.pickle`.

## Acknowledgments

- Pygame for game development
- NEAT-Python for neural evolution

## Source Code Link:
- [MaxRohowsky](https://github.com/MaxRohowsky/chrome-dinosaur)

---

Enjoy playing (or watching) Dino! 🦖

