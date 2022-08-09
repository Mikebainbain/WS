import requests
import json

url = "https://app.semarnat.gob.mx/ws-mobiliario/mobiliario"

payload = ""
headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJzZW1hcm5hdEpXVCIsInN1YiI6IlVzdWFyaW97c2VnVXN1YXJpb3NJZDoyLHNlZ1VzdWFyaW9zTm9tYnJlVXN1YXJpbzogJ21vYmlsaWFyaW9fZGdpdCcsc2VnVXN1YXJpb3NQYXNzd29yZDogJyQyYSQxMCRXUW83bkhOcXlKaFFncXJBbklIWnB1NnlQU29yYVFyajdrUU45SzJrcGRwbGEuOTl0WXJRMid9IiwiYXV0aG9yaXRpZXMiOlsibW9iaWxpYXJpbyJdLCJpYXQiOjE2NjAwMDA2NTUsImV4cCI6MTY2MDAwMjQ1NX0.ooWBfG6y-lQ3g_CwML5pwHrdU3Tyz4W0F-hRO3xd5fd_vnF3kyvqLFToDqpluB9KYNCQhmA3tIcvPw0aPdc-ew',
  'Cookie': 'JSESSIONID="j5jMTHZ3R8Ekdae-ohXm-ji7Bg3ANYtcdPoS13MT.master-10.150.13.36:server-three"'
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

response=response.json()
print(response)

# response_dict=json.loads(response)
# print(type(response_dict))

# print(response_dict["resguardante"])


"""
userdata = json.loads(str(response.json())[0])

resguardante =  userdata["resguardante"]
descripcionCabms = userdata["descripcionCabms"]
descripcion = userdata["descripcion"]


print(f"{resguardante} es el reguardante")
print(f"{descripcionCabms} queda en resguardo")
print(f"Su descripcion: {descripcion}")
"""
