import requests
import json

url = "https://app.semarnat.gob.mx/ws-mobiliario/mobiliario"

payload = ""
headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJzZW1hcm5hdEpXVCIsInN1YiI6IlVzdWFyaW97c2VnVXN1YXJpb3NJZDoyLHNlZ1VzdWFyaW9zTm9tYnJlVXN1YXJpbzogJ21vYmlsaWFyaW9fZGdpdCcsc2VnVXN1YXJpb3NQYXNzd29yZDogJyQyYSQxMCRXUW83bkhOcXlKaFFncXJBbklIWnB1NnlQU29yYVFyajdrUU45SzJrcGRwbGEuOTl0WXJRMid9IiwiYXV0aG9yaXRpZXMiOlsibW9iaWxpYXJpbyJdLCJpYXQiOjE2NjAwODExOTMsImV4cCI6MTY2MDA4Mjk5M30.bNxcVvj15PFbZWgzJJnDjkRpRe6YDAvn9b-CVHinyg-bJS75lIUj7C3_w4-NFN6OsV4SmK6kSIAFZTon8VVzog',
  'Cookie': 'JSESSIONID="CThmwvA1-YoVZ596RvyIMjJXRJCaVqolbQ9TBET3.master-10.150.13.36:server-three"'
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)


if response.status_code == 200:
     response = response.json()
    # print(response)
     for e in response['Consulta']: 
        print(e['resguardante'])
        print(e['descripcionCabms'])
        print(e['descripcion'])
        print("")

     lista=json.loads(response)

     print(type(lista))


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
