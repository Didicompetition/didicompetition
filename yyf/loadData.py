#encoding:utf-8
DATA_DATE = "2016-01-30"
DATA_PATH_ORDER="C:\\Users\\matter\Desktop\\season_1\\test_set_1\\order_data\\order_data_"+DATA_DATE+"_test"
DATA_PATH_DIST = "C:\\Users\\matter\Desktop\\season_1\\test_set_1\\cluster_map\\cluster_map"


DIC_DIST={}
show=[]
def loadDistData():
    f = open(DATA_PATH_DIST,'r')
    for l in f:
        tmp = l.split('\t')
        DIC_DIST[tmp[0]]=tmp[1][:-1]
    f.close()



def convertTime(t):
    if  DATA_DATE+' 07:00:00'<t<  DATA_DATE+' 08:31:00':
        return DATA_DATE+'-46'
    if  DATA_DATE+' 09:00:00'<t<  DATA_DATE+' 10:31:00':
        return DATA_DATE+'-58'
    if  DATA_DATE+' 11:00:00'<t<  DATA_DATE+' 12:31:00':
        return DATA_DATE+'-70'
    if  DATA_DATE+' 13:00:00'<t<  DATA_DATE+' 14:31:00':
        return DATA_DATE+'-82'
    if  DATA_DATE+' 15:00:00'<t<  DATA_DATE+' 16:31:00':
        return DATA_DATE+'-94'
    if  DATA_DATE+' 17:00:00'<t<  DATA_DATE+' 18:31:00':
        return DATA_DATE+'-106'
    if  DATA_DATE+' 19:00:00'<t<  DATA_DATE+' 20:31:00':
        return DATA_DATE+'-118'
    if  DATA_DATE+' 21:00:00'<t<  DATA_DATE+' 22:31:00':
        return DATA_DATE+'-130'
    if  DATA_DATE+' 23:00:00'<t<  DATA_DATE+' 24:31:00':
        return DATA_DATE+'-142'



def foo():
    loadDistData()
    f=open(DATA_PATH_ORDER,'r')
    # out=11
    for l in f:
        # out-=1
        tmp = l.split('\t')
        if tmp[1]=="NULL":
            _time = convertTime(tmp[6][:-1])
            if _time:
                show.append([DIC_DIST[tmp[3]],_time])
        # if out <0:break
    f.close()


foo()
output = {}
for i in show:
    if output.has_key("%s,%s"%(i[0],i[1])):
        output["%s,%s"%(i[0],i[1])]+=1
    else:
        output["%s,%s"%(i[0],i[1])]=1
content2write = []
for (k,v) in output.items():
    content2write.append("%s,%0.1f\n"%(k,(v/8.5)))
fw = open('output'+DATA_DATE+'.csv','a+')
# content2write = "".join(content2write)
fw.writelines( "".join(content2write))
fw.close()
