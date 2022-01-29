from os import abort
from turtle import back
import typing
from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
from qiskit.tools.monitor import job_monitor
from azure.quantum.qiskit import AzureQuantumProvider
from scipy.fft import set_backend


# provider = AzureQuantumProvider (
#     resource_id = "/subscriptions/b1d7f7f8-743f-458e-b3a0-3e09734d716d/resourceGroups/aq-hackathons/providers/Microsoft.Quantum/Workspaces/aq-hackathon-01",
#     location = "eastus"
# )
# print([backend.name() for backend in provider.backends()])





# game logic
# 1. pool of gates
# 2. build phase
# 3. 

SINGLE_QUBIT_GATES = ['X', 'Y', 'Z', 'H']
TWO_QUBIT_GATES = ['CX']

def applySQG(circuit, gatename, targets):
    if gatename == 'X':
        circuit.x(targets[0])
    elif gatename == 'Y':
        circuit.y(targets[0])
    elif gatename == 'Z':
        circuit.z(targets[0])
    elif gatename == 'H':
        circuit.h(targets[0])
    else:
        print("gate translation not implemented")
        return None

def applyTQG(circuit, gatename, targets):
    if gatename == 'CX':
        circuit.cx(targets[0], targets[1])
    else:
        print("gate translation not implemented")
        return None


class Player:
    id = None
    minions = {}
    circuit:QuantumCircuit = None
    last_circuit:QuantumCircuit = None

    def __init__(self, id, gate_types):
        self.id = id
        self.minions = gate_types.copy()

    def __str__(self):
        return f"Player {self.id}, with minions {self.minions}"




class Arena:
    players = []
    pool = {}
    hero_pool = {}
    round = 0
    lanes = 0

    target_backend = 'ionq-simulator'
    provider = None


    def __init__(self, playercount, lanes, starting_pool, hero_pool, backend=None):
        starting_gates = starting_pool.copy()
        for gate in starting_gates.keys():
            starting_gates[gate] = 0
        self.players = [Player(i+1, starting_gates.copy()) for i in range(playercount)]
        self.pool = starting_pool
        self.lanes = lanes
        if not backend==None:
            self.set_backend(backend)

        self.provider = AzureQuantumProvider (
            resource_id = "/subscriptions/b1d7f7f8-743f-458e-b3a0-3e09734d716d/resourceGroups/aq-hackathons/providers/Microsoft.Quantum/Workspaces/aq-hackathon-01",
            location = "eastus"
        )
        print([backend.name() for backend in self.provider.backends()])


    def set_backend(self, backend):
        self.target_backend = backend
    
    """
    Hero pick phase
    """


    """
    Buy/sell phase
    """
    # pid is the id of the player
    # minion is the string name of the gate
    def buy_minion(self, pid, minion):
        if self.pool[minion] <= 0:
            return False

        self.players[pid].minions[minion] += 1
        self.pool[minion] -= 1
        return True

    def sell_minion(self, pid, minion):
        self.players[pid].minions[minion] -= 1
        self.pool[minion] += 1
        return True
    
    """
    Build phase
    """

    def use_last_circuit(self, pid):
        self.players[pid].circuit = self.players[pid].last_circuit


    # requirement: circuit_data is an array containing pairs (gate, [list of qubits])
    def build_circuit(self, pid, circuit_data):
        circuit = QuantumCircuit(self.lanes, self.lanes)
        for gate_spec in circuit_data:
            if gate_spec[0] in SINGLE_QUBIT_GATES:
                applySQG(circuit, gate_spec[0], gate_spec[1])
            else:
                applyTQG(circuit, gate_spec[0], gate_spec[1])
        self.players[pid].circuit = circuit
    
    """
    Battle phase
    """
    def sum_score(bitstring):
        return sum([b=='1' for b in bitstring])


    def battle(self, pid1, pid2):
        atob = self.players[pid1].circuit.combine(self.players[pid2].circuit)
        btoa = self.players[pid2].circuit.combine(self.players[pid1].circuit)
        atob.measure(list(range(self.lanes)), list(range(self.lanes)))
        btoa.measure(list(range(self.lanes)), list(range(self.lanes)))
        
        simulator_backend = self.provider.get_backend(self.target_backend)
        job1 = simulator_backend.run(atob, shots=1)
        job2 = simulator_backend.run(btoa, shots=1)




    """
    Printing functions
    """

    def pr_playerstate(self):
        print("\n".join([str(player) for player in self.players]))

    def pr_boardstate(self):
        print(f"Minions in the pool: {self.pool}")


    def pr_state(self):
        print(f"State at round {self.round}:")
        self.pr_playerstate()
        self.pr_boardstate()
        print("=======")









# Create a Quantum Circuit acting on the q register
# circuit = QuantumCircuit(3, 3)
# circuit.name = "Qiskit Sample - 3-qubit GHZ circuit"
# circuit.h(0)
# circuit.cx(0, 1)
# circuit.cx(1, 2)
# circuit.measure([0,1,2], [0, 1, 2])

# Print out the circuit
# print(circuit.draw())

# simulator_backend = provider.get_backend("ionq.simulator")
# job = simulator_backend.run(circuit, shots=100)
# job_id = job.id()
# print("Job id", job_id)

# result = job.result()

# The histogram returned by the results can be sparse, so here we add any of the missing bitstring labels.
# counts = {format(n, "03b"): 0 for n in range(8)}
# counts.update(result.get_counts(circuit))
# print(counts)

# print('success')