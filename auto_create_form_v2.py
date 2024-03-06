import pandas as pd

agedsg = ['&lt;1','1 - 4','5-9','10--14','15-19','20-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65+']
dsg1 = ['Out patient','Community','Total']
dsg2 = ['Paedriatic Sevices','Malnutrition Clinic','Blood Bank']
dsg3 = ['OVC','Spoke Site','VCT']
sxdsg = ['Male','Female']
elements = ['ele1','ele2','ele3']
dimensions = '3'
srcframe = pd.read_excel("Updated DMEL-reviewed.xlsx",sheet_name = 'AP3',usecols=['Data Element Name'])
refframe_de = pd.read_excel("data_elements_new.xlsx",sheet_name = 'data_elements_new')
refframe_catcom = pd.read_excel("category_combinations.xlsx",sheet_name = 'category_combinations')
f = open('source2.html','a')

def insert_header():
    global agedsg,dsg1,dsg2,dsg3,sxdsg,elements,dimensions,f
    f.writelines('<tr><th class="header-label" rowspan="{}">Data Element Name</th class="header-label">'.format(dimensions))
    f.writelines('<th class="header-label" rowspan="{}">Age Groups(years)</th class="header-label">'.format(dimensions))
    for val in dsg1:
        if val == dsg1[len(dsg1)-1]:
            f.writelines('<th class="header-label" rowspan="2" colspan = "{}" style ="text-align:center">{}</th class="header-label">'.format(len(sxdsg),val))
        else:
            f.writelines('<th class="header-label" colspan="{}" style = "text-align:center">{}</th class="header-label">'.format(len(sxdsg)*len(dsg3),val))
    f.writelines('</tr>')
    f.writelines('<tr>')
    for val in dsg2:
        f.writelines('<th class="header-label" colspan = "{}">{}</th class="header-label">'.format(len(sxdsg),val))
    for val in dsg3:
        f.writelines('<th class="header-label" colspan = "{}">{}</th class="header-label">'.format(len(sxdsg),val))
    f.writelines('</tr>')
    f.writelines('<tr>')
    for val in dsg2:
        f.writelines('<th class="header-label">{}</th class="header-label">'.format(sxdsg[0]))
        f.writelines('<th class="header-label">{}</th class="header-label">'.format(sxdsg[1]))
    for val in dsg3:
        f.writelines('<th class="header-label">{}</th class="header-label">'.format(sxdsg[0]))
        f.writelines('<th class="header-label">{}</th class="header-label">'.format(sxdsg[1]))
    for val in sxdsg:
        f.writelines('<th class="header-label">{}</th class="header-label">'.format(val))
        #f.writelines('<th>{}</th>'.format(sxdsg[1]))
        
    f.writelines('</tr>')

def insert_body():
    #f = open('source2.html','a')
    global agedsg,dsg1,dsg2,dsg3,sxdsg,elements,dimensions, f
    #for element in elements:
    for index,row in srcframe.iterrows():
        print('Writing New Data Element................')
        element = row['Data Element Name']
        id = lookupde(element)
        f.writelines('<tr ><td rowspan = "{}">{}</td>'.format(len(agedsg),stripOfPrefix(element)))
        for band in agedsg:
            if band == agedsg[0]:
                f.writelines('<td>{}</td>'.format(band))
                for type in dsg2:
                    for sex in sxdsg:
                        catopcmb = '{}, {}, {}'.format(type,sex,removeHtmlDecor(band))
                        catopcmid = lookupde(catopcmb,type = 'cat')
                        tit = '{} {}'.format(element,catopcmb)
                        f.writelines('<td><input id="{}-{}-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,catopcmid,tit,tit))
                        #f.writelines('<td></td>')
                for type in dsg3:
                    for sex in sxdsg:
                        catopcmb = '{}, {}, {}'.format(type,sex,removeHtmlDecor(band))
                        catopcmid = lookupde(catopcmb,type = 'cat')
                        tit = '{} {}'.format(element,catopcmb)
                        #f.writelines('<td></td>')
                        f.writelines('<td><input id="{}-{}-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,catopcmid,tit,tit))
                f.writelines('<td></td><td></td></tr>')
            else:
                f.writelines('<tr><td>{}</td>'.format(band))
                for type in dsg2:
                    for sex in sxdsg:
                        catopcmb = '{}, {}, {}'.format(type,sex,removeHtmlDecor(band))
                        catopcmid = lookupde(catopcmb,type = 'cat')
                        tit = '{} {}'.format(element,catopcmb)
                        #f.writelines('<td></td>')
                        f.writelines('<td><input id="{}-{}-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,catopcmid,tit,tit))
                for type in dsg3:
                    for sex in sxdsg:
                        catopcmb = '{}, {}, {}'.format(type,sex,removeHtmlDecor(band))
                        catopcmid = lookupde(catopcmb,type = 'cat')
                        tit = '{} {}'.format(element,catopcmb)
                        #f.writelines('<td></td>')
                        f.writelines('<td><input id="{}-{}-val" name="entryfield" title="{}" value = "[ {} ]"></td>'.format(id,catopcmid,tit,tit))
                f.writelines('<td></td><td></td></tr>')
        
    
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
    return string.strip().replace('HFR1_','').replace('PMTCT_Add_','').replace('ART_ADD_','').replace('Indexadd_','').replace('htsadd_','')
def removeHtmlDecor(value):
    return value.replace('&lt;','<')


def main():
    f.writelines('<table class = "table">')
    f.writelines('<thead>')
    insert_header()
    f.writelines('</thead>')
    insert_body()
    f.writelines('</table>')
    f.close()
    

if __name__ == '__main__':
    main()



    
        