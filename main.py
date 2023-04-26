from opcut import common
from opcut import calculate

data = {
    'cut_width': 0.3,
    'min_initial_usage': True,
    'panels': {
        'Panel1': {'width': 89, 'height': 100},
        'Panel2': {'width': 89, 'height': 100},
        'Panel3': {'width': 89, 'height': 100}
    },
    'items': {
        'Item1': {'width': 45, 'height': 100, 'can_rotate': True},
        'Item2': {'width': 25, 'height': 100, 'can_rotate': True},
        'Item3 1': {'width': 20, 'height': 100, 'can_rotate': True},
        'Item3 2': {'width': 20, 'height': 100, 'can_rotate': True},
        'Item3 3': {'width': 20, 'height': 100, 'can_rotate': True},
        'Item4': {'width': 35, 'height': 100, 'can_rotate': True}
    }
}
method = "forward_greedy_native"

method = common.Method(method)
params = common.params_from_json(data)
output = calculate.calculate(method=method,params=params)
print(output)