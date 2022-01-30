import quantum_battlegrounds as qb
import sys



def main():
    if not len(sys.argv) == 2:
        print('qpu?')
        exit()

    target_backend = 'ionq.simulator'
    if int(sys.argv[1]) == 1:
        target_backend = 'ionq.qpu'

    starting_pool = {'X':4, 'Y':4, 'Z':4, 'H':4, 'CX':4}

    arena = qb.Arena(2, 2, starting_pool, hero_pool=None, backend=target_backend)
    arena.pr_state()
    arena.buy_minion(0, 'X')
    arena.buy_minion(0, 'H')
    arena.buy_minion(0, 'CX')
    arena.pr_state()

    circuit_data1 = [('X', [0]), ('X', [1]), ('CX',[0, 1])]
    arena.build_circuit(0, circuit_data1)
    circuit_data2 = [('H', [1]), ('CX',[0, 1])]
    arena.build_circuit(1, circuit_data2)

    print(arena.players[0].circuit)
    print(arena.players[1].circuit)

    # r1, r2 = arena.battle(0, 1)
    # print (r1, r2)
    r1, r2, s1, s2 = arena.battle_resolve(0, 1)
    print(r1, r2, s1, s2)


if __name__=='__main__':
    main()