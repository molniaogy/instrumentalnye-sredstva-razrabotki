# -*- coding: utf-8 -*-
from simlib import run
print('=== Step 2: breakpoint in mark_task_done ===')
run('task_manager_original.py', '1|Купить хлеб|1|Сделать ДЗ|1|Погулять|3|1|3|2|3|3|6'.split('|'), 29, ['c','p task_id',"p [t['id'] for t in tasks]","p tasks[task_id]['title']",'c','p task_id',"p tasks[task_id]['title']",'c','p task_id','p len(tasks)','c'])
