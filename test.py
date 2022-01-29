import quantum_battlegrounds as qb



def main():
    starting_pool = {'X':4, 'Y':4, 'Z':4, 'H':4, 'CX':4}

    arena = qb.Arena(2, 2, starting_pool, hero_pool=None)
    arena.pr_state()
    arena.buy_minion(0, 'X')
    arena.buy_minion(0, 'H')
    arena.buy_minion(0, 'CX')
    arena.pr_state()

    circuit_data = [('X', [0]), ('H', [1]), ('CX',[0, 1])]
    arena.build_circuit(0, circuit_data)

    print(arena.players[0].circuit)


if __name__=='__main__':
    main()