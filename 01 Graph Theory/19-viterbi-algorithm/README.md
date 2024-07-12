## Viterbi Algorithm
The Viterbi algorithm is a dynamic programming algorithm used to find the most likely sequence of hidden states (also known as the Viterbi path) that results in a sequence of observed events, especially in the context of hidden Markov models (HMMs).</br></br>

Viterbi algorithm is not typically classified as a part of graph theory; instead, it is primarily used in the context of dynamic programming and probabilistic modeling. However, it can be related to graph theory in a conceptual way, as it involves finding the most likely path through a sequence of states, which can be visualized as a path-finding problem on a graph where nodes represent states and edges represent transitions with associated probabilities.</br>

1. Time complexity: <b>𝑂(T.N<sup>3</sup>>)</b>
2. Space complexity: <b>𝑂(n<sup>2</sup>>)</b>
<b>T</b> is the number of observations and <b>N</b> is the number of states.


### How this works
1. Initialization:
   - Initialize the starting probabilities.
2. Recursion:
   - Compute the most probable path up to each state.
3. Termination:
   - Identify the final state with the highest probability.number of lines.
4. Path backtracking:
   - Trace back the path to get the most probable sequence.

### Uses
Viterbi algorithm is widely used in various applications, including speech recognition, bioinformatics, and decoding of convolutional codes in telecommunications.

https://www.youtube.com/watch?v=IqXdjdOgXPM