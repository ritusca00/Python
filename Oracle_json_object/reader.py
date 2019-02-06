# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 19:37:08 2019

@author: blizn
"""

import json
import connect
import pandas as pd

cursor.execute("""SELECT json_object('workers' IS (SELECT JSON_ARRAYAGG(JSON_OBJECT('name' IS s.name,
                                                                  'workday' IS to_char(s.workday,'YYYY.MM.DD'),
                                                                  'hours' IS s.hours))
                                   FROM json_data s))
  FROM dual""",())
json_obj = cursor.fetchone()
jsonObj = json.dumps(json_obj)
data = json.loads(jsonObj ) 
print(data)
