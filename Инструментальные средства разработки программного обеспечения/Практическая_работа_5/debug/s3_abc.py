# -*- coding: utf-8 -*-
from simlib import run
print('=== Step 3.1: ValueError on input abc ===')
run('task_manager_original.py', '1|Купить хлеб|3|abc'.split('|'))
