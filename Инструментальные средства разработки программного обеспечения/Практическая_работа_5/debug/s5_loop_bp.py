# -*- coding: utf-8 -*-
from simlib import run
print('=== Step 3.2: breakpoint inside the loop ===')
run('task_manager_stage3.py', '1|Задача A|1|Задача B|1|Задача C|1|Задача D|3|1|3|2|5|6'.split('|'), 57, ['c']+["p task['title']",'p tasks.index(task)',"p [t['title'] for t in tasks]",'c']*3)
