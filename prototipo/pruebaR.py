import requests

url = "https://app.semarnat.gob.mx/ws-mobiliario/mobiliario"

payload = ""
headers = {
  'Authorization': 'eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJzZW1hcm5hdEpXVCIsInN1YiI6IlVzdWFyaW97c2VnVXN1YXJpb3NJZDoyLHNlZ1VzdWFyaW9zTm9tYnJlVXN1YXJpbzogJ21vYmlsaWFyaW9fZGdpdCcsc2VnVXN1YXJpb3NQYXNzd29yZDogJyQyYSQxMCRXUW83bkhOcXlKaFFncXJBbklIWnB1NnlQU29yYVFyajdrUU45SzJrcGRwbGEuOTl0WXJRMid9IiwiYXV0aG9yaXRpZXMiOlsibW9iaWxpYXJpbyJdLCJpYXQiOjE2NTk3NDIxMDIsImV4cCI6MTY1OTc0MzkwMn0.hsyXu7uKCA9pqDQlmwui_mrOb6CtB5ubbTEIJbPqBs96C7tISkrc3Pz1THY2y4ljnCr0dfzKqa03iNkSB2zRJg'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

