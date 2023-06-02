import matplotlib .pyplot as plt
import psutil as p

list_appname = {}


count = 0

for process in p.process_iter():
    count = count+1
    if count<=6:
        name = process.name()
        cpu_usage = p.cpu_percent()
        
        print("Name: ",name," --- CPU Usage: ",cpu_usage)
        list_appname.update({name:cpu_usage})
        
keymax=max(list_appname,key=list_appname.get)
print(keymax)
keymin=min(list_appname,key=list_appname.get)
print(keymin)

name = [keymax,keymin]

print(name)

app = list_appname.values()
max_app = max(app)

print("Maximum: ",max_app)

min_app = min(app)

print("Minimum: ",min_app)

max_min_list = [max_app,min_app]
print(max_min_list)
    
plt.figure(figsize=(15,7))
plt.xlabel("Min Max CPU Consumption")
plt.ylabel("CPU Usage")
    
plt.bar(name,max_min_list,width=0.6,color=("red","yellow"))
plt.show()