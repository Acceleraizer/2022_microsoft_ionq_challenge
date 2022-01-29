from os import abort
import typing
from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
from qiskit.tools.monitor import job_monitor
from azure.quantum.qiskit import AzureQuantumProvider
import numpy as np

circuit = QuantumCircuit(2, 2)
circuit.h(0)
circuit.x(0)
circuit.y(1)
circuit.p(np.pi/4, 0)
circuit.cx(0,1)
circuit.measure([0, 1], [0, 1])

print(circuit.draw())

provider = AzureQuantumProvider (
            resource_id = "/subscriptions/b1d7f7f8-743f-458e-b3a0-3e09734d716d/resourceGroups/aq-hackathons/providers/Microsoft.Quantum/Workspaces/aq-hackathon-01",
            location = "eastus"
        )

simulator_backend = provider.get_backend('ionq.simulator')
job = simulator_backend.run(circuit, shots=100)
result = job.result().get_counts()

print(result)

# The histogram returned by the results can be sparse, so here we add any of the missing bitstring labels.
# counts = {format(n, "03b"): 0 for n in range(8)}
# counts.update(result.get_counts(circuit))
# print(counts)