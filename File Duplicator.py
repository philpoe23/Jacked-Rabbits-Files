#mp4 Duplicator
 
#Imports
import shutil

for i in range(2190,2200):
    Source = "/Users/thoma/Desktop/Thomas/Solana-NFT/Generator/DiamondThumbnail.png"
    Destination = "/Users/thoma/Desktop/Thomas/Solana-NFT/Generator/NFTs/Thumbnails/"+str(i)+".png"
    Copy = shutil.copy(Source, Destination)
 
print("Done")
