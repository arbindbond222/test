
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

url = "http://www.bom.gov.au/fwo/IDN60701/IDN60701.94598.json"
headers={'User-Agent':user_agent,}

request=urllib.request.Request(url,None,headers) #The assembled request
response = urllib.request.urlopen(request)
data = response.read()# The data u need
output= json.loads(data)
y=[output['observations']['data'][i]["press"] for i in range(30)]
maximum=max(y)
minimum=min(y)
wind=[output['observations']['data'][i]["wind_spd_kt"] for i in range(30)]
maximum_wind=max(wind)
min_wind=min(wind)
s1=sum(wind)
ab=s1/3
s=sum(y)
average =s/3
print("<h1>average pressure"+str(average)+"</h1>")
print("<h1>minimum pressure"+str(minimum)+"</h1>")
print("<h1>maximum pressure"+str(maximum)+"</h1>")
print("<h1>maximum wind"+str(maximum_wind)+"</h1>")
print("<h1>minimum wind"+str(min_wind)+"</h1>")
print("<h1>average wind"+str(ab)+"</h1>")