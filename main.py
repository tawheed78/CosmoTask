list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]

def merge_lists(list_1, list_2) -> list:
    list_3 = []
    for val1 in list_1:
        for val2 in list_2:
            if val1["id"] == val2["id"]:
                merged_values = {**val1, **val2}
                list_3.append(merged_values)
                list_2.remove(val2)
                break
        else:
            list_3.append(val1)
    for val2 in list_2:
        if val2 not in list_3:
            list_3.append(val2)
                
    return list_3


list_3 = merge_lists(list_1, list_2)
