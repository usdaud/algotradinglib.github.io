# Uniswap (V3)

Uniswap, a decentralized [exchange](../e/exchange.md) (DEX) protocol on the [Ethereum](../e/ethereum_.md) [blockchain](../b/blockchain_in_trading.md), allows users to [swap](../s/swap.md) various cryptocurrency tokens directly from their wallets. The third iteration of the protocol, Uniswap V3, introduces several notable advancements in terms of [liquidity](../l/liquidity.md) provisioning and [fee](../f/fee.md) structures, thereby enhancing [capital](../c/capital.md) [efficiency](../e/efficiency.md) and user experience. Uniswap V3 is built to maximize the flexibility and [efficiency](../e/efficiency.md) for its users, setting new standards in the decentralized [finance](../f/finance.md) (DeFi) space.

## Core Features

### Concentrated Liquidity
In traditional automated [market maker](../m/market_maker.md) (AMM) models, [liquidity](../l/liquidity.md) is evenly distributed along the price curve between 0 and infinity. Uniswap V3 introduces a concept called concentrated [liquidity](../l/liquidity.md), which allows [liquidity](../l/liquidity.md) providers (LPs) to allocate [liquidity](../l/liquidity.md) within custom price ranges. This means that LPs can [offer](../o/offer.md) [liquidity](../l/liquidity.md) only within ranges where they believe most of the trading [will](../w/will.md) happen, significantly improving [capital](../c/capital.md) [efficiency](../e/efficiency.md). By doing this, the same amount of [capital](../c/capital.md) can provide up to 4000x the [liquidity](../l/liquidity.md) compared to Uniswap V2.

### Multiple Fee Tiers
Uniswap V3 offers [multiple](../m/multiple.md) [fee](../f/fee.md) tiers to accommodate different levels of [risk](../r/risk.md) associated with providing [liquidity](../l/liquidity.md) to diverse token pairs. LPs can choose from the following [fee](../f/fee.md) tiers:

- 0.05%
- 0.30%
- 1.00%

These tiers are meant to cater to various token pairs, whether they are stablecoins with minimal [volatility](../v/volatility.md) or highly volatile tokens, thus [offering](../o/offering.md) more flexibility.

### Non-Fungible Positions
In contrast to Uniswap V2, where LP tokens are fungible, Uniswap V3 positions are represented by non-fungible tokens (NFTs) due to their unique characteristics, such as custom price ranges and [fee](../f/fee.md) structures. This facilitates unique positions and allows LPs to provide customized [liquidity](../l/liquidity.md) provisioning strategies.

### Active Liquidity Management
Uniswap V3 introduces features that enable more [active management](../a/active_management.md) of [liquidity](../l/liquidity.md). [Liquidity](../l/liquidity.md) providers can concentrate their [liquidity](../l/liquidity.md) closer to the current [market price](../m/market_price.md) and adjust their positions more frequently, which increases their potential returns compared to the passive [provision](../p/provision.md) model in Uniswap V2.

## Technical Specifications

### Smart Contract Design
Uniswap V3 employs a modular architecture with core and periphery contracts. The core contracts [handle](../h/handle.md) the critical functions such as swaps and [liquidity provision](../l/liquidity_provision.md), while the periphery contracts [handle](../h/handle.md) additional utilities like [liquidity](../l/liquidity.md) migration and router functions.

### Oracles
To improve the reliability of price oracles, Uniswap V3 introduces time-[weighted average](../w/weighted_average.md) price (TWAP) oracles. These oracles compute the average price over a configurable period, providing more resistant and reliable data points against manipulation and large price swings.

### License
Uniswap V3 codebase was initially released under [Business](../b/business.md) Source License (BSL) 1.1. This restricts commercial use of the V3 codebase for up to two years. Post this period, the code is intended to be released under the GPL-3.0 [open](../o/open.md)-source license.

## Advanced Strategies

### Range Orders
[Range](../r/range.md) orders in Uniswap V3 allow LPs to [deposit](../d/deposit.md) [liquidity](../l/liquidity.md) within a specific price [range](../r/range.md). When the [market price](../m/market_price.md) enters this [range](../r/range.md), it effectively executes a [limit order](../l/limit_order.md) until either the [range](../r/range.md) is depleted, or the price exits the [range](../r/range.md).

### Arbitrage Opportunities
Due to the [multiple](../m/multiple.md) [fee](../f/fee.md) tiers and concentrated [liquidity](../l/liquidity.md), opportunities for [arbitrage](../a/arbitrage.md) between different pools and markets are more prevalent. Advanced traders and bots can exploit these [arbitrage opportunities](../a/arbitrage_opportunities.md) to maintain efficient markets and [profit](../p/profit.md) from price discrepancies.

### Impermanent Loss Mitigation
Concentrated [liquidity](../l/liquidity.md) and the ability to set custom price ranges give LPs tools to counteract impermanent loss—a common [issue](../i/issue.md) in AMMs where prices of assets diverge after being deposited into a pool. By actively managing their positions, LPs can minimize their exposure to high [volatility](../v/volatility.md) and optimize returns.

## Governance and Tokenomics

### UNI Token
Uniswap’s governance tokens, UNI, play a crucial role in the ecosystem. UNI holders can propose, debate, and vote on various upgrades and changes to the protocol, including [fee](../f/fee.md) structures and [distribution](../d/distribution.md) of community treasury funds.

### Governance Proposals
Governance in Uniswap V3 happens through the community, enabling any UNI holder to submit proposals. These proposals can [range](../r/range.md) from parameter adjustments to new features and improvements to the protocol. Once submitted, proposals undergo a voting process. If passed, they are implemented by the core development team.

### Fee Governance
Uniswap V3 has an in-built governance mechanism to enable [fee](../f/fee.md) switching. Currently, fees collected from LPs are distributed among them, but the governance system provides an option for a fixed percentage to be redirected to the Uniswap treasury, ensuring community-driven, sustainable future development.

## Performance Metrics

### Total Value Locked (TVL)
TVL is a primary metric for assessing the health of a DeFi protocol. Uniswap V3 has consistently shown high TVL, reflecting the protocol’s [liquidity](../l/liquidity.md) and user [trust](../t/trust.md).

### Transaction Volume
The daily [transaction](../t/transaction.md) [volume](../v/volume.md) on Uniswap V3 is another critical performance metric. High [transaction](../t/transaction.md) volumes signify active use and [trust](../t/trust.md) in the platform’s ability to execute trades effectively.

### User Adoption
The number of active wallets and unique users using Uniswap V3 serves as an [indicator](../i/indicator.md) of its [market penetration](../m/market_penetration.md) and user acceptance. Growing numbers reflect increasing user confidence and broader acceptance in the DeFi space.

### Fee Generation
[Fee](../f/fee.md) generation can be seen as both a measure of [liquidity](../l/liquidity.md) provider profitability and protocol usage. Higher [fee](../f/fee.md) generation implies more trades and thus more utilization of the platform's services.

## Use Cases

### Token Swapping
Token swapping is the most basic use case for Uniswap and remains its primary function. Users can [swap](../s/swap.md) ERC-20 tokens directly from their wallets without needing a centralized intermediary.

### Yield Farming
With Uniswap V3’s concentrated [liquidity](../l/liquidity.md), [yield](../y/yield.md) farming becomes more [capital](../c/capital.md) efficient. LPs can strategically position their [liquidity](../l/liquidity.md) to maximize yields relative to the [risk](../r/risk.md) they are willing to assume.

### Liquidity Mining
Projects can incentivize [liquidity provision](../l/liquidity_provision.md) by rewarding LPs with their native tokens. Such [liquidity](../l/liquidity.md) [mining](../m/mining.md) initiatives can stimulate higher [liquidity](../l/liquidity.md) levels and encourage more decentralized trading activities.

### Decentralized Trading
Uniswap V3 enables decentralized trading with greater [capital](../c/capital.md) [efficiency](../e/efficiency.md), providing a viable alternative to centralized exchanges. Traders benefit from high [liquidity](../l/liquidity.md), [transparency](../t/transparency.md), and eliminated [counterparty](../c/counterparty.md) risks.

## Security Considerations

### Audits
Uniswap V3 has undergone [multiple](../m/multiple.md) third-party audits to ensure the robustness and [security](../s/security.md) of its [smart contracts](../s/smart_contracts_in_trading.md). However, [security](../s/security.md) risks are inherent in any DeFi project, and users should [exercise](../e/exercise.md) caution.

### Flash Loan Attacks
Like other DeFi protocols, Uniswap V3 is susceptible to flash [loan](../l/loan.md) attacks. Such attacks can exploit the price oracles and other mechanisms, emphasizing the need for rigorous [risk management](../r/risk_management.md) practices.

### User Best Practices
Users are advised to follow [best practices](../b/best_practices.md), such as using hardware wallets, double-checking [transaction](../t/transaction.md) approvals, and staying informed about ongoing [security](../s/security.md) updates and community governance changes.

For more detailed information, you can visit the Uniswap official site: [Uniswap](https://uniswap.org/).

## Conclusion

Uniswap V3 represents a significant step forward in decentralized [finance](../f/finance.md). From concentrated [liquidity](../l/liquidity.md) and [multiple](../m/multiple.md) [fee](../f/fee.md) tiers to non-fungible [liquidity](../l/liquidity.md) positions and active [liquidity](../l/liquidity.md) management, Uniswap V3 enhances the sophistication and [efficiency](../e/efficiency.md) of decentralized trading. As DeFi continues to evolve, Uniswap V3 is well-positioned to remain a pivotal player in the ecosystem, [offering](../o/offering.md) advanced trading dynamics backed by [robust](../r/robust.md) governance and a broad community base.