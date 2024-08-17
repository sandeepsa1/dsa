## Greedy Algorithm
A greedy algorithm is an approach to solving optimization problems by making a series of decisions, each of which is locally optimal at the time. The idea is that by making the best possible choice at each step, the algorithm will ultimately arrive at a globally optimal solution.<br/><br/>

Samples included here are;
1. <b>Best Time to Buy and Sell Stock</b>: Given an array where the i-th element is the price of a given stock on day i, find the maximum profit.
2. <b>Coin Change Problem</b>: Given a set of coin denominations and an amount, find the minimum number of coins needed to make the amount.


### 1. Best Time to Buy and Sell Stock
Given an array 'prices[]' where 'prices[i]' is the price of a given stock on day 'i,' find the maximum profit achieveable by buying and selling the stock. Stock can be baught or sold only once and must buy before sell.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(1)</b></br>

#### Steps
The idea is to traverse the price array while keeping track of the minimum price seen so far and calculating the profit if the stock were sold at the current day's price. The maximum profit is updated if this profit is greater than the previously recorded maximum profit.

### 2. Coin Change Problem
Given a set of coin denominations and an amount, find the minimum number of coins needed to make the amount.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(1)</b></br>

#### Steps
Always pick the largest coin denomination that doesn’t exceed the remaining amount. This works well if the coin denominations are like '1, 5, 10, 25', but it might fail for other sets of denominations.


### Common Examples of Greedy Algorithms
1. <b>Dijkstra's Algorithm</b>: Finds the shortest path from a source node to all other nodes in a graph. It always picks the node with the smallest known distance that hasn't been processed yet.
2. <b>Kruskal's Algorithm</b>: Used to find the Minimum Spanning Tree (MST) of a graph. It always picks the smallest edge that doesn't form a cycle.
3. <b>Prim's Algorithm</b>: Another algorithm for finding the MST, but it grows the MST one edge at a time by adding the smallest edge connecting the MST to a node not yet in the MST.
4. <b>Activity Selection Problem</b>: Given a set of activities with start and end times, the goal is to select the maximum number of activities that don't overlap. The greedy choice is to always pick the next activity that finishes the earliest.
5. <b>Huffman Coding</b>: A greedy algorithm used for lossless data compression. It builds a binary tree with the shortest codes for the most frequent characters.

### Advantages of Greedy Algorithms
1. <b>Efficiency</b>: Greedy algorithms tend to be faster and easier to implement than other algorithms like dynamic programming or backtracking.
2. <b>Simplicity</b>: They are straightforward and often lead to a quick solution.

### Disadvantages of Greedy Algorithms
1. <b>Not Always Optimal</b>: Greedy algorithms do not always produce the optimal solution for every problem. They work best for problems that have the greedy choice property.
2. <b>Problem-Specific</b>: A greedy approach needs to be tailored to the specific problem and doesn't generalize well.