import json
import pprint

from libqtile.command.client import InteractiveCommandClient

def get_icons(group):
    icons = {
        'dashboard': '<U+F056E>',
        'main': '<U+F0C8>',
        'alt': '<U+F111>',
        'vms': '<U+EA7A>',
        'gaming': '<U+F11B>',
    }

    return icons[group]

pp = pprint.PrettyPrinter()
c = InteractiveCommandClient()

groups = {}

# Returns a tuple of (default: bool, name: list[str|int])
# Only grab the first 5 names. The groups I initially configure less scratchpads
qtile_groups = c.items('group')[1][0:5]

for qtile_group in qtile_groups:
    qtile_group_info = c.group[qtile_group].info()
    
    group = {
        'name': qtile_group,
        'active': True if qtile_group_info['screen'] is not None else False,
        'open_window': True if len(qtile_group_info['windows']) >= 1 else False,
    }

    groups[qtile_group] = group

with open('/tmp/qtile.state', 'w') as f:
    json.dump(groups, f)
