def normalize_data(data):
    if not data:
        return []

    min_val = min(data)
    max_val = max(data)

    if min_val == max_val:
        return [0] * len(data)

    return [(x - min_val) / (max_val - min_val) for x in data]

data = [10, 20, 30, 40, 50]
normalized_data = normalize_data(data)
print(normalized_data)