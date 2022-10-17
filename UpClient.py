#Video Compresser and Uploader for Vimeo API
#Wesley Evangelista
#10.10.22
#v.: 1.0

from ast import Continue
from compressor import compressor
from compressor import name_video
import vimeo
from os import getenv
from os import path
from dotenv import load_dotenv

load_dotenv() 
API_TOKEN =getenv("API_TOKEN")
API_KEY = getenv("API_KEY")
API_SECRET = getenv("API_SECRET")

client = vimeo.VimeoClient(
    token= API_TOKEN,
    key=API_KEY,
    secret= API_SECRET
)


url = 'https://api.vimeo.com/me/videos'
caminho = 'C:\\xampp\\htdocs\\API_Vimeo'



r = client.get(url)


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


#start Uploading in Vimeo API
try:  

    uri = client.upload(caminho_video, data = {'name': name_video, 'description' : 'Modelo de teste'})
    
    #Get the Video ID on Vimeo
    print(uri)

except vimeo.exceptions.VideoUploadFailure as e:

    print('Error')


vimeo_url = 'https://api.vimeo.com'

uri = vimeo_url + uri

whitelist = uri +'/privacy/domains/medway.com.br'

client.put(whitelist)

list_allowed = uri + '/privacy/domains'
print(client.get(list_allowed).json())

#Privacy.set_embed(uri)
#set the privacy configuration
client.patch(uri, data={'privacy': {'view': 'nobody'}})

#Set the  embed configuration
#Privacy.set_privacy(uri)
client.patch(uri, data={'privacy':{'embed': 'whitelist'}})

privacy_list = uri+'?fields=privacy.values'

print (client.get(privacy_list).json())
