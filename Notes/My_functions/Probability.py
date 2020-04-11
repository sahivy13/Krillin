def prob_in_list(event: list, possible_outcomes: list) -> float:
    return sum([possible_outcomes.count(e) for i in event]) / len(possible_outcomes)

def probability(num_events, numpossible_outcomes):
    return num_events / nym_possible_outcomes

def in_a_row(prob, times):
    return prob ** times