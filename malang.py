import folium

m = folium.map(
  location =[-7.9786395,112.5617421]'
  zoom_start = 12,
)

folium.Marker(
  location =[-7.976854,112.6307393],
  popup='Kahuripan',
  icon = folium.Icon (icon='info-sign')
).add_to(m)

m.save('index.html')
