tpl = (1, 2, 3)
repeat_count = 3
repeated = tuple(item for item in tpl for _ in range(repeat_count))
print(repeated)