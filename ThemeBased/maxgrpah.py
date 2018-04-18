import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
def bytespdatenum(fmt,encoding='utf-8'):
	strconverter=mdates.strpdate2num(fmt)
	def bytesconverter(b):
		s=b.decode(encoding)
		return strconverter(s)
	return bytesconverter
def convert(li):
        pi=[]
        for x in li:
                tes=x[0]+x[1]+x[2]
                if tes=='Jan':
                        tes='01'
                elif tes=='Feb':
                        tes='02'
                elif tes=='Mar':
                        tes='03'
                elif tes=='Apr':
                        tes='04'
                elif tes=='May':
                        tes='05'
                elif tes=='Jun':
                        tes='06'
                elif tes=='Jul':
                        tes='07'
                elif tes=='Aug':
                        tes='08'
                elif tes=='Sep':
                        tes='09'
                elif tes=='Oct':
                        tes='10'
                elif tes=='Nov':
                        tes='11'
                elif tes=='Dec':
                        tes='12'
                x=tes+x[3:]
                pi.append(x)
        return pi      
file1=open('BTC-profit.csv','r');
li=file1.readlines()
li=[x.split('\n')[0] for x in li ]
li=[(x.split(',')[0],x.split(',')[1]) for x in li]
date=[]
profit=[]
for x in li:
	date.append(x[0])
	profit.append(x[1])

profit=[int(x) for x in profit]
#profit=[-x for x in profit]
#date=convert(date)
date=np.loadtxt(date,unpack=True,converters={0:bytespdatenum('%Y%m%d')})
plt.plot_date(date,profit,'-',label='Price')
#plt.plot(date,profit)
plt.xlabel('Year')
plt.title('BTC-profit')
plt.show()
file1.close()









