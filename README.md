# # Conway's Game of Life

This repository contains an implementation of **Conway's Game of Life** in Python. The Game of Life is a cellular automaton devised by the mathematician John Conway. This simulation showcases how simple rules can lead to complex and fascinating patterns.

## Features

- Random or custom initialization of the grid.
- Generation limit (maximum of 100 generations).
- Grid size limit (maximum of 20x20).
- Interactive console interface for configuration.

## How It Works

The Game of Life is played on a grid of square cells. Each cell can be either "alive" (1) or "dead" (0). The state of the cells evolves in discrete steps (generations) according to these rules:

1. Any live cell with fewer than two live neighbors dies (underpopulation).
2. Any live cell with two or three live neighbors survives.
3. Any live cell with more than three live neighbors dies (overpopulation).
4. Any dead cell with exactly three live neighbors becomes a live cell (reproduction).

## Getting Started

### Prerequisites
- Python 3.x installed on your system.

### Installation
1. Clone the repository:
   ```bash
   git clone <URL_OF_YOUR_FORK>
   cd game_of_life
