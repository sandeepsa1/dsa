def viterbi(obs, states, start_p, trans_p, emit_p):
    # Initialization
    V = [{}]
    path = {}

    for y in states:
        V[0][y] = start_p[y] * emit_p[y].get(obs[0], 0)
        path[y] = [y]

    # Recursion
    for t in range(1, len(obs)):
        V.append({})
        newpath = {}

        for y in states:
            (prob, state) = max((V[t-1][y0] * trans_p[y0].get(y, 0) * emit_p[y].get(obs[t], 0), y0) for y0 in states)
            V[t][y] = prob
            newpath[y] = path[state] + [y]

        path = newpath

    # Termination
    (prob, state) = max((V[len(obs) - 1][y], y) for y in states)
    return (prob, path[state])

# Example usage
states = ('N', 'V', 'D', 'P')
observations = ('the', 'cat', 'chases', 'a', 'mouse', 'with', 'speed')
start_probability = {'N': 0.3, 'V': 0.1, 'D': 0.5, 'P': 0.1}
transition_probability = {
    'D': {'N': 0.8, 'V': 0.1, 'P': 0.1},
    'N': {'V': 0.6, 'P': 0.3, 'N': 0.1},
    'V': {'N': 0.5, 'P': 0.4, 'D': 0.1},
    'P': {'N': 0.8, 'D': 0.2}
}
emission_probability = {
    'D': {'the': 0.5, 'a': 0.5},
    'N': {'cat': 0.3, 'mouse': 0.3, 'speed': 0.2, 'chases': 0.2},
    'V': {'chases': 0.6, 'runs': 0.4},
    'P': {'with': 1.0}
}

prob, sequence = viterbi(observations, states, start_probability, transition_probability, emission_probability)
print(f"Most likely sequence of states: {sequence}")
print(f"Probability of the sequence: {prob}")