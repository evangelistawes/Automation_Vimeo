import UpClient

#Set the privacy configuration

def set_privacy(uri):
    UpClient.client.patch(uri, data={
'privacy': {
    'view': 'nobody'
}})
   

#Set the  embed configuration
def set_embed(uri):

    UpClient.client.patch(uri, data={'privacy':{'embed': 'whitelist'}})

   

