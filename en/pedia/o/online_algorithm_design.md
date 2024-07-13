# Online Algorithm Design

Online [algorithm design](../a/algorithm_design.md) is a subfield of computer science and applied mathematics that involves algorithms which process their input piece-by-piece, without knowing the future input values. This is in contrast to offline algorithms, which have access to the entire input from the beginning. Online algorithms make decisions at each step while the input is revealed piece by piece, typically aiming to provide solutions that are competitive with the optimal offline algorithm.

## Key Concepts

### Competitive Analysis

Competitive analysis is a framework for evaluating the performance of an online algorithm by comparing it to an optimal offline algorithm. The competitive ratio is defined as the worst-case ratio between the cost incurred by the online algorithm and the cost incurred by an optimal offline algorithm. An online algorithm is said to be c-competitive if for all possible input sequences, the cost of the online algorithm is at most c times the cost of the optimal offline algorithm.

### Adversarial Models

Online algorithms often assume adversarial models where an adversary determines the sequence of inputs to maximize the disadvantage of the online algorithm. Common adversarial models include:

- **Oblivious Adversary**: Does not know the internal state of the online algorithm when constructing the input sequence.
- **Adaptive Adversary**: Constructs the input sequence while knowing the internal state of the online algorithm at each step.
- **Adaptive Online Adversary**: Constructs the input while the algorithm proceeds but commits to the entire input sequence before seeing any of the decisions made by the algorithm.

### Greedy Algorithms

Greedy algorithms follow a problem-solving heuristic of making locally optimal choices at each stage with the goal of finding a global optimum. In many online algorithm scenarios, greedy algorithms are used due to their simplicity and [efficiency](../e/efficiency.md).

## Common Online Problems

### Paging Problem

The paging problem is a classic online problem where the goal is to manage a limited-size cache to minimize the number of page faults (requests for pages that are not currently in the cache). Several online strategies exist for this problem, such as:

- **Least Recently Used (LRU)**: Evicts the page that has not been used for the longest period of time.
- **First-In-First-Out (FIFO)**: Evicts the oldest page in the cache.
- **Least Frequently Used (LFU)**: Evicts the page with the lowest access frequency.

### K-Server Problem

The K-server problem involves a set of K servers located at points in a metric space, and a sequence of requests, each of which specifies a point in the metric space. The goal is to move the servers to serve the requests in a way that minimizes the total movement cost. Notable online strategies for this problem include:

- **Work Function Algorithm**: Makes decisions based on the work function, which considers the minimal cost to serve all requests seen so far.
- **Greedy Algorithm**: Moves the nearest server to the requested point.

### Online Bipartite Matching

Online bipartite matching involves a bipartite graph where one set of vertices (Offline Set) is known in advance, while the other set (Online Set) arrives one by one. The online algorithm has to decide immediately and irrevocably whether to match the arriving vertex to an unmatched vertex in the offline set. One prominent solution is the Ranking algorithm, which assigns ranks to the offline vertices and matches online vertices to the highest-ranked available vertex.

### Ski Rental Problem

The ski rental problem exemplifies the balance between renting and buying. Given the cost of renting skis per day and the cost of purchasing skis, the goal is to minimize the total cost without knowing ahead of time how many days skiing [will](../w/will.md) occur. The 2-competitive algorithm rents skis until the cumulative rental cost reaches the purchase cost, then buys the skis.

## Applications in Real World

### Online Ad Allocation

Online ad allocation involves assigning ad slots to advertisers in real-time as users [load](../l/load.md) web pages. This problem is highly relevant in [digital marketing](../d/digital_marketing.md), and online algorithms are used to balance immediate [revenue](../r/revenue.md) versus long-term benefits. Companies like Google [handle](../h/handle.md) these situations using online algorithms ([Google Ads](https://ads.google.com)).

### Ride-Hailing Services

Ride-hailing services such as Uber must match drivers to ride requests dynamically. The goal is to minimize the waiting time for passengers and [idle time](../i/idle_time.md) for drivers. Uber employs online algorithms to optimize this matching process ([Uber](https://www.uber.com)).

### Cloud Resource Management

In [cloud computing](../c/cloud_computing_in_trading.md), resource management involves the dynamic allocation of computational resources. Companies like Amazon Web Services (AWS) use online algorithms to allocate instances to tasks submitted by customers ([AWS](https://aws.amazon.com)). The goal is to maximize resource utilization while minimizing cost and ensuring quality of service.

### Stock Market Trading

[Algorithmic trading](../a/algorithmic_trading.md) involves making transactions in [financial markets](../f/financial_market.md) using pre-programmed codes, where decisions must be made in real time in response to [market](../m/market.md) movements. Companies such as Two Sigma and Renaissance Technologies utilize sophisticated online algorithms to manage portfolios and execute trades ([Two Sigma](https://www.twosigma.com), [Renaissance Technologies](https://www.rentec.com)).

## Example Algorithms and Their Competitive Ratios

### Online Paging Algorithms

1. **LRU (Least Recently Used)**: This algorithm has a competitive ratio of k, where k is the size of the cache.
2. **FIFO (First In, First Out)**: Also has a competitive ratio of k.
3. **LFU (Least Frequently Used)**: Generally does not perform as well as LRU or FIFO in terms of competitive ratio.

### Online K-Server Algorithms

1. **Work Function Algorithm**: For general metric spaces with k servers, the competitive ratio is 2k - 1.
2. **Double Coverage Algorithm**: For the special case of the k-server problem on a line, the competitive ratio is k.

### Online Matching Algorithms

1. **Ranking Algorithm**: In the context of online bipartite matching, the Ranking algorithm achieves a competitive ratio of (1 - 1/e), where e is the base of the natural logarithm.
2. **Greedy Algorithm**: Simple and efficient, but less effective than the Ranking algorithm when performance is measured in terms of competitive ratio.

## Summary

Online [algorithm design](../a/algorithm_design.md) plays a crucial role in situations where decisions must be made sequentially without complete knowledge of future events. By employing techniques like competitive analysis and considering various adversarial models, researchers and practitioners can develop online strategies that perform well compared to optimal offline solutions. These algorithms are essential in a wide [range](../r/range.md) of applications today, from internet advertising to resource management in [cloud computing](../c/cloud_computing_in_trading.md) and financial trading.