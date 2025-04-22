Names =  {"Marvin": "Washington D.C.", "Charles": "Paris", "Marcus": "Berlin"}
# if Names.get("Charles"):
#     print("Marvin exists in Washington D.C.")
# else :
#     print("Seems like Marvin is in a different city")

# keys = Names.keys()

# for key in Names.keys():
#         print(key)

for key, value in Names.items():
    print(f"{key}: {value}")