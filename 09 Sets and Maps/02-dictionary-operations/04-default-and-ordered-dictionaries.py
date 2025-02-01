from collections import defaultdict, OrderedDict

# Default Dictionary
dd = defaultdict(int)
dd['x'] += 5
print("DefaultDict:", dict(dd))  # {'x': 5}

# Ordered Dictionary
od = OrderedDict()
od['one'] = 1
od['two'] = 2
od['three'] = 3
print("OrderedDict:", od)  # OrderedDict([('one', 1), ('two', 2), ('three', 3)])

# Move 'two' to end
od.move_to_end('two')
print("After move_to_end:", od)  # OrderedDict([('one', 1), ('three', 3), ('two', 2)])