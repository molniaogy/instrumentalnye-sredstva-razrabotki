# -*- coding: utf-8 -*-
from simlib import run
print('=== Bug 5: duplicate IDs after deletion ===')
run('task_manager_stage_ids.py', '1|A|1|B|1|C|4|1|1|D|2|3|3|2|6'.split('|'))
