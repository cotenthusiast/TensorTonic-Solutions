def target_encoding(categories: list, targets: list) -> list:
    """
    Returns each category replaced by its mean target.
    """
    # Write code here
    encoded = {}

    counts = {}
    totals = {}

    for i in range(len(categories)):
        category = categories[i]
        if category in counts:
            counts[category] += 1
            totals[category] += targets[i]
        else:
            counts[category] = 1
            totals[category] = targets[i]

    return [totals[category] / counts[category] for category in categories]