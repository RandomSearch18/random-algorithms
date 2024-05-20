task_1_graph = {
    "A": ["C"],
    "B": ["C", "D"],
    "C": ["E", "F"],
    "D": ["A", "F"],
    "E": []
}

print("Task 1:", task_1_graph)

task_2_graph = {
    "A": {
        "C": 7,
    },
    "B": {
        "C": 4,
        "D": 5,
    },
    "C": {
        "D": 8,
        "E": 2,
        "F": 10,
    },
    "D": {
        "A": 13,
        "F": 6,
    },
    "E": {},
    "F": {},
}

print("Task 2:", task_2_graph)
