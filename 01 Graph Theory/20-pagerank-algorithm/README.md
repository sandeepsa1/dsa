## PageRank Algorithm
PageRank is an algorithm used to rank web pages in search engine results. Developed by Larry Page and Sergey Brin, the founders of Google, it works by counting the number and quality of links to a page to determine a rough estimate of the website's importance. The underlying assumption is that more important websites are likely to receive more links from other websites.</br>

1. Time complexity: <b>𝑂(I. (E + n) )</b>
2. Space complexity: <b>𝑂(E + n)</b></br>
I is the number of iterations, E is the number of edges, and n is the number of nodes.


### Key Concepts
1. Links as Votes:
   - A link from one page to another is considered a vote of confidence. However, not all votes are equal. Pages that are themselves highly ranked carry more weight.
2. Random Surfer Model:
   - Imagine a user randomly surfing the web by clicking on links. The probability that the user lands on a particular page is its PageRank.
3. Damping Factor:
   - To model the probability that a user continues clicking links, a damping factor (typically 0.85) is used. There is a 15% chance that the user will jump to a random page instead of following a link.

### PageRank Formula
The PageRank <b>PR(P)</b> of a page <b>P</b> is given by the following formula:

$\ 
PR(P) = \frac{1-d}{N} + d \left( \sum_{i \in L(P)} \frac{PR(i)}{C(i)} \right)
\$


$\[\text{PR(P)} = \frac{1-d}{N} + d \left( \sum_{i \in L(P)} \right)   \]$

- <b>PR(P)</b>: The PageRank of page \( P \).
- <b>d</b>: Damping factor, usually set to 0.85. It represents the probability that a user will continue clicking on links.
- <b>N</b>: Total number of pages in the network.
- <b>L(P)</b>: Set of pages that link to page \( P \).
- <b>PR(i)</b>: PageRank of page \( i \) that links to page \( P \).
- <b>C(i)</b>: Number of outbound links on page \( i \).

### How this works
1. Initialization:
   - Each page starts with an equal rank, representing the initial probability distribution.
2. Transition Matrix:
   - Construct the transition matrix based on the out-links. For example, page 0 links to pages 1 and 2, so its probabilities are divided among these pages.
3. Iterative Update:
   - The ranks are updated iteratively using the transition matrix and the damping factor until convergence.
4. Result:
   - The final rank vector represents the steady-state distribution of the random walk, indicating the relative importance of each page.

### Uses
Beyond web search, PageRank has applications in social network analysis, recommendation systems, and citation networks, illustrating its versatility and power as a graph-based ranking algorithm.