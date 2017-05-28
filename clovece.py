from random import randint
import sys

gamestate=((0, 1, 2, 3), (10, 11, 12, 13), (20, 21, 22, 23), (30, 31, 32, 33))

def print_pl(states):
    print('Player 1 pieces are on fields: ', states[0])
    print('Player 2 pieces are on fields: ', states[1])
    print('Player 3 pieces are on fields: ', states[2])
    print('Player 4 pieces are on fields: ', states[3])


def update_states(old, dice, player, piece):
    old = old[:player] + (old[player][:piece] + ((old[player][piece] + dice) % 40,) + old[player][piece+1:],) + old[player+1:]
    return old

player = -1
while 1:
    print('press -1 to quit')
    print_pl(gamestate)
    player += 1
    dice = randint(1, 6)
    player %= 4
    print('Player: ', player + 1, 'is on turn.')
    print('Dice: ', dice)
    print('What piece to move? (1-4):')
    cmd = int(input()) - 1
    if cmd == -2:
        sys.exit()
    gamestate = update_states(gamestate, dice, int(player), cmd)