import numpy as np
import points as pt
from characters import barbarians, dragons, balloons, archers, stealth_archers, healers

king_obj = None

def update_king_obj(king):
    global king_obj
    king_obj = king

class Building:
    def destroy(self):
        self.destroyed = True
        if self.type == 'hut':
            self.V.remove_hut(self)
        elif self.type == 'cannon':
            self.V.remove_cannon(self)
        elif self.type == 'wizardtower':
            self.V.remove_wizard_tower(self)
        elif self.type == 'townhall':
            self.V.remove_town_hall(self)


class Hut(Building):
    def __init__(self, position, V):
        self.position = position
        self.dimensions = (2, 2)
        self.V = V
        self.destroyed = False
        self.health = 40
        self.max_health = 40
        self.type = 'hut'


class Cannon(Building):
    def __init__(self, position, level, V):
        self.position = position
        self.level = level
        self.dimensions = (2, 2)
        self.V = V
        self.destroyed = False
        self.health = 60 + 30 * level
        self.max_health = 60 + 30 * level
        self.type = 'cannon'
        self.attack = 4 + level
        self.attack_radius = 5 + float(level) / 2
        self.isShooting = False

    def scan_for_targets(self, King):
        self.isShooting = False

        troops = barbarians + archers + stealth_archers
        for troop in troops:
            if hasattr(troop, 'isInvisible') and troop.isInvisible == True:
                continue

            if (troop.position[0] - self.position[0])**2 + (troop.position[1] - self.position[1])**2 <= self.attack_radius**2:
                self.isShooting = True
                self.attack_target(troop)
                return

        # for barb in barbarians:
        #     if (barb.position[0] - self.position[0])**2 + (barb.position[1] - self.position[1])**2 <= self.attack_radius**2:
        #         self.isShooting = True
        #         self.attack_target(barb)
        #         return
        # for dragon in dragons:
        #     if (dragon.position[0] - self.position[0])**2 + (dragon.position[1] - self.position[1])**2 <= self.attack_radius**2:
        #         self.isShooting = True
        #         self.attack_target(dragon)
        #         return

        if King.alive == False:
            return

        if(King.position[0] - self.position[0])**2 + (King.position[1] - self.position[1])**2 <= self.attack_radius**2:
            self.isShooting = True
            self.attack_target(King)

    def attack_target(self, target):
        if(self.destroyed == True):
            return
        if hasattr(target, 'isInvisible') and target.isInvisible == True:
            return
        target.deal_damage(self.attack)


class Wall(Building):
    def __init__(self, position, level, V):
        self.position = position
        self.dimensions = (1, 1)
        self.V = V
        self.destroyed = False
        self.level = level
        self.health = 100 + 40 * level
        self.max_health = 100 + 40 * level
        self.destruction_radius = 2
        self.explosion_damage = 200
        self.type = 'wall'

    def scan_for_targets(self):
        troops = barbarians + archers + stealth_archers

        for troop in troops:
            if abs(troop.position[0] - self.position[0]) <= self.destruction_radius and abs(troop.position[1] - self.position[1]) <= self.destruction_radius:
                self.attack_target(troop)

        global king_obj
        
        if king_obj.alive == False:
            return
        
        if abs(king_obj.position[0] - self.position[0]) <= self.destruction_radius and abs(king_obj.position[1] - self.position[1]) <= self.destruction_radius:
            self.attack_target(king_obj)
    
    def attack_target(self, target):
        if self.destroyed == True:
            return
        target.deal_damage(self.explosion_damage)

    def destroy(self):
        if self.level >= 3:
            self.scan_for_targets()

        self.destroyed = True
        self.V.remove_wall(self)


class TownHall(Building):
    def __init__(self, position, V):
        self.position = position
        self.dimensions = (4, 3)
        self.V = V
        self.destroyed = False
        self.health = 100
        self.max_health = 100
        self.type = 'townhall'


class WizardTower(Building):
    def __init__(self, position, level, V):
        self.position = position
        self.level = level
        self.dimensions = (1, 1)
        self.V = V
        self.destroyed = False
        self.health = 60 + 30 * level
        self.max_health = 60 + 30 * level
        self.type = 'wizardtower'
        self.attack = 4 + level
        self.attack_radius = 5 + float(level) / 2
        self.isShooting = False

    def scan_for_targets(self, King):
        self.isShooting = False
        troops = barbarians+ archers + dragons + balloons + stealth_archers + healers
        for troop in troops:
            if hasattr(troop, 'isInvisible') and troop.isInvisible == True:
                continue

            if (troop.position[0] - self.position[0])**2 + (troop.position[1] - self.position[1])**2 <= self.attack_radius**2:
                self.isShooting = True
                self.attack_target(troop,0)
                return

        if King.alive == False:
            return

        if(King.position[0] - self.position[0])**2 + (King.position[1] - self.position[1])**2 <= self.attack_radius**2:
            self.isShooting = True
            self.attack_target(King,1)

    def attack_target(self, target, isKing):
        if(self.destroyed == True):
            return

        if isKing == 1:
            target.deal_damage(self.attack)
        i = target.position[0] - 1
        j = target.position[1] - 1
        troops = barbarians+ archers + dragons + balloons + stealth_archers + healers
        for row in range(i, i+3):
            for col in range(j, j+3):
                if(row < 0 or col < 0):
                    continue
                for troop in troops:
                    if(troop.position[0] == row and troop.position[1] == col):
                        troop.deal_damage(self.attack)


def shoot_cannons(King, V):
    for cannon in V.cannon_objs:
        V.cannon_objs[cannon].scan_for_targets(King)


def shoot_wizard_towers(King, V):
    for tower in V.wizard_tower_objs:
        V.wizard_tower_objs[tower].scan_for_targets(King)
