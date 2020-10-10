import os
import json
"""
验证**full wiki** 的支撑事实不一定在当前问题的context中
"""

with open("hotpot_dev_fullwiki_v1.json", 'r') as fr:
    data = json.load(fr)

res = []
count = 0
for d in data:
    facts = d["supporting_facts"]
    facts = [x[0] for x in facts]
    contexts = d["context"]
    contexts = [x[0] for x in contexts]
    for f in facts:
        if f not in contexts:
            print(f)
            count += 1
            break

print(count)
print(len(data))
