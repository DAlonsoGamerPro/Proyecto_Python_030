import matplotlib
import matplotlib.pyplot as plt
import numpy as np

decadencia = ["Minecraft","Bendy","YS","Lego Fornite","SlendyTubbies","Plants vz Zombies"]
y_pos = np.arange(len(decadencia))
popularidad_actual = [8,3,0,4,0,1]

plt.barh(y_pos, popularidad_actual, align = "center", alpha = 0.5)
plt.yticks(y_pos, decadencia)
plt.xlabel("Popularidad")
plt.title("Popularidad Actual de Juegos Viejos")

plt.show()