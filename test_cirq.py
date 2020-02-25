import cirq

##Pick a qubit
qubit = cirq.GridQubit(0,0)

##Create  a circuit
circuit = cirq. Circuit.from_ops([
    cirq.X(qubit), ##NOT
    cirq.measure(qubit,key='m')

]  )

##Display circuit
print("Circuit:")
print(circuit)

##Get a simulator to execute the circuit
simulator = cirq.Simulator()

#Simulate the circuit several times
result = simulator.run(circuit, repetitions=10)

##print results
print("Results")
print(result)
