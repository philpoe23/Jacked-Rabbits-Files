#Metadata (.json) File Generator

#Imports
import json
  
#Metadata
Metadata ={
  "name": "Jacked Rabbits Membership Card #1",
  "symbol": "DIMD",
  "seller_fee_basis_points": 500,
  "description": "Diamond Rarity",
  "image": "0.png",
  "animation_url": "0.mp4",
  "attributes": [
    {
      "trait_type": "Diamond",
      "value": "1"
    }
  ],
  
  "collection": {
    "name": "Jacked Rabbits Gym Club",
    "family": "Jacked Rabbits Gym Club"
  },
  "properties": {
    "files": [
      {
        "uri": "0.png",
        "type": "image/png"
      },
      {
        "uri": "0.mp4",
        "type": "video/mp4"
      }
    ],
    "category": "video",
    "creators": [
      {
        "address": "2sr3JuiYmKEWyjEaouKwuHPtGmUvyYDaAaSJ13gNhGGK",
        "share": 100
      }
    ]
  }
}


#Code
for i in range(1,1501):
    Metadata.update({"name": "Jacked Rabbit Membership Card #" + str(i)})
    Metadata.update({"image": str(i-1)+".png"})
    Metadata.update({"animation_url": str(i-1)+".mp4"})
    Metadata.update({'properties' : {'files': [{'uri': str(i-1)+'.png', 'type': 'image/png'}, {'uri': str(i-1)+'.mp4', 'type': 'video/mp4'}], 'category': 'video', 'creators': [{'address': '2sr3JuiYmKEWyjEaouKwuHPtGmUvyYDaAaSJ13gNhGGK', 'share': 100}]}})
    json_object = json.dumps(Metadata, indent = 4)
    with open(str(i-1)+".json", "w") as outfile:
        outfile.write(json_object)

print("Done")

