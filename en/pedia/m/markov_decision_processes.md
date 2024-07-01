# Markov Decision Processes (MDPs)

## Introduction
Markov Decision Processes (MDPs) are mathematical frameworks used for modeling decision-making in environments where outcomes are partly random and partly under the control of a decision maker. MDPs are widely used in a variety of fields, including robotics, economics, manufacturing, and finance. They provide a rigorous foundation for analyzing and optimizing sequential decision-making problems, where each action influences not only immediate rewards but also future states and rewards.

## Components of MDPs
An MDP is generally defined by the following components:

### States (\(S\))
The set of all possible states \(S\) represents every conceivable situation the agent could find itself in. Each state contains all the information needed to make a decision.
- **Example**: In a stock [trading environment](../t/trading_environment.md), a state could be represented by the current prices of different stocks, available funds, and existing portfolio holdings.

### Actions (\(A\))
The set of all possible actions \(A\) includes all the decisions the agent can make in any state.
- **Example**: In the same stock [trading environment](../t/trading_environment.md), actions might include buying, selling, or holding a stock.

### Transition Probabilities (\(T\) or \(P\))
The transition probabilities \( P(s'|s,a) \) describe the likelihood of moving from state \( s \) to state \( s' \) given action \( a \). The probabilities must satisfy the Markov property, implying that the future state depends only on the current state and action, not on the history of states and actions.
- **Example**: If an agent buys a stock, the transition probability would estimate the likelihood of various changes in the stock's price.

### Rewards (\(R\))
The reward function \( R(s,a,s') \) specifies the immediate reward received after transitioning from state \( s \) to state \( s' \) due to action \( a \). This quantitatively represents the benefit of taking a particular action in a given state.
- **Example**: In a [trading environment](../t/trading_environment.md), the reward could be the profit or loss resulting from buying or selling a stock.

## Formal Definition
An MDP can be formally defined as a tuple \( (S, A, P, R, \gamma) \), where:
- \( S \) is the state space
- \( A \) is the action space
- \( P \) is the transition probability function
- \( R \) is the reward function
- \( \gamma \) is the discount factor, which determines the present value of future rewards

## Policies
A policy \( \pi \) is a strategy used by the agent, specifying the action to take in each state. Policies can be deterministic (\( \pi(s) = a \)) or stochastic (\( \pi(a|s) \)), where the latter is a probability distribution over actions given a state.

### Optimal Policy
The goal in MDPs is to find an optimal policy \( \pi^* \) that maximizes the expected cumulative reward over time. This is often formalized using the value function or the action-value function.

## Value Functions
Value functions are used to estimate the long-term benefits of states or state-action pairs under a given policy. Two primary types of value functions are:

### State Value Function (\( V^\pi(s) \))
The state value function \( V^\pi(s) \) represents the expected cumulative reward of starting in state \( s \) and following policy \( \pi \).

\[ V^\pi(s) = \mathbb{E}_\pi \left[ \sum_{t=0}^{\infty} \gamma^t R(s_t, a_t, s_{t+1}) \mid s_0 = s \right] \]

### Action-Value Function (\( Q^\pi(s, a) \))
The action-value function \( Q^\pi(s, a) \) represents the expected cumulative reward of starting in state \( s \), taking action \( a \), and thereafter following policy \( \pi \).

\[ Q^\pi(s, a) = \mathbb{E}_\pi \left[ \sum_{t=0}^{\infty} \gamma^t R(s_t, a_t, s_{t+1}) \mid s_0 = s, a_0 = a \right] \]

### Bellman Equations
The Bellman equations provide recursive relationships for value functions, essential for solving MDPs.

#### Bellman Expectation Equation for \( V^\pi \)

\[ V^\pi(s) = \sum_{a \in A} \pi(a|s) \left[ R(s, a) + \gamma \sum_{s' \in S} P(s' | s, a) V^\pi(s') \right] \]

#### Bellman Expectation Equation for \( Q^\pi \)

\[ Q^\pi(s, a) = R(s, a) + \gamma \sum_{s' \in S} P(s' | s, a) \sum_{a' \in A} \pi(a'|s') Q^\pi(s', a') \]

## Solution Methods
There are several methods for finding optimal policies in MDPs, categorized into dynamic programming, Monte Carlo, and temporal difference methods.

### Dynamic Programming
Dynamic programming methods leverage the Bellman equations to iteratively improve value estimates and policies. Key algorithms include:

#### Value Iteration
Value iteration repeatedly updates the state value function until it converges to the optimal value function.

\[ V_{k+1}(s) = \max_{a \in A} \left[ R(s, a) + \gamma \sum_{s' \in S} P(s' | s, a) V_k(s') \right] \]

#### Policy Iteration
Policy iteration alternates between policy evaluation (estimating the value function for a given policy) and policy improvement (generating a better policy based on the current value function).

1. **Policy Evaluation**: Solve \( V^\pi(s) \) for the current policy \( \pi \).
2. **Policy Improvement**: Update the policy \( \pi \) using the updated value function.

\[ \pi'(s) = \arg\max_{a \in A} \left[ R(s, a) + \gamma \sum_{s' \in S} P(s' | s, a) V^\pi(s') \right] \]

### Monte Carlo Methods
[Monte Carlo methods](../m/monte_carlo_methods.md) estimate value functions based on sample episodes from the MDP. These methods do not require knowledge of transition probabilities and are used in model-free contexts.

#### First-Visit MC
First-Visit Monte Carlo updates the value function based on the first occurrence of each state or state-action pair in an episode.

#### Every-Visit MC
Every-Visit Monte Carlo updates the value function based on every occurrence of each state or state-action pair in an episode.

### Temporal Difference (TD) Learning
Temporal difference methods combine the ideas of dynamic programming and [Monte Carlo methods](../m/monte_carlo_methods.md). TD learning updates value estimates based on the difference (temporal difference) between consecutive value estimates.

#### TD(0)
TD(0) is the simplest form, updating the value function using a single step lookahead.

\[ V(s_t) \leftarrow V(s_t) + \alpha \left[ R_{t+1} + \gamma V(s_{t+1}) - V(s_t) \right] \]

#### Q-Learning
Q-Learning is an off-policy TD control algorithm that learns the optimal policy independent of the agent's actions.

\[ Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha \left[ R_{t+1} + \gamma \max_{a} Q(s_{t+1}, a) - Q(s_t, a_t) \right] \]

#### SARSA
SARSA is an on-policy TD control algorithm that updates the action-value function based on the agent's actions following the current policy.

\[ Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha \left[ R_{t+1} + \gamma Q(s_{t+1}, a_{t+1}) - Q(s_t, a_t) \right] \]

## Applications in Algorithmic Trading
MDPs have significant applications in [algorithmic trading](../a/algorithmic_trading.md), where agents must make sequential decisions under uncertainty to maximize returns. 

### Optimal Execution
One of the key applications is optimal trade execution, wherein an agent determines the best times and quantities to trade to minimize transaction costs and market impact.

### Portfolio Management
MDPs can be used for dynamic [portfolio optimization](../p/portfolio_optimization.md), where the agent adjusts its holdings in response to changing market conditions to achieve a balance between risk and return.

### Market Making
Agents can use MDPs to design optimal market-making strategies, setting bid-ask spreads based on likely future price movements to maximize profit from the spread while managing inventory risk.

### Reinforcement Learning in Trading
Reinforcement learning, encompassing many MDP solution methods, is used for developing sophisticated [trading algorithms](../t/trading_algorithms.md). Platforms like [Alpaca](https://alpaca.markets/) and [QuantConnect](https://www.quantconnect.com/) provide environments for testing and deploying these strategies.

## Conclusion
Markov Decision Processes offer a robust framework for solving sequential decision-making problems in stochastic environments. With their ability to balance immediate and future rewards, they are indispensable in various fields, particularly in [algorithmic trading](../a/algorithmic_trading.md), where they help design strategies to optimize financial returns under uncertainty. Through methods including dynamic programming, Monte Carlo, and temporal difference learning, MDPs facilitate the development of optimal policies for complex, real-world problems.