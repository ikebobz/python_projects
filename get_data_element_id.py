# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 20:47:28 2023

@author: HI LEAD
"""

import pandas as p 
import numpy as np
import re
import os



switch = 0
dframe = p.read_excel("category_combinations.xlsx",sheet_name = 'category_combinations')
dictr = dframe.to_dict('dict')
def main():
    df = p.read_excel("data_elements_new.xlsx",sheet_name = 'data_elements_new')
    delements = p.read_excel("Updated DMEL-reviewed.xlsx",sheet_name = 'pmtct',usecols=['Data Element Name'])
    fh = open(r'C:/Users/HI LEAD/Downloads/dhis_forms/index.txt','r')
    fc = fh.read()
    findDataElement(delements,df)
    #print(df)
def findDataElement(elements,df):
    f = open('source.html','a')
    """for m in re.findall('(<td rowspan\s*=\s*"\d+">)((?!M|F)[\w\s\(\)\-\/\+]+)(</td>)',text):
        #print(m[1])
        getElementID(m[1],df,f)"""
    for index,row in elements.iterrows():
        #print(row['Data Element Name'])
        dataelement =row['Data Element Name']
        getElementID(dataelement,df,f)
    f.close()
def getElementID(text,df,file):
    global switch
    if text == "Community":
        switch = 1
        file.writelines('------Community-------------')
    count = 0
    #print(text)
    #val = df[df['DataElementName'] == 'HFR_{}'.format(text)]['ID']
    for index,row in df.iterrows():
        count = count + 1
        de = row['DataElementName'].strip().replace('HFR1_','')
        original = row['DataElementName'].strip()
        if de == text:
            print(de)
            elementid = row['ID']
            #print(elementid)
            if switch == 0:
             #renderHTML(elementid,original,original,file)
             renderPMTCT(elementid,original,text,file)
            else:
             renderHTML_community(elementid,original,original,file)
            break
    #print(count)
def renderHTML(id,displayname,topic,f):
    f.writelines('<tr>')
    f.writelines('<td rowspan ="1">{}</td>'.format(topic))
    f.writelines('<td><b>M</b></td>')
    f.writelines('<td><input id="{}-G1LQ16eaem8-val" name="entryfield" title="{} &lt;1, Male" value="[ {} &lt;1, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-jDpI0eT1OdT-val" name="entryfield" title="{} 1-4, Male" value="[ {} 1-4, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-taiY9ViQHEx-val" name="entryfield" title="{} 5-9, Male" value="[ {} 5-9, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-ZFV8pz8qJCD-val" name="entryfield" title="{} 10-14, Male" value="[ {} 10-14, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-BE9736NBqTG-val" name="entryfield" title="{} 15-19, Male" value="[ {} 15-19, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-AodN9PsJwm8-val" name="entryfield" title="{} 20-24, Male" value="[ {} 20-24, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-HhSZ8L0sH2G-val" name="entryfield" title="{} 25-29, Male" value="[ {} 25-29, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-ezFMF91jO1m-val" name="entryfield" title="{} 30-34, Male" value="[ {} 30-34, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-P4BaUZGl9Vi-val" name="entryfield" title="{} 35-39, Male" value="[ {} 35-39, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-Rd0ws8yXWxn-val" name="entryfield" title="{} 40-44, Male" value="[ {} 40-44, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-vNaNlCB4BwV-val" name="entryfield" title="{} 45-49, Male" value="[ {} 45-49, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-yU7kij6mucu-val" name="entryfield" title="{} 50+, Male" value="[ {} 50+, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td name="total">&nbsp;</td>')
    f.writelines('</tr>')
    f.writelines('<tr>')
    f.writelines('<td><b>F</b></td>')
    f.writelines('<td><input id="{}-LlfgaBfFcDq-val" name="entryfield" title="{} &lt;1, Female" value="[ {} &lt;1, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-cP7avw9gpQn-val" name="entryfield" title="{} 1 - 4, Female" value="[ {} 1 - 4, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-ZbWsDaBYzm1-val" name="entryfield" title="{} 5-9, Female" value="[ {} 5-9, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-I6DQzb2QdxK-val" name="entryfield" title="{} 10--14, Female" value="[ {} 10--14, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-pQ1kYROcld1-val" name="entryfield" title="{} 15-19, Female" value="[ {} 15-19, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-glvQ8d4CjTW-val" name="entryfield" title="{} 20-24, Female" value="[ {} 20-24, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-kdVFueLRMXZ-val" name="entryfield" title="{} 25-29, Female" value="[ {} 25-29, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-lm9gPLileIB-val" name="entryfield" title="{} 30-34, Female" value="[ {} 30-34, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-I9g7aOeV7Cl-val" name="entryfield" title="{} 35-39, Female" value="[ {} 35-39, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-wRQfAI2HWrY-val" name="entryfield" title="{} 40-44, Female" value="[ {} 40-44, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-jd0mfLhh9Cf-val" name="entryfield" title="{} 45-49, Female" value="[ {} 45-49, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-EbEIm0ochDr-val" name="entryfield" title="{} 50+, Female" value="[ {} 50+, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td name="total">&nbsp;</td>')
    f.writelines('</tr>')
def renderHTML_community(id,displayname,topic,f):
    f.writelines('<tr>')
    f.writelines('<td rowspan ="1">{}</td>'.format(topic))
    f.writelines('<td><b>M</b></td>')
    f.writelines('<td><input id="{}-IkOpsrTL0BT-val" name="entryfield" title="{} &lt;1, Male" value="[ {} &lt;1, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-LJwQDziqJb5-val" name="entryfield" title="{} 1-4, Male" value="[ {} 1-4, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-ca87S73J9t5-val" name="entryfield" title="{} 5-9, Male" value="[ {} 5-9, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-ZheuyhRCR6f-val" name="entryfield" title="{} 10-14, Male" value="[ {} 10-14, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-N7Y1I36Tiwt-val" name="entryfield" title="{} 15-19, Male" value="[ {} 15-19, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-m8wQFqR4G0l-val" name="entryfield" title="{} 20-24, Male" value="[ {} 20-24, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-obDo0Fu83df-val" name="entryfield" title="{} 25-29, Male" value="[ {} 25-29, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-bVesgHe2SCz-val" name="entryfield" title="{} 30-34, Male" value="[ {} 30-34, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-p3uUf6wMDkz-val" name="entryfield" title="{} 35-39, Male" value="[ {} 35-39, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-WepGnPVeRZf-val" name="entryfield" title="{} 40-44, Male" value="[ {} 40-44, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-AweyRPXLuxm-val" name="entryfield" title="{} 45-49, Male" value="[ {} 45-49, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-DOwyVUwGOkV-val" name="entryfield" title="{} 50+, Male" value="[ {} 50+, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td name="total">&nbsp;</td>')
    f.writelines('</tr>')
    f.writelines('<tr>')
    f.writelines('<td><b>F</b></td>')
    f.writelines('<td><input id="{}-eMEfB41kz0A-val" name="entryfield" title="{} &lt;1, Female" value="[ {} &lt;1, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-FPwA7y28OoQ-val" name="entryfield" title="{} 1 - 4, Female" value="[ {} 1 - 4, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-Dw6BbW2VMd7-val" name="entryfield" title="{} 5-9, Female" value="[ {} 5-9, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-I6hMs4H6Y5z-val" name="entryfield" title="{} 10--14, Female" value="[ {} 10--14, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-H1eDstn4AfY-val" name="entryfield" title="{} 15-19, Female" value="[ {} 15-19, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-AhsOQTGdZjT-val" name="entryfield" title="{} 20-24, Female" value="[ {} 20-24, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-U45kuDppvvs-val" name="entryfield" title="{} 25-29, Female" value="[ {} 25-29, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-KAVKLmYeUBs-val" name="entryfield" title="{} 30-34, Female" value="[ {} 30-34, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-YmSyRRfzUAk-val" name="entryfield" title="{} 35-39, Female" value="[ {} 35-39, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-Hwjg5YyMGC1-val" name="entryfield" title="{} 40-44, Female" value="[ {} 40-44, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-MEov0DwDawU-val" name="entryfield" title="{} 45-49, Female" value="[ {} 45-49, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-r8i8lZSDkg8-val" name="entryfield" title="{} 50+, Female" value="[ {} 50+, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td name="total">&nbsp;</td>')
    f.writelines('</tr>')
def renderFineAge(id,displayname,topic,f):
    f.writelines('<tr>')
    f.writelines('<td rowspan ="2">{}</td>'.format(topic))
    f.writelines('<td><b>M</b></td>')
    f.writelines('<td><input id="{}-IkOpsrTL0BT-val" name="entryfield" title="{} &lt;1, Male" value="[ {} &lt;1, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-LJwQDziqJb5-val" name="entryfield" title="{} 1-4, Male" value="[ {} 1-4, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-ca87S73J9t5-val" name="entryfield" title="{} 5-9, Male" value="[ {} 5-9, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-ZheuyhRCR6f-val" name="entryfield" title="{} 10-14, Male" value="[ {} 10-14, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-N7Y1I36Tiwt-val" name="entryfield" title="{} 15-19, Male" value="[ {} 15-19, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-m8wQFqR4G0l-val" name="entryfield" title="{} 20-24, Male" value="[ {} 20-24, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-obDo0Fu83df-val" name="entryfield" title="{} 25-29, Male" value="[ {} 25-29, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-bVesgHe2SCz-val" name="entryfield" title="{} 30-34, Male" value="[ {} 30-34, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-p3uUf6wMDkz-val" name="entryfield" title="{} 35-39, Male" value="[ {} 35-39, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-WepGnPVeRZf-val" name="entryfield" title="{} 40-44, Male" value="[ {} 40-44, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-AweyRPXLuxm-val" name="entryfield" title="{} 45-49, Male" value="[ {} 45-49, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td name="total">&nbsp;</td>')
    f.writelines('</tr>')
    f.writelines('<tr>')
    f.writelines('<td><b>F</b></td>')
    f.writelines('<td><input id="{}-eMEfB41kz0A-val" name="entryfield" title="{} &lt;1, Female" value="[ {} &lt;1, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-FPwA7y28OoQ-val" name="entryfield" title="{} 1 - 4, Female" value="[ {} 1 - 4, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-Dw6BbW2VMd7-val" name="entryfield" title="{} 5-9, Female" value="[ {} 5-9, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-I6hMs4H6Y5z-val" name="entryfield" title="{} 10--14, Female" value="[ {} 10--14, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-H1eDstn4AfY-val" name="entryfield" title="{} 15-19, Female" value="[ {} 15-19, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-AhsOQTGdZjT-val" name="entryfield" title="{} 20-24, Female" value="[ {} 20-24, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-U45kuDppvvs-val" name="entryfield" title="{} 25-29, Female" value="[ {} 25-29, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-KAVKLmYeUBs-val" name="entryfield" title="{} 30-34, Female" value="[ {} 30-34, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-YmSyRRfzUAk-val" name="entryfield" title="{} 35-39, Female" value="[ {} 35-39, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-Hwjg5YyMGC1-val" name="entryfield" title="{} 40-44, Female" value="[ {} 40-44, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-MEov0DwDawU-val" name="entryfield" title="{} 45-49, Female" value="[ {} 45-49, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td name="total">&nbsp;</td>')
    f.writelines('</tr>')
def renderHTMLDSDNeutral(id,displayname,topic,f):
    f.writelines('<tr>')
    f.writelines('<td rowspan ="2">{}</td>'.format(topic))
    f.writelines('<td><b>M</b></td>')
    f.writelines('<td><input id="{}-fsJqYCPHP01-val" name="entryfield" title="{} &lt;1, Male" value="[ {} &lt;1, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-bMWhocghjsV-val" name="entryfield" title="{} 1-4, Male" value="[ {} 1-4, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-ShtKZwEQsyh-val" name="entryfield" title="{} 5-9, Male" value="[ {} 5-9, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-NRhTRlBac0Z-val" name="entryfield" title="{} 10-14, Male" value="[ {} 10-14, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-IlOmx8kSPmS-val" name="entryfield" title="{} 15-19, Male" value="[ {} 15-19, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-ISe2MFyjI32-val" name="entryfield" title="{} 20-24, Male" value="[ {} 20-24, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-Jx7modGCLvc-val" name="entryfield" title="{} 25-29, Male" value="[ {} 25-29, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-iNbYTZ2jOD4-val" name="entryfield" title="{} 30-34, Male" value="[ {} 30-34, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-hcpd67SnmC4-val" name="entryfield" title="{} 35-39, Male" value="[ {} 35-39, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-PECNsjUO2AA-val" name="entryfield" title="{} 40-44, Male" value="[ {} 40-44, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-SeK211OEnoR-val" name="entryfield" title="{} 45-49, Male" value="[ {} 45-49, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-hjyYNLb8xu9-val" name="entryfield" title="{} 50+, Male" value="[ {} 50+, Male ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td name="total">&nbsp;</td>')
    f.writelines('</tr>')
    f.writelines('<tr>')
    f.writelines('<td><b>F</b></td>')
    f.writelines('<td><input id="{}-DrUc2NoibWP-val" name="entryfield" title="{} &lt;1, Female" value="[ {} &lt;1, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-Oqqv8Nelgjo-val" name="entryfield" title="{} 1 - 4, Female" value="[ {} 1 - 4, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-kqzprBeJZfA-val" name="entryfield" title="{} 5-9, Female" value="[ {} 5-9, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-CxNTFv5NyIK-val" name="entryfield" title="{} 10--14, Female" value="[ {} 10--14, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-FZdJE52H3FO-val" name="entryfield" title="{} 15-19, Female" value="[ {} 15-19, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-fiogdqQP6Nv-val" name="entryfield" title="{} 20-24, Female" value="[ {} 20-24, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-D9UCQp2Pd1g-val" name="entryfield" title="{} 25-29, Female" value="[ {} 25-29, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-wdkUN4BqPOR-val" name="entryfield" title="{} 30-34, Female" value="[ {} 30-34, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-TYnBvlllX0i-val" name="entryfield" title="{} 35-39, Female" value="[ {} 35-39, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-noCqd8II0uO-val" name="entryfield" title="{} 40-44, Female" value="[ {} 40-44, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-BAp27lWm8sW-val" name="entryfield" title="{} 45-49, Female" value="[ {} 45-49, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td><input id="{}-LdRASGjnopF-val" name="entryfield" title="{} 50+, Female" value="[ {} 50+, Female ]" /></td>'.format(id,displayname,topic))
    f.writelines('<td name="total">&nbsp;</td>')
    f.writelines('</tr>')
def renderPMTCT(id,original,display,f):
    f.writelines('<tr>')
    f.writelines('<td rowspan="5">{}</td>'.format(display))
    f.writelines('<td>TBA rt-HCW</td>')
    f.writelines('<td><input id="{}-fXyOCqjKb30-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('fXyOCqjKb30',original),resolve('fXyOCqjKb30',original)))
    f.writelines('<td><input id="{}-GwsyuxnG8mf-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('GwsyuxnG8mf',original),resolve('GwsyuxnG8mf',original)))
    f.writelines('<td><input id="{}-vNRhs5QULNJ-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('vNRhs5QULNJ',original),resolve('vNRhs5QULNJ',original)))
    f.writelines('<td><input id="{}-ldxUw70Hv9e-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('ldxUw70Hv9e',original),resolve('ldxUw70Hv9e',original)))
    f.writelines('<td><input id="{}-x4fieq3reZk-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('x4fieq3reZk',original),resolve('x4fieq3reZk',original)))
    f.writelines('<td><input id="{}-jX9v4wO6SRQ-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('jX9v4wO6SRQ',original),resolve('jX9v4wO6SRQ',original)))
    f.writelines('<td><input id="{}-vBWcgyf9YOR-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('vBWcgyf9YOR',original),resolve('vBWcgyf9YOR',original)))
    f.writelines('<td><input id="{}-iZhr3woSrRa-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('iZhr3woSrRa',original),resolve('iZhr3woSrRa',original)))
    f.writelines('<td><input id="{}-z0Sunv0ljmB-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('z0Sunv0ljmB',original),resolve('z0Sunv0ljmB',original)))
    f.writelines('<td><input id="{}-z1feg5GPbcj-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('z1feg5GPbcj',original),resolve('z1feg5GPbcj',original)))
    f.writelines('<td name = "total"></td></tr>')
        
    f.writelines('<tr>')
    f.writelines('<td>TBA Orthodox</td>')
    f.writelines('<td><input id="{}-NFtKWPKiIJD-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('NFtKWPKiIJD',original),resolve('NFtKWPKiIJD',original)))
    f.writelines('<td><input id="{}-clOiLmZ8nyv-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('clOiLmZ8nyv',original),resolve('clOiLmZ8nyv',original)))
    f.writelines('<td><input id="{}-CXxat0a5X3E-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('CXxat0a5X3E',original),resolve('CXxat0a5X3E',original)))
    f.writelines('<td><input id="{}-pFAmfwRo5Wu-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('pFAmfwRo5Wu',original),resolve('pFAmfwRo5Wu',original)))
    f.writelines('<td><input id="{}-WHPDNqgtA0f-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('WHPDNqgtA0f',original),resolve('WHPDNqgtA0f',original)))
    f.writelines('<td><input id="{}-VK0aoNBU5NG-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('VK0aoNBU5NG',original),resolve('VK0aoNBU5NG',original)))
    f.writelines('<td><input id="{}-j4pRrqDTHof-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('j4pRrqDTHof',original),resolve('j4pRrqDTHof',original)))
    f.writelines('<td><input id="{}-T0M6SVikMUW-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('T0M6SVikMUW',original),resolve('T0M6SVikMUW',original)))
    f.writelines('<td><input id="{}-Wx8wf1wlv7Y-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('Wx8wf1wlv7Y',original),resolve('Wx8wf1wlv7Y',original)))
    f.writelines('<td><input id="{}-jp8aH6bgB3Z-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('jp8aH6bgB3Z',original),resolve('jp8aH6bgB3Z',original)))
    f.writelines('<td name = "total"></td></tr>')
        
    f.writelines('<tr>')
    f.writelines('<td>Congregational setting (CAP)</td>')
    f.writelines('<td><input id="{}-HCmzHRYQTaO-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('HCmzHRYQTaO',original),resolve('HCmzHRYQTaO',original)))
    f.writelines('<td><input id="{}-oDMUJqF887A-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('oDMUJqF887A',original),resolve('oDMUJqF887A',original)))
    f.writelines('<td><input id="{}-n3gVQenSdL5-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('n3gVQenSdL5',original),resolve('n3gVQenSdL5',original)))
    f.writelines('<td><input id="{}-YPJNn5GikGa-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('YPJNn5GikGa',original),resolve('YPJNn5GikGa',original)))
    f.writelines('<td><input id="{}-AJzwRS9fcnC-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('AJzwRS9fcnC',original),resolve('AJzwRS9fcnC',original)))
    f.writelines('<td><input id="{}-iVKzsJ6UJwG-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('iVKzsJ6UJwG',original),resolve('iVKzsJ6UJwG',original)))
    f.writelines('<td><input id="{}-CeKuKDFSFaS-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('CeKuKDFSFaS',original),resolve('CeKuKDFSFaS',original)))
    f.writelines('<td><input id="{}-C3hJ8ETzLpT-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('C3hJ8ETzLpT',original),resolve('C3hJ8ETzLpT',original)))
    f.writelines('<td><input id="{}-tmJJaP0BpUB-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('tmJJaP0BpUB',original),resolve('tmJJaP0BpUB',original)))
    f.writelines('<td><input id="{}-HCmzHRYQTaO-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('HCmzHRYQTaO',original),resolve('HCmzHRYQTaO',original)))
    f.writelines('<td name = "total"></td></tr>')
        
    f.writelines('<tr>')
    f.writelines('<td>Community (Delivery Home)</td>')
    f.writelines('<td><input id="{}-krMNJdjsO8J-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('krMNJdjsO8J',original),resolve('krMNJdjsO8J',original)))
    f.writelines('<td><input id="{}-vsLE1iEFn8F-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('vsLE1iEFn8F',original),resolve('vsLE1iEFn8F',original)))
    f.writelines('<td><input id="{}-hKpKSIfwpFC-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('hKpKSIfwpFC',original),resolve('hKpKSIfwpFC',original)))
    f.writelines('<td><input id="{}-pNLGH4nMwyL-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('pNLGH4nMwyL',original),resolve('pNLGH4nMwyL',original)))
    f.writelines('<td><input id="{}-lkBZtGFXVC8-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('lkBZtGFXVC8',original),resolve('lkBZtGFXVC8',original)))
    f.writelines('<td><input id="{}-eiG0WQG0p9y-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('eiG0WQG0p9y',original),resolve('eiG0WQG0p9y',original)))
    f.writelines('<td><input id="{}-arodXL4Fi7c-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('arodXL4Fi7c',original),resolve('arodXL4Fi7c',original)))
    f.writelines('<td><input id="{}-vQTKA37x4iI-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('vQTKA37x4iI',original),resolve('vQTKA37x4iI',original)))
    f.writelines('<td><input id="{}-g5Abe3Smqhw-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('g5Abe3Smqhw',original),resolve('g5Abe3Smqhw',original)))
    f.writelines('<td><input id="{}-lFNN0cPKLNZ-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('lFNN0cPKLNZ',original),resolve('lFNN0cPKLNZ',original)))
    f.writelines('<td name = "total"></td></tr>')
        
    f.writelines('<tr>')
    f.writelines('<td>Community(s-HF)</td>')
    f.writelines('<td><input id="{}-ZR8exxgvgkt-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('ZR8exxgvgkt',original),resolve('ZR8exxgvgkt',original)))
    f.writelines('<td><input id="{}-cnGoBgOQQPF-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('cnGoBgOQQPF',original),resolve('cnGoBgOQQPF',original)))
    f.writelines('<td><input id="{}-xACjMfyPJh4-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('xACjMfyPJh4',original),resolve('xACjMfyPJh4',original)))
    f.writelines('<td><input id="{}-eKDsvQH2cBB-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('eKDsvQH2cBB',original),resolve('eKDsvQH2cBB',original)))
    f.writelines('<td><input id="{}-dVoKbUbWQ9D-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('dVoKbUbWQ9D',original),resolve('dVoKbUbWQ9D',original)))
    f.writelines('<td><input id="{}-Lj7mFte9Nnd-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('Lj7mFte9Nnd',original),resolve('Lj7mFte9Nnd',original)))
    f.writelines('<td><input id="{}-tF6XVdOiy0O-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('tF6XVdOiy0O',original),resolve('tF6XVdOiy0O',original)))
    f.writelines('<td><input id="{}-dhKbrYEEp9f-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('dhKbrYEEp9f',original),resolve('dhKbrYEEp9f',original)))
    f.writelines('<td><input id="{}-PXkJwyOBPys-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('PXkJwyOBPys',original),resolve('PXkJwyOBPys',original)))
    f.writelines('<td><input id="{}-ANPREvfiFiL-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,resolve('ANPREvfiFiL',original),resolve('ANPREvfiFiL',original)))
    f.writelines('<td name = "total"></td></tr>')
    
    
    
def resolve(id,name):
    #val = df['name'].to_numpy()[df['id'].to_numpy() == id].item()
    global dictr
    #print(dictr['id'])
    for index,value in dictr['id'].items():
        if value == id:
            return '{} {}'.format(name,dictr['name'][index])
            
    """for index,row in df.iterrows():
        if row['id'].strip() == id:"""
    #return '{} {}'.format(name,val)
    

    
    
    

if __name__ == '__main__':
    main()