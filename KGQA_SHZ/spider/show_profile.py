import codecs
import json
with open('./spider/json/data.json', encoding='utf-8')as f:
    data = json.load(f)

def get_profile(name):
    s=''
    # print(data)
    # print(name)
    # print(data['data'])
    for i in data[name]:
        st="<dt class = \"basicInfo-item name\" >"+ str(i)+" \
        <dd class = \"basicInfo-item value\" >"+str(data[name][i])+"</dd >"
        s+=st
    # print(s)
    return s

# get_profile('宣赞')