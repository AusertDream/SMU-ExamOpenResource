import requests
import re
with open('test.txt','a',encoding='utf-8') as f:
    for i in range(1,100):
        url=f'https://portal.shmtu.edu.cn/xsydxhdgg?page={i}'
        header={
            # 填自己的cookie
            'Cookie': ''
        }
        resp=requests.get(url,headers=header).text


        get_name=re.compile(r'</span><p><a href="(?P<url>.*?)" rel="noopener noreferrer" target="_blank">(?P<name>.*?)</a></p></td>',re.S)
        get_con=re.compile(r'<div class="field-item even">(?P<context>.*?)<div class="field field-name-field-department field-type-taxonomy-term-reference field-label-inl',re.S)
        pat=re.compile("<.*?>")
        names=re.findall(get_name,resp)

        for url,name in names:
            resp2=requests.get("https://portal.shmtu.edu.cn"+url,headers=header).text
            con=re.findall(get_con,resp2)[0]
            con=re.sub(r'</p>','\n',con)
            con=re.sub(r'<.*?>','',con)
            f.write(name+'\n')
            f.write(con+'\n')
            f.write('\n\n\n\n\n')

