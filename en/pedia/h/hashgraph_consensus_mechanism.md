# Hashgraph Consensus Mechanism

## Introduction

The Hashgraph consensus mechanism is a novel approach to achieving consensus in distributed networks. Unlike traditional [blockchain](../b/blockchain_in_trading.md) technology, Hashgraph does not follow a linear chain of blocks. Instead, it uses a graph structure where nodes communicate their information through "gossip about gossip" and virtual voting. This makes the Hashgraph consensus mechanism highly efficient, with benefits such as high [throughput](../t/throughput.md), low latency, and strong [security](../s/security.md) guarantees. Hashgraph technology has been primarily developed by Hedera Hashgraph, founded by Dr. Leemon Baird and Mance Harmon.

## Gossip Protocol

Gossip protocols are communication methods used in distributed systems where information is spread in a manner similar to how rumors spread in social networks. Each node randomly selects other nodes to share information with, and this process continues until all nodes are aware of the new information. In the context of Hashgraph, the gossip protocol is used to share information about transactions and the network's state.

### Gossip About Gossip

"Gossip about gossip" is a unique aspect of Hashgraph that involves nodes sharing not only the information about transactions but also the history of how they learned the information. This historical context is captured in a structure called an "event", which contains a payload of the [transaction](../t/transaction.md) data, a timestamp, and records of which nodes gossiped the information to each other.

By sharing the history of communication, Hashgraph allows nodes to build a complete picture of the communication pathways, enabling them to reach consensus on the [order](../o/order.md) of transactions without the need for intensive computational work.

## Virtual Voting

Virtual voting is a core element of the Hashgraph consensus mechanism. After the gossip protocol has disseminated events throughout the network, nodes can locally determine the [order](../o/order.md) of transactions based on the shared communication history. Virtual voting works as follows:

1. **Round Creation**: Events are grouped into rounds based on when they are received. Each node keeps track of the rounds.
2. **Witnesses**: Within each round, nodes nominate certain events as "witnesses". Witnesses are events that a specific node is confident have been received by the majority of the network.
3. **Fame Voting**: Nodes "vote" on the fame of witnesses. Fame indicates whether a witness should be considered as representative of the consensus. The voting occurs virtually, based on the information already known to the nodes, without actual message exchanges.
4. **Finalization**: Once a sufficient number of rounds have passed and witnesses' fame has been determined, the consensus [order](../o/order.md) of events is finalized.

This process ensures that all honest nodes can independently and efficiently reach the same consensus without the need for extensive communication. The virtual voting algorithm is Byzantine fault tolerant, meaning it can tolerate malicious actors within the network.

## Advantages of Hashgraph

### High Throughput

Unlike traditional blockchains, which can become bottlenecked by the need to sequentially add blocks, Hashgraph allows for [multiple](../m/multiple.md) events to be processed in parallel. This multi-lane approach enables Hashgraph to achieve higher [transaction](../t/transaction.md) [throughput](../t/throughput.md). The platform can [handle](../h/handle.md) hundreds of thousands of transactions per second, making it suitable for high-[volume](../v/volume.md) applications.

### Low Latency

Hashgraph achieves consensus quickly due to its efficient communication and consensus mechanisms. The gossip protocol rapidly disseminates information, and virtual voting finalizes consensus without lengthy delays. This results in low latency, meaning transactions are confirmed quickly, often within seconds.

### Security

Hashgraph provides strong [security](../s/security.md) guarantees. It is asynchronous Byzantine fault tolerant (aBFT), meaning it can achieve consensus despite the presence of malicious actors and without relying on precise timing assumptions. This makes Hashgraph [robust](../r/robust.md) against various attack vectors, including network delays and targeted attacks on specific nodes.

### Fairness

The consensus mechanism of Hashgraph aims to be fair in terms of [transaction](../t/transaction.md) ordering. The use of virtual voting and witness selection ensures that no single node or small group of nodes can unduly influence the [order](../o/order.md) of transactions. This stands in contrast to some [blockchain](../b/blockchain_in_trading.md) systems where miners or validators can have disproportionate control.

## Applications of Hashgraph

### Cryptocurrency

Hashgraph technology serves as the [underlying](../u/underlying.md) protocol for the Hedera Hashgraph platform, which includes the HBAR cryptocurrency. HBAR transactions benefit from Hashgraph's high [throughput](../t/throughput.md), low latency, and [security](../s/security.md), making it a viable [digital currency](../d/digital_currency.md) for everyday transactions and enterprise uses.

### Decentralized Applications (DApps)

The [efficiency](../e/efficiency.md) and robustness of Hashgraph make it an ideal platform for decentralized applications. DApps can [leverage](../l/leverage.md) the high [transaction](../t/transaction.md) [throughput](../t/throughput.md) and quick finality to provide smooth user experiences. Sectors such as [finance](../f/finance.md), gaming, and [supply chain](../s/supply_chain.md) management stand to benefit from these capabilities.

### Enterprise Solutions

Hashgraph's strong [security](../s/security.md) and [efficiency](../e/efficiency.md) also make it suitable for enterprise solutions. Companies can deploy private or permissioned Hashgraph networks to manage internal processes, data sharing, and contractual agreements. The consensus mechanism ensures that the data integrity and confidentiality are maintained.

## Hedera Governing Council

The Hedera Hashgraph platform is governed by the Hedera Governing Council, a diverse group of leading organizations from various industries. These council members are responsible for overseeing the network's development, ensuring its decentralization, and guiding decisions about platform policies. Some notable members include Google, IBM, Boeing, and Deutsche Telekom.

The council ensures that the platform remains [open](../o/open.md) and standards-compliant, fostering [trust](../t/trust.md) among users and developers. The involvement of reputable organizations provides additional credibility to the Hedera Hashgraph network.

For more information about the Hedera Governing Council, visit [Hedera Governing Council](https://hedera.com/council).

## Conclusion

The Hashgraph consensus mechanism represents a significant advancement in [distributed ledger technology](../d/distributed_ledger_technology.md). By utilizing gossip protocols, gossip about gossip, and virtual voting, Hashgraph achieves high [throughput](../t/throughput.md), low latency, and [robust](../r/robust.md) [security](../s/security.md). Its applications [range](../r/range.md) from cryptocurrency and decentralized applications to enterprise solutions, making it a versatile and powerful technology for the digital age. With the backing of the Hedera Governing Council, Hashgraph is poised to become a leading platform in the decentralized ecosystem.