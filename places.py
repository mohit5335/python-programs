import json
import requests
api_key="  "   #enter API key 
url="https://maps.googleapis.com/maps/api/place/textsearch/json?"
image="https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference="
name=input("Enter name of the place\n")        #name of place you want to search
page=requests.get(url+'query='+name+'&key='+api_key)
data=page.json()
search=data['results']
for i in range(len(search)):
    print(i+1,'\t',search[i]['name'])
no=int(input("enter your choice "))
print("Name:\t"+data['results'][no-1]['name']+"\n\tAddress:"+data['results'][no-1]['formatted_address']+"\n\tRating:",data['results'][no-1]['rating'])
photo=requests.get(image+search[no-1]["photos"][0]['photo_reference']+'&key='+api_key)
f  = open('temp.jpeg','wb')
f.write(photo.content)
f.close()
import matplotlib.pyplot as plt
with open('temp.jpeg','rb') as fp :
    img = plt.imread(fp)
    fp.close()
plt.imshow(img)
plt.show()