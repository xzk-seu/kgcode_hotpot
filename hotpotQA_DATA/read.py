import os
import json


if __name__ == '__main__':

    with open("hotpot_train_v1.1.json", 'r') as fr:
        data = json.load(fr)

    res = []
    for d in data:
        if d["level"] == "easy":
            res.append(d)
        if len(res) == 10:
            with open("easy_sample_10.json", "w") as fw:
                json.dump(res, fw)
            break
