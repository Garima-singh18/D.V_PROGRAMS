import matplotlib.pyplot as plt
x = [20,45,70,83]
y = ["Red tape","campus","Liberty","Killer"]
ex = [0.0,0.0,0.0,0.0]
plt.pie(x,labels=y,autopct="%0.1f%%",explode=ex,shadow=1)
plt.legend(loc=2)
plt.show()