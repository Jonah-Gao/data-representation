import json

dict = {}

for i in range(205744):
    dict[chr(i)] = f"U+{str(hex(i)).split('x')[-1].zfill(4).upper()}"

json_object = json.dumps(dict, indent=4)
# store characters instead of unicode in json,
# my laptop uses gbk encoding instead of utf so certain characters have encoding errors
# json_object = json.dumps(dict, indent=4, ensure_ascii=False)

with open('unicode_inverted.json', 'w') as f:
    f.write(json_object)

dict = {}

for i in range(205744):
    dict[f"U+{str(hex(i)).split('x')[-1].zfill(4).upper()}"] = chr(i)

json_object = json.dumps(dict, indent=4)
# store characters instead of unicode in json,
# my laptop uses gbk encoding instead of utf so certain characters have encoding errors
# json_object = json.dumps(dict, indent=4, ensure_ascii=False)

with open('unicode.json', 'w') as f:
    f.write(json_object)
