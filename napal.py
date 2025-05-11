import numpy as np
from qiskit import QuantumCircuit
import qiskit.quantum_info as qi
from math import sqrt

qc = QuantumCircuit(2)
qc.h(1)
qc.cx(1,0)

k = qc.draw(reverse_bits=True)
print(k)

QAB = qi.DensityMatrix(qc)
print("nuestra matriz densidad:\n",QAB)

QA = qi.partial_trace(QAB,[0])
print("parcial A\n", QA)
