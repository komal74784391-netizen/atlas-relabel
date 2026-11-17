"""Adaptive relabeling policies."""


def uniform_batch(items, budget):
    return items[:budget]


def margin_batch(items, budget, scores):
    ranked = sorted(items, key=lambda x: scores[x], reverse=True)
    return ranked[:budget]
