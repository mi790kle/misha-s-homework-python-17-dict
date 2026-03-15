import statistics
import random


def get_statistics(numbers: list) -> dict:
    result = {
        "sum": sum(numbers),
        "avg": statistics.mean(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "length": len(numbers),
    }
    return result

numbers = []
for i in range(5):
    numbers.append(random.randint(1, 20))
print(numbers)
print(get_statistics(numbers))