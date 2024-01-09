# Clash of Clans

- To run the game : `python3 game.py`
- To view replays : `python3 replay.py`  and select the replay you want to watch according to mentioned date and time.
- For Victory : All buildings apart from walls get destroyed from the map in all three levels.
- For Defeat : If all troops and King die before destroying all buildings apart from walls.

## Controls :

### Hero :

- w : move up
- a : move left
- d : move right
- s : move down
- 1 : Special Attack
- space : Normal Attack

### Barbarian :

- z : spawn at point 1
- x : spawn at point 2
- c : spawn at point 3

### Dragon :

- v : spawn at point 1
- b : spawn at point 2
- n : spawn at point 3

### Archer :

- i : spawn at point 1
- o : spawn at point 2
- p : spawn at point 3

### Balloon :

- j : spawn at point 1
- k : spawn at point 2
- l : spawn at point 3

q : Quit Game

## Assumptions :

- Rage and Heal Spell can be applied multiple times.
- The limit for troops in each level is as follows :
    - Barbarians : 10
    - Archers : 7
    - Balloon : 5
    - Dragon : 3
- You have to choose the type of troop movement at start of the game.
- You have to choose the hero after each level.
<hr>

## Updates :

- Range of attack of archers and stealth archers has been set to `4` tiles

### Stealth Archer :

- t : spawn at point 1
- y : spawn at point 2
- u : spawn at point 3

- Stealth archer is a child class of archer
    - This implementation of stealth archer is used to show implementation concept of OOPS

### Healer :

- H : spawn at point 1

## Assumptions :

- The limits for the newly added troops are as follows:
    - Stealth Archer : 3
    - Healer : 1

- Checking of buildings within range of attack of stealth archer is done on the basis of `Euclidean` distance as it was the logic used in the archer class and the stealth archer class inherited the same function to check for nearby buildings
- Attacking and moving mechanism is same as archer

- The speed of healer has been set to `2` as it is the same speed as the speed of the balloon and it has been mentioned in the assignment pdf that specific details of the healer can be referred to from the specifications of the balloon
- The troops that are within the `7` tile radius are checked on the basis of `Euclidean` distance
- The AoE of the heal of the healer is `1` tile and the area is checked on the basis of `Manhattan` distance, which essentially creates a 3*3 tile AoE around the point of healing with the point of healing being in the center
- Healers cannot heal any healers but can heal other air and ground troops and heroes
- Healers first move to the nearest wounded troop and if there are none, then they move to the nearest troop

- Levels of the cannons, wizard towers and walls have been hardcoded in the `points.py` file, where the building objects are declared as dictionaries with `position` key containing the coordinates tuple and the `level` key containing the level of the building, which ranges from `1` to `5`

- Uniformity in the level of walls in a level has not been maintained, i.e. the walls in a level can have different levels
- The presence of troops within explosion radius is checked on the basis of `Manhattan` distance, which essentially creates a 5*5 tile AoE around the point of explosion with the wall being in the center
- All troops, both air and ground and even heroes are affected by the explosion of the wall