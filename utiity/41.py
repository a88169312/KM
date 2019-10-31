from urllib import request
from PIL import Image

url = 'https://instagram.ftpe8-2.fna.fbcdn.net/vp/9057917ae7d8db6b3bd1aea87cb7f783/5E3F7AAD/t51.2885-15/sh0.08/e35/c0.180.1440.1440a/s640x640/71696242_532847117261436_7701094884909329420_n.jpg?_nc_ht=instagram.ftpe8-2.fna.fbcdn.net&_nc_cat=100'



file1 = request.urlopen(url)
image1 = Image.open(file1)
image1.save('Images\\sample.jpg')



#saveImage(url,'Images\\sample.jpg')