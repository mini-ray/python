lat = input("Enter lats: ")
lon = input("Enter lons: ")

lat_list = [float(s) for s in lat.split(',')]
lon_list = [float(s) for s in lon.split(',')]

print("Farthest north = " + str(max(lat_list))) 
print("Farthest west = " + str(max(lon_list)))
print("Farthest south = " + str(min(lat_list)))
print("Farthest east = " + str(min(lon_list)))
