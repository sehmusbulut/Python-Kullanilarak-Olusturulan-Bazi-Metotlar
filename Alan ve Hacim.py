   
  # Sırasıyla ( koni, silindir ve küre) hacim ve alan hesaplamalarını yapan fonksiyonlar
   
   import math
   
   #-Koni---------------------
   
#Hacim Fonksiyonu
def cone_volume(r, h):
  return math.pi * r**2 * h / 3
  
#Alan Fonksiyonu
def cone_surface_area(r, h):
  return math.pi * r * (r + math.sqrt(h**2 + r**2))

   #-Silindir-------------------
   
#Hacim Fonksiyonu
def cylinder_volume(r, h):
  return math.pi * r**2 * h
  
#Alan Fonksiyonu
def cylinder_surface_area(r, h):
  return 2 * math.pi * r * (r + h)

   #-Küre-------------------------
   
#Hacim Fonksiyonu
def sphere_volume(r):
  return 4/3 * math.pi * r**3
  
#Alan Fonksiyonu
def sphere_surface_area(r):
  return 4 * math.pi * r**2
