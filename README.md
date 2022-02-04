# Rock Paper Scissors Game



## Setup

Create a virtual environment:

```sh
conda create -n rps-env python=3.8
```

Activate the virtual environment:

```sh
conda activate rps-env
```

Install package dependencies (mainly for testing):

```sh
pip install -r requirements.txt
```

## Usage

Run the rock paper scissors game and add your player name in place of "John Doe":

```sh
PLAYER_NAME="John Doe" python game.py
```

## Instructions

The game works just as any traditional rock-paper-scissors game. Once you make your selection, the rules are as follows:
1. Rock beats Scissors
2. Paper beats Rock
3. Scissors beats Paper
4. Rock vs Rock, Paper vs Paper, and Scissors vs Scissors each results in a "tie"

Good luck!
