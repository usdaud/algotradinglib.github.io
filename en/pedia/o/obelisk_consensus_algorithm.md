# Obelisk Consensus Algorithm

The Obelisk Consensus Algorithm is a unique approach to achieving consensus in [distributed ledger technology](../d/distributed_ledger_technology.md), specifically designed for the Skycoin ecosystem. Aimed at addressing limitations and issues found in other consensus mechanisms, such as Proof of Work (PoW) and Proof of Stake (PoS), Obelisk focuses on enhanced [security](../s/security.md), decentralization, and [efficiency](../e/efficiency.md).

### Overview

Obelisk is a novel form of consensus that implements a system of "web of [trust](../t/trust.md)" in place of traditional [mining](../m/mining.md) methods. Unlike PoW, which relies on computational power, and PoS, which leverages ownership stakes, Obelisk uses a network of nodes where each node trusts a set of other nodes. This framework helps in limiting control by any single entity and enhances the network's resistance to attacks.

### Key Components and Concepts

1. **Web of [Trust](../t/trust.md):**
   - In Obelisk, each node maintains a list of other nodes it trusts. This list is essentially a directed acyclic graph (DAG) whereby each node's [trust](../t/trust.md) is based on the connections it builds with others.
   - [Trust](../t/trust.md) relationships among nodes are public, which allows network participants to identify and avoid potential malicious nodes.

2. **Distributed Consensus:**
   - Nodes communicate to reach a consensus on the state of the ledger without the need for [mining](../m/mining.md). This means there are no substantial computational requirements, making the network both energy-efficient and fast.
   - Each node in the network votes on transactions and blocks, forming a method of agreement through trusted communication channels.

3. **[Security](../s/security.md):**
   - Obelisk addresses [security](../s/security.md) by decentralizing [trust](../t/trust.md). Each node's influence is proportional to its [trust](../t/trust.md) relationships, making it harder for a single entity to exert control over the network.
   - Forks and attacks are more complex to execute due to the interdependence of trusted nodes.

4. **[Efficiency](../e/efficiency.md):**
   - The algorithm is designed to be lightweight, requiring minimal computational resources. This directly translates into lower operating costs and higher [transaction](../t/transaction.md) [throughput](../t/throughput.md).
   - Without the need for energy-intensive [mining](../m/mining.md) or staking, the network maintains ecological sustainability and cost-effectiveness.

5. **Anti-Sybil Mechanisms:**
   - The web of [trust](../t/trust.md) inherently offers resistance to Sybil attacks, where an attacker might introduce a large number of fraudulent identities. Since nodes prioritize communication with trusted counterparts, adding fake nodes without establishing [trust](../t/trust.md) would be ineffective.

### Practical Implementation

In the Skycoin [blockchain](../b/blockchain_in_trading.md), Obelisk is operational and aims to surpass the limitations posed by traditional consensus methods. Skycoin nodes validate and propagate transactions and blocks using the principles outlined above.

### Benefits

1. **Decentralization:**
   - True decentralization is achieved through diverse and distributed [trust](../t/trust.md) networks, minimizing the [risk](../r/risk.md) of centralization seen in PoW and PoS systems.
   
2. **Environmental Impact:**
   - Energy consumption is drastically reduced, promoting a greener and more sustainable [blockchain](../b/blockchain_in_trading.md) network.
   
3. **[Security](../s/security.md) and Robustness:**
   - [Trust](../t/trust.md)-based consensus guards against many traditional attacks, providing a [robust](../r/robust.md) and resilient ledger.

4. **[Throughput](../t/throughput.md) and Speed:**
   - The consensus process allows for faster [transaction](../t/transaction.md) validation, enhancing the user experience with quicker confirmations.

### Challenges

1. **Network [Trust](../t/trust.md) Initialization:**
   - Establishing initial [trust](../t/trust.md) networks can be complex, requiring effective mechanisms for nodes to build [trust](../t/trust.md) tables without prior experiences.
   
2. **[Scalability](../s/scalability.md):**
   - While more efficient than PoW, the system's [scalability](../s/scalability.md) depends on maintaining a manageable level of [trust](../t/trust.md) relationships, which could become challenging with network growth.
   
3. **[Trust](../t/trust.md) Exploitation:**
   - Ensuring that [trust](../t/trust.md) relationships are not exploited for fraudulent purposes requires continuous monitoring and potential algorithmic adjustments.

### Conclusion

The Obelisk Consensus Algorithm offers an innovative pathway for achieving distributed consensus, particularly emphasizing the balance between decentralization, [security](../s/security.md), and [efficiency](../e/efficiency.md). By leveraging a web of [trust](../t/trust.md), it opens up avenues for sustainable, high-performance [blockchain](../b/blockchain_in_trading.md) applications.

For further details on the implementation and technical specifications of Obelisk, please visit the official Skycoin website: [Skycoin Documentation](https://www.skycoin.net/docs/).