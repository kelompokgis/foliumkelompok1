import folium

m = folium.map(
  location =[-7.9786395,112.5617421]'
  zoom_start = 12,
)

folium.Marker(
  location =[-7.976854,112.6307393],
  popup='Kahuripan',
  icon = folium.Icon (icon='info-sign')
).add_to(m
         
folium.Marker(
  location =[-7.977109, 112.631426],
  popup='Brawijaya',
  icon = folium.Icon (icon='info-sign')
).add_to(m)

folium.Marker(
  location =[-7.974825, 112.632595],
  popup='Belakang RSU',
  icon = folium.Icon (icon='info-sign')
).add_to(m)
 
 folium.Marker(
  location =[-7.974846, 112.634387],
  popup='Suropati',
  icon = folium.Icon (icon='info-sign')
).add_to(m)
         
 folium.Marker(
  location =[-7.970394,112.6320173],
  popup='Doktor Sutomo',
  icon = folium.Icon (icon='info-sign')
).add_to(m)
         
 folium.Marker(
  location =[-7.974155, 112.636662],
  popup='Trunojoyo',
  icon = folium.Icon (icon='info-sign')
).add_to(m)
         
 folium.Marker(
  location =[-7.971839,112.6332613],
  popup='Husni Tamrin',
  icon = folium.Icon (icon='info-sign')
).add_to(m)
         
  folium.Marker(
  location =[-7.97101,112.6302143],
  popup='Patimura',
  icon = folium.Icon (icon='info-sign')
).add_to(m)
         
 folium.Marker(
  location =[-7.970681,112.6336903],
  popup='Kartini',
  icon = folium.Icon (icon='info-sign')
).add_to(m)
         
 folium.Marker(
  location =[-7.968588,112.6340983],
  popup='Dokter Wahidin',
  icon = folium.Icon (icon='info-sign')
).add_to(m) 

m.save('index.html')
