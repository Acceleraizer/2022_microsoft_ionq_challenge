import quantum_battlegrounds as qb
import UnityEngine


starting_pool = {'I':4, 'X':4, 'Y':4, 'Z':4, 'H':4, 'S':4, 'CX':4}
arena = qb.Arena(2, 2, starting_pool, hero_pool=None)

# IMPORTANT! RETRIEVE CIRCUIT DESCRIPTIONS FROM C#
circuit_data1 = UnityEngine.GameObject.Find("ScriptHolder").GetComponent("ButtonBehaviour").circuit_data1
circuit_data2 = UnityEngine.GameObject.Find("ScriptHolder").GetComponent("ButtonBehaviour").circuit_data2

arena.build_circuit(0, circuit_data1)
arena.build_circuit(1, circuit_data2)
r1, r2, s1, s2 = arena.battle(0, 1)

if s1 > s2:
    winner = 0
elif s1 < s2:
    winner = 1
else:
    winner = -1

# WRITE WINNER TO C#
UnityEngine.GameObject.Find("ScriptHolder").GetComponent("ButtonBehaviour").winner = winner

# --end--



