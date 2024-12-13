import random

def generate_ascii_chart(current_price):
    # Generate some random historical prices around the current price
    prices = [current_price + random.uniform(-50, 50) for _ in range(10)]
    min_p = min(prices)
    max_p = max(prices)
    # Avoid division by zero
    scale = (max_p - min_p) / 10 if (max_p - min_p) != 0 else 1

    lines = []
    for p in prices:
        # Determine "height" of each bar relative to the min value
        height = int((p - min_p) / scale)
        line = "#" * max(height, 1)  # ensure at least one mark
        lines.append(line)
    return "\n".join(lines)

