screens = [{'gaps': {'bottom': None,
           'left': None,
           'right': None,
           'top': (1440, 1440, 5120, 20)},
  'group': 'main',
  'height': 1440,
  'index': 0,
  'width': 5120,
  'x': 1440,
  'y': 1440},
 {'gaps': {'bottom': None,
           'left': None,
           'right': None,
           'top': (2280, 0, 3440, 20)},
  'group': 'code',
  'height': 1440,
  'index': 1,
  'width': 3440,
  'x': 2280,
  'y': 0},
 {'gaps': {'bottom': None,
           'left': None,
           'right': None,
           'top': (0, 818, 1440, 20)},
  'group': 'www',
  'height': 2560,
  'index': 2,
  'width': 1440,
  'x': 0,
  'y': 818}]

groups = {'code': {'floating_info': {'clients': ['scratchpad', 'scratchpad'],
                            'name': 'floating'},
          'focus': '@Snowman - Discord',
          'focus_history': ['i raided a hacker vault... - YouTube — Mozilla '
                            'Firefox',
                            '@Snowman - Discord'],
          'label': 'code',
          'layout': 'columns',
          'layouts': ['columns', 'floating', 'stack'],
          'name': 'code',
          'screen': 1,
          'tiled_windows': {'@Snowman - Discord',
                            'i raided a hacker vault... - YouTube — Mozilla '
                            'Firefox'},
          'windows': ['i raided a hacker vault... - YouTube — Mozilla Firefox',
                      '@Snowman - Discord']},
 'games': {'floating_info': {'clients': ['scratchpad', 'scratchpad'],
                             'name': 'floating'},
           'focus': '~',
           'focus_history': ['~'],
           'label': 'games',
           'layout': 'columns',
           'layouts': ['columns', 'floating', 'stack'],
           'name': 'games',
           'screen': None,
           'tiled_windows': {'~'},
           'windows': ['~']},
 'main': {'floating_info': {'clients': ['scratchpad', 'scratchpad'],
                            'name': 'floating'},
          'focus': 'qtile cmd-obj -o cmd -f get_groups',
          'focus_history': ['allusive-dev/compfy: A Linux Compositor for X11. '
                            'Based on Picom. Providing Animations, Active '
                            'Support and More! — Mozilla Firefox',
                            'Qtile root object — Qtile '
                            '0.1.dev50+g2b5ad3c.d20240120 documentation — '
                            'Mozilla Firefox',
                            'nvim eww.scss',
                            'Eww Bar - My vault - Obsidian v1.5.3',
                            'Python - Loop Lists — Mozilla Firefox',
                            'nvim config.py',
                            '…/.config/qtile/test',
                            'qtile cmd-obj -o cmd -f get_groups'],
          'label': 'main',
          'layout': 'columns',
          'layouts': ['columns', 'floating', 'stack'],
          'name': 'main',
          'screen': 0,
          'tiled_windows': {'Eww Bar - My vault - Obsidian v1.5.3',
                            'Python - Loop Lists — Mozilla Firefox',
                            'Qtile root object — Qtile '
                            '0.1.dev50+g2b5ad3c.d20240120 documentation — '
                            'Mozilla Firefox',
                            'allusive-dev/compfy: A Linux Compositor for X11. '
                            'Based on Picom. Providing Animations, Active '
                            'Support and More! — Mozilla Firefox',
                            'nvim config.py',
                            'nvim eww.scss',
                            'qtile cmd-obj -o cmd -f get_groups',
                            '…/.config/qtile/test'},
          'windows': ['allusive-dev/compfy: A Linux Compositor for X11. Based '
                      'on Picom. Providing Animations, Active Support and '
                      'More! — Mozilla Firefox',
                      'Python - Loop Lists — Mozilla Firefox',
                      '…/.config/qtile/test',
                      'Eww Bar - My vault - Obsidian v1.5.3',
                      'nvim config.py',
                      'nvim eww.scss',
                      'Qtile root object — Qtile 0.1.dev50+g2b5ad3c.d20240120 '
                      'documentation — Mozilla Firefox',
                      'qtile cmd-obj -o cmd -f get_groups']},
 'terminal': {'floating_info': {'clients': ['scratchpad', 'scratchpad'],
                                'name': 'floating'},
              'focus': 'scratchpad',
              'focus_history': ['scratchpad'],
              'label': '',
              'layout': 'floating',
              'layouts': ['floating'],
              'name': 'terminal',
              'screen': None,
              'tiled_windows': set(),
              'windows': ['scratchpad']},
 'vm': {'floating_info': {'clients': ['scratchpad', 'scratchpad'],
                          'name': 'floating'},
        'focus': None,
        'focus_history': [],
        'label': 'vm',
        'layout': 'columns',
        'layouts': ['columns', 'floating', 'stack'],
        'name': 'vm',
        'screen': None,
        'tiled_windows': set(),
        'windows': []},
 'www': {'floating_info': {'clients': ['scratchpad', 'scratchpad'],
                           'name': 'floating'},
         'focus': 'YouTube — Mozilla Firefox',
         'focus_history': ['YouTube — Mozilla Firefox'],
         'label': 'www',
         'layout': 'columns',
         'layouts': ['columns', 'floating', 'stack'],
         'name': 'www',
         'screen': 2,
         'tiled_windows': {'YouTube — Mozilla Firefox'},
         'windows': ['YouTube — Mozilla Firefox']}}


screen_list = []

state = []
screen_state = []

for qtile_scree in screens:
    print(qtile_scree)
    print(qtile_scree['index'])
    screen = {
            'index' : qtile_scree['index']
            }
    print(screen)
    screen_list.append(screen)

    for qtilegroupname, qtileinfo in groups.items():
        index = 0
        if qtile_scree['index'] == qtileinfo['screen']:
            index = qtile_scree['index']
            group = {
                    'name' : qtilegroupname,
                    'index': index,
                    }
            screen_state.append(dict(group))

for qtilegroupname, qtileinfo in groups.items():
    group = {
            'name' : qtilegroupname,
            'active' : True if qtileinfo['screen'] is not None else False,
            'screen' : qtileinfo['screen']
            }
    state.append(dict(group))

print("screenlist")
print(screen_list)
print("state")
print(state)
print("screen state")
print(screen_state)
