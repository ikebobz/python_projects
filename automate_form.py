# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 00:47:43 2024

@author: HI LEAD
"""
import pandas as pd
import numpy as np

disag1 = ['Male','Female']
#disag1 = ['TLD (Tenofovir+Lamivudine+Dolutegravir)','TLD (Tenofovir+Lamivudine+Efavirenz) -300/300/400','ABC/3TC/DTG (Abacavir+Lamivudine+Dolutegravir) 120/60mg/10mg']
#disag2 = ['<1','1 - 4','5-9','10--14','15-19','20-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65+']
#disag2 = ['<1 Month','1 Month','2 Months','3 Months','4 Months','5 Months','6 Months']
#disag2 = ['&lt;1','1 - 4','5-9','10--14','15-19','20-24','25-29','30-34','35-39','40-44','45-49','50+']
disag2 = ['<=72hrs','>72hrs - <2months','2-12 Months']
#disag2 = ['<15','>=15']
#disag2 = ['<10','10--14','15-19','20-24','25-29','30-34','35-39','40-44','45-49','50+']
disag3 = ['TBA rt-HCW','TBA Orthodox','Congregational setting','Delivery Homes (DH)','Spoke Health facilities  (s-HF)']
#disag3 = ['Negative Result','Positive Result','Known Positive Result','Known Negative Result','Already on ART at Time of Visit','Unknown HIV Status at time of visit','Unknown HIV Status and tested for HIV']
#disag3 = ['Spouse','Self','Sexual Partner','Social Network','Other','Caregiver for Child','Children']
#disag3 = ['First time testers','Retesters']
#disag3 = ['Post ANC 1 (Breastfeeding)','Post ANC 1 (Pregnant/L&D)']
#disag3 = ['Injectables','Oral','Other PrEP Type']
#disag3 = ['Chronic Care Checklist','Chest X-Ray','AHD Classification']
#disag3 = ['Genexpert','Chest X-Ray','XMAP','Urine LF LAM','Truenat','Sputum TB LAMP','Others']
#disag3 = ['DSTB','DRTB']
#disag3 = ['6H','3HP','1HP','3HR']
#disag3 = ['PrEP','Other']
#disag3 = ['Reactive','Non-Reactive','Indeterminate']
#disag3 = ['VL suppressed','Clients Return To Treatment','Others']
#disag3 = ['Children Enumerated','Partners Elicited']
#disag3 = ['Passive Notification/Self','Provider Assisted','Contracted','Dual Approach']
#disag3 = ['Paedriatic Sevices','Malnutrition Clinic','Blood Bank']
#disag3 = ['OVC','Spoke Site','VCT']


srcframe = pd.read_excel("Updated DMEL-reviewed.xlsx",sheet_name = 'AP3',usecols=['Data Element Name'])
refframe_de = pd.read_excel("data_elements_new.xlsx",sheet_name = 'data_elements_new')
refframe_catcom = pd.read_excel("category_combinations.xlsx",sheet_name = 'category_combinations')

def rendertags2D():
    f = open('source2.html','a')
    global disag1, disag2, disag3, srcframe, refframe
    rowspan = len(disag1)
    f.writelines('<tbody>')
    for index,row in srcframe.iterrows():
        print('Writing New Data Element................')
        name = row['Data Element Name']
        id = lookupde(name)
        
        f.writelines('<tr><td rowspan = {}>{}</td>'.format(rowspan,name))
        for sex in disag1:
          if sex == 'Female':
           f.writelines('<tr><td><b>{}</b></td>'.format(sex[0]))
          else:
            f.writelines('<td><b>{}</b></td>'.format(sex[0]))
          for i in range(0,len(disag2)):
             catopcmb = '{}, {}'.format(disag2[i],sex)
             catopcmbid = lookupde(catopcmb,type='cat')
             #tit = 'HFR1_{} {}'.format(name,catopcmb)
             tit = 'ART_ADD_{} {}'.format(name,catopcmb)
             f.writelines('<td><input id="{}-{}-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,catopcmbid,tit,tit))
          f.writelines('<td name = "total"></td></tr>')
    f.writelines('</tbody>')
def rendertags2DNoSex():
    f = open('source2.html','a')
    global disag1, disag2, disag3, srcframe, refframe
    rowspan = len(disag1)
    f.writelines('<tbody>')
    for index,row in srcframe.iterrows():
        print('Writing New Data Element................')
        name = row['Data Element Name']
        id = lookupde(name)
        
        f.writelines('<tr><td rowspan = {}>{}</td>'.format(rowspan,name))
        for type in disag1:
          if type != disag1[0]:
           f.writelines('<tr><td><b>{}</b></td>'.format(type))
          else:
            f.writelines('<td><b>{}</b></td>'.format(type))
          for i in range(0,len(disag2)):
             catopcmb = '{}, {}'.format(disag2[i],type)
             catopcmbid = lookupde(catopcmb,type='cat')
             #tit = 'HFR1_{} {}'.format(name,catopcmb)
             tit = 'ART_ADD_{} {}'.format(name,catopcmb)
             f.writelines('<td><input id="{}-{}-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,catopcmbid,tit,tit))
          f.writelines('<td name = "total"></td></tr>')
    f.writelines('</tbody>')
def rendertags3D():
    f = open('source2.html','a')
    global disag1, disag2, disag3, srcframe, refframe
    outerspan = len(disag1)*len(disag3)
    innerspan = len(disag1)
    print('writing rows......................')
    f.writelines('<tbody>')
    for index,row in srcframe.iterrows():
        print('Writing New Data Element................')
        name = row['Data Element Name']
        id = lookupde(name)
        f.writelines('<tr><td rowspan = {}>{}</td>'.format(outerspan,name))
        for opt in disag3:
            if opt == disag3[0]:
             f.writelines('<td rowspan = {}>{}</td>'.format(innerspan,opt))
            else:
             f.writelines('<tr><td rowspan = {}>{}</td>'.format(innerspan,opt)) 
            for sex in disag1:
                if sex == 'Female':
                 f.writelines('<tr><td><b>{}</b></td>'.format(sex[0]))
                else:
                  f.writelines('<td><b>{}</b></td>'.format(sex[0]))
                for i in range(0,len(disag2)):
                    catopcmb = '{}, {}, {}'.format(opt,sex,disag2[i])
                    catopcmb1 = '{}, {}, {}'.format(disag2[i],opt,sex)
                    catopcmid = lookupde(catopcmb,type = 'cat')
                    if catopcmid == None:
                        catopcmid = lookupde(catopcmb1,type = 'cat')
                    tit = 'htsadd_{} {}'.format(name,catopcmb)
                    #tit = '{} {}'.format(name,catopcmb)
                    if catopcmid == None:
                        f.writelines('<td></td>')
                    else:
                        f.writelines('<td><input id="{}-{}-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,catopcmid,tit,tit))
                f.writelines('<td name = "total"></td></tr>')
    f.writelines('</tbody>')
def rendertags2DF():
    f = open('source2.html','a')
    global disag1, disag2, disag3, srcframe, refframe
    rowspan = len(disag3)
    f.writelines('<table><tbody>')
    for index,row in srcframe.iterrows():
        print('Writing New Data Element................')
        name = row['Data Element Name']
        id = lookupde(name)
        f.writelines('<tr><td rowspan = {}>{}</td>'.format(rowspan,stripOfPrefix(name)))
        for type in disag3:
          if type == disag3[0]:
            f.writelines('<td><b>{}</b></td>'.format(type))
          else:
            f.writelines('<tr><td><b>{}</b></td>'.format(type))
          for i in range(0,len(disag2)):
             catopcmb = '{}, {}'.format(type,disag2[i])
             catopcmbid = lookupde(catopcmb,type='cat')
             #tit = 'PMTCT_Add_{} {}'.format(name,catopcmb)
             tit = '{} {}'.format(name,catopcmb)
             f.writelines('<td><input id="{}-{}-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,catopcmbid,tit,tit))
          f.writelines('<td name = "total"></td></tr>')
    f.writelines('</tbody></table>')
def rendertags1DF():
    f = open('source2.html','a')
    global disag1, disag2, disag3, srcframe, refframe
    f.writelines('<tbody>')
    for index,row in srcframe.iterrows():
        print('Writing New Data Element................')
        name = row['Data Element Name']
        id = lookupde(name)
        f.writelines('<tr><td>{}</td><td></td>'.format(stripOfPrefix(name)))
        for i in range(0,len(disag2)):
           catopcmb = '{}'.format(disag2[i])
           catopcmbid = lookupde(catopcmb,type='cat')
           tit = '{} {}'.format(name,catopcmb)
           f.writelines('<td><input id="{}-{}-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,catopcmbid,tit,tit))
        f.writelines('<td name = "total"></td></tr>')
    f.writelines('</tbody>')
    
     
    

    
def lookupde(e,type = 'de'):
    #print(e)
    global refframe_de,refframe_catcom
    if type == 'de':
        for i,r in refframe_de.iterrows():
            #print(r['DataElementName'])
            if r['DataElementName'].strip().replace('HFR1_','').replace('PMTCT_Add_','').replace('ART_ADD_','').replace('Indexadd_','')== e.strip():
                return r['ID']
    elif type == 'cat':
        for i,r in refframe_catcom.iterrows():
            if r['name'].strip().lower() == e.strip().lower():
                return r['id']
            
def stripOfPrefix(string):
    return string.strip().replace('HFR1_','').replace('PMTCT_Add_','').replace('ART_ADD_','').replace('Indexadd_','').replace('htsadd_','').replace('PWSF_','')
def removeHtmlDecor(value):
    return value.replace('&lt;','<')


def main():
    rendertags1DF()
    

if __name__ == '__main__':
    main()