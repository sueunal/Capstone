import requests
import hashlib

def virustotal(my_file_name):
    url = "https://www.virustotal.com/api/v3/files/" + my_file_name
    headers = {
        "accept": "application/json",
        "x-apikey": "912884d69a5188c31eefa29806f557ac7936c884f17aae126abd3aee32e07bf4"
    }
    response = requests.get(url, headers=headers)
    data = response.text.split()
    for i in data:
        if i == '"detected",':
            return True 
        else:
            return False
def file_hashing(inputfile):
    f = open("temp/"+inputfile,'rb')
    data = f.read()
    hash = hashlib.md5(data).hexdigest()
    return virustotal(my_file_name=hash)

