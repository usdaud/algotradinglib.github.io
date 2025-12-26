# Uncle Block (Cryptocurrency)

In the context of [blockchain](../b/blockchain_in_trading.md) technology and cryptocurrencies, an uncle block refers to a block in a [blockchain](../b/blockchain_in_trading.md) that is not part of the longest or main chain but still [shares](../s/shares.md) some degree of relation to it. These blocks are referred to as "uncles" on the [Ethereum](../e/ethereum_.md) network, while on the [Bitcoin](../b/bitcoin.md) network, they are commonly called orphan blocks or stale blocks. Uncle blocks are an essential aspect of decentralized consensus mechanisms, influencing the network's [security](../s/security.md) and decentralization.

## Concept of Uncle Blocks

### Blockchain Basics

A [blockchain](../b/blockchain_in_trading.md) is essentially a distributed ledger where transactions are recorded in blocks. These blocks are cryptographically linked to form an immutable and transparent chain. New blocks are appended by miners, who solve complex mathematical problems to validate transactions and maintain the integrity of the [blockchain](../b/blockchain_in_trading.md).

### Mining and Forks

In a decentralized network, miners work simultaneously to add the next block to the [blockchain](../b/blockchain_in_trading.md). Sometimes, two miners may solve the mathematical puzzle almost at the same time, leading to the creation of two competing blocks. This situation creates a temporary fork in the [blockchain](../b/blockchain_in_trading.md).

### Resolving Forks

The [blockchain](../b/blockchain_in_trading.md) protocol eventually resolves these forks when subsequent blocks are added, causing one chain to become longer than the other. The network adheres to a rule that the longest chain (the one with the most cumulative work) is considered the valid chain. The shorter chain's competing blocks that do not make it into the longest chain become stale or orphaned.

## Uncle Blocks in Ethereum

[Ethereum](../e/ethereum_.md)'s [blockchain](../b/blockchain_in_trading.md) incorporates a unique mechanism to reward miners for blocks that do not end up in the longest chain, known as "uncle blocks".

### Definition and Function

An uncle block is a valid block rejected during the race to add blocks to the [blockchain](../b/blockchain_in_trading.md). Despite being valid, these blocks did not make it to the main chain due to timing differences. [Ethereum](../e/ethereum_.md) acknowledges the computational effort required to produce these blocks and includes them as uncles.

### Incentivizing Uncle Blocks

[Ethereum](../e/ethereum_.md) provides rewards for uncle blocks to enhance network [security](../s/security.md) and increase decentralization. Miners receive a smaller reward for uncle blocks compared to the main block reward. This incentivizes continued [mining](../m/mining.md) efforts even if a miner's block doesn't make it to the main chain.

### GHOST Protocol

The GHOST (Greedy Heaviest Observed Subtree) protocol, implemented in [Ethereum](../e/ethereum_.md), allows uncle blocks to be referenced in the main [blockchain](../b/blockchain_in_trading.md). By allowing references to uncle blocks, [Ethereum](../e/ethereum_.md) optimizes for faster block creation times without severely compromising [security](../s/security.md). This approach helps reduce the centralization of miners and improves overall [throughput](../t/throughput.md).

## Differences Between Uncle Blocks and Orphan Blocks

### Orphan Blocks in Bitcoin

On the [Bitcoin](../b/bitcoin.md) [blockchain](../b/blockchain_in_trading.md), blocks not included in the longest chain are termed orphan blocks or stale blocks. [Bitcoin](../b/bitcoin.md) does not [offer](../o/offer.md) rewards for these blocks, and they do not contribute to the [blockchain](../b/blockchain_in_trading.md)'s metrics like [security](../s/security.md) or chain-length.

### Rewards Mechanism

[Ethereum](../e/ethereum_.md)'s reward mechanism for uncle blocks is a significant [divergence](../d/divergence.md) from [Bitcoin](../b/bitcoin.md). In [Bitcoin](../b/bitcoin.md)'s network, only blocks in the validated [blockchain](../b/blockchain_in_trading.md) sequence earn rewards. [Ethereum](../e/ethereum_.md)'s incentives for uncle blocks aim to create a more inclusive and secure [mining](../m/mining.md) environment.

## Importance and Implications

### Network Security

Uncle blocks contribute to the consensus mechanism's [security](../s/security.md) by rewarding miners for their effort, reducing the likelihood of centralization, and encouraging continuous participation.

### Reduced Centralization

By compensating [mining](../m/mining.md) efforts that result in uncle blocks, [Ethereum](../e/ethereum_.md) deters centralization. It means smaller miners can still earn rewards, even if they can't consistently win the race to add the next main block.

### Improved Throughput

The GHOST protocol allows [Ethereum](../e/ethereum_.md) to have shorter block times, thus increasing [transaction](../t/transaction.md) [throughput](../t/throughput.md). Uncle blocks ensure that even with faster block times, network [security](../s/security.md) remains [robust](../r/robust.md).

## Real-world Example: Ethereum

[Ethereum](../e/ethereum_.md) is the most notable [blockchain](../b/blockchain_in_trading.md) platform utilizing uncle blocks. Miners who discover uncle blocks receive approximately 1.75 ETH, as opposed to the 2 ETH for a full valid block. This incentivizes miners and contributes to the network's [security](../s/security.md) and decentralization. More details about [Ethereum](../e/ethereum_.md)

## Conclusion

Uncle blocks in cryptocurrency networks like [Ethereum](../e/ethereum_.md) represent an innovative approach to maintaining decentralization, [security](../s/security.md), and fairness in [blockchain](../b/blockchain_in_trading.md) consensus mechanisms. By acknowledging and rewarding efforts that partially contribute to the network's growth, [Ethereum](../e/ethereum_.md) ensures broader participation and [robust](../r/robust.md) performance. Understanding uncle blocks provides insight into the nuanced and sophisticated mechanisms [underlying](../u/underlying.md) decentralized networks like [Ethereum](../e/ethereum_.md), setting them apart from traditional financial systems and other cryptocurrencies like [Bitcoin](../b/bitcoin.md).