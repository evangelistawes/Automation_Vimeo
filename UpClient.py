#Video Compresser and Uploader for Vimeo API
#Wesley Evangelista
#10.10.22
#v.: 1.0


from ast import Break, Continue
from compressor import compressor
from compressor import name_video
import vimeo
import json
from os import path




client = vimeo.VimeoClient(
    token= '466f3f4a6f1f365337e6b1f726bced5e',
    key='a9f8984a831d1dd56f76a95276f89dd93d8c81dc',
    secret='o0t6wz5saAxy8spF6kX3eY6x5ImWg+HC0CCc7HAYZpu44j3lkHBSdbubIwCWFM1hRQ1WUA02igzEnMMTBTv+8LsB9ki+0TmjGDVf9sUwrzzI/rSIQuRkPg/Y956xKo7I'
)


url = 'https://api.vimeo.com/me/videos'

response = client.get('https://api.vimeo.com/videos/611934332?fields=transcode.status').json()

print(response)

r = client.get(url)
caminho = 'C:\\xampp\\htdocs\\API_Vimeo'



if r.status_code == 200:
    print("Conectado ao Vimeo com sucesso")
    Continue
else:
    print("Error")
    exit


clip = 'test.mp4'
clip = compressor(clip)

print('Uploading: %s' % name_video)

caminho_video = path.join(caminho, name_video)
print(caminho_video)



try:  

    uri = client.upload(caminho_video, data = {'name': name_video, 'description' : 'Modelo de teste'})
    print(uri)

except vimeo.exceptions.VideoUploadFailure as e:

    print('Error')


