## Topological Sorting
This repository contains the implementation of the topological sort algorithm for a directed acyclic graph (DAG). A topological sorting is an ordering of the nodes in a directed graph where for each directed edge from node A to node B, node A apprears before node B in the ordering.</br>
Not every graph can have topological ordering, for example, a graph with a cycle. That means, the only graphs that can have topological sorting are directed acyclic graphs.</br>
https://www.youtube.com/watch?v=eL-KzMXSXXI


1. Time complexity: 𝑂(V + E)
2. Space complexity: 𝑂(V + E)


### Uses
Topological sorting is a fundamental algorithm that finds its application in any scenario where tasks, data, or resources need to be ordered based on dependency constraints. Some usages listed below.
1. Game Development:
   1. Resource Loading: In game development, resources such as textures, sounds, and models often have dependencies. Topological sorting helps determine the order in which these resources should be loaded to ensure that all dependencies are satisfied.
2. Network Analysis:
   1. Deadlock Prevention: In distributed systems and operating systems, topological sorting can help analyze dependencies to prevent deadlocks by ensuring a proper order of resource allocation.
3. Dependency Parsing in Natural Language Processing (NLP):
   1. Syntax Analysis: In NLP, dependency parsing involves analyzing the grammatical structure of a sentence. Topological sorting can help determine the order of words based on their dependencies to construct parse trees.
4. Data Serialization:
   1. Serialization of Data: When serializing objects that have interdependencies (e.g., databases, configuration files), topological sorting ensures that objects are serialized in an order that respects their dependencies.
5. Project Management:
   1. In Project Management to determine order of tasks that need to be completed.
6. Course Prerequisites:
   1. Academic Planning: In academic settings, topological sorting can be used to determine the order in which courses should be taken based on their prerequisites.

### How it works
The topological sort algorithm works by iterating through the graph and keeping track of the visited nodes. It uses Depth-First Search (DFS) to explore the graph and then places each vertex onto a stack, which gives the topological ordering of the graph.