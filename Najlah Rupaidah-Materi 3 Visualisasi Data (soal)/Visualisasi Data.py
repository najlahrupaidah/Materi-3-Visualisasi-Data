import numpy as np 
import matplotlib.pyplot as plt 
 
h0 = 50 
g = 9.8 
v0 = 0
x0,y0 = 0,0 

t_fall = np.sqrt(2 * h0 / g)
print("Waktu yang diperlukan untuk mencapai tanah = ", t_fall, " s")
t = np.arange(0.0, t_fall, 10**(-3))

v_t = g * t
print("\nKecepatan benda saat mencapai tanah (v(t) akhir) =", v_t[-1], "m/s")
h_t = h0 - 0.5 * g * t**2
print("Posisi benda saat mencapai tanah (h(t) akhir) =", h_t[-1], "m")
 
fig, ax1 = plt.subplots()
ax1.plot(t, v_t)
ax1.set(xlabel='t (s)', ylabel='v(t) (m/s)', title='Grafik Kecepatan Benda sebagai Fungsi Waktu')
ax1.grid()
plt.show()

fig, ax2 = plt.subplots()
ax2.plot(t, h_t)
ax2.set(xlabel='t (s)', ylabel='h(t) (m)', title='Grafik Posisi Benda sebagai Fungsi Waktu')
ax2.grid()
plt.show()
