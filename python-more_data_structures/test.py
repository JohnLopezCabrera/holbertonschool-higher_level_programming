capitals = {"USA": "Washington D.C.", "India": "New Delhi", "China": "Beijing", "Russia": "Moscow"}

#print(dir(capitals))
#print()
#print(capitals.get("japan"))
#if capitals.get("japan"):
  #  print("that capital exists")
#else:
 #   print("that capital doesn't exist")

#capitals.update({"Germany": "Berlin"})
#capitals.update({"USA": "Detroit"})
#capitals.pop("China")
#capitals.popitem()

#keys = capitals.keys()

#for key in capitals.keys():
#alues = capitals.values()
#for value in capitals.values():
items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")