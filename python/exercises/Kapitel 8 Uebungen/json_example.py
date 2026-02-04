import json
# TEL ist ein Text im JSON Format
TEL ='''{"Tom": ["0172 567 343", "03202 67231"],
"Anna": [],
"Tina": ["0201 897551"]}'''

tel = json.loads(TEL)
for name in tel.keys():
    print(name, tel[name])