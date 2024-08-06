items = [
    "s24", "iphone13",
    "s24", "a55",
    "iphone13", "tab9"
]

unique_items = []

for i in items:
    if i not in unique_items:
        unique_items.append(i)

print(unique_items)
