import quantum_battlegrounds as qb
import sys



def main():
    if not len(sys.argv) == 2:
        print('qpu?')
        exit()

    target_backend = 'ionq.simulator'
    if int(sys.argv[1]) == 1:
        target_backend = 'ionq.qpu'

    starting_pool = {'I':4, 'X':4, 'Y':4, 'Z':4, 'H':4, 'S':4, 'CX':4}

    arena = qb.Arena(2, 2, starting_pool, hero_pool=None, backend=target_backend)
    arena.run_game()


if __name__=='__main__':
    main()