import psutil 
import matplotlib.pyplot as plt
import matplotlib.animation as anime
from matplotlib import style
import datetime


style.use('fivethirtyeight')
fig = plt.figure()

##for vertical stacked ploting

(ax1,ax2,ax3) = fig.subplots(3,sharey=False)

x = []
y = []
z = []
d = []

class Cpusage:
    def __init__(self):
        #self.last = psutil.cpu_percent(interval=0.5, percpu=True)
        pass

    def update():
        values = psutil.cpu_percent(interval=0.3,percpu=True)
        ylabel = 0
        for ele in range(0, len(values)):
            ylabel = (ylabel + values[ele])
            percentage=round(ylabel/len(values),2)
        return percentage
    def memory():
        me = psutil.virtual_memory()
        mem = me[2]
        return mem
    def disk():
        di=psutil.disk_usage('/')
        dis= di[3]
        return dis




def animate(i,x,y,z,d):
    percentag=Cpusage.update()
    memory=Cpusage.memory()
    disk=Cpusage.disk()
    

    x.append(datetime.datetime.now().strftime('%H:%M:%S'))
    y.append(percentag)
    z.append(memory)
    d.append(disk)

    x= x[-20:]
    y= y[-20:]
    z= z[-20:]
    d= d[-20:]
    
    ax1.clear()
    ax1.plot(x, y)
    ax1.set_ylabel('CPU % Percentage',fontsize=10)
    ax1.set_xticklabels([])
    ax1.set_title('CPU, RAM and Storage DISK Usage of the system',fontsize=20)


    ax2.clear()
    color = 'tab:red'
    ax2.set_ylabel('Memory % used', color=color,fontsize=12)
    ax2.set_xticklabels([])
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.plot(x,z,color=color)

    ax3.clear()
    color= 'tab:green'
    ax3.set_ylabel('Total disk % used', color=color,fontsize=12)
    ax3.plot(x,d,color=color)

    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    
  
    plt.xlabel('Time')
    
ani = anime.FuncAnimation(fig, animate,fargs=(x, y, z, d), interval=1000)

plt.show()  
