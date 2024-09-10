import requests
from datetime import datetime
today=datetime(day=12,month=2,year=2023)
day=today.now().strftime("%Y%m%d")

pixela_endpoint="https://pixe.la/v1/users"
USER="a-mna"
TOKEN="gfhg4567fdsk3"
params={
"token":TOKEN,
    "username":"a-mna",
"agreeTermsOfService":"yes",
"notMinor":"yes"
}
"""respond=requests.post(url=pixela_endpoint,json=params)
print(respond.text)"""
graph_header={
"X-USER-TOKEN":TOKEN
}
graph_params={
"id":"manar-draw",
"name":"coding-tracker",
    "unit":"hour",
"type":"float",
"color":"shibafu"
}
graph_endpoint=f"https://pixe.la/v1/users/{USER}/graphs"
"""graph_respond=requests.post(url=graph_endpoint,json=graph_params,headers=graph_header)
print(graph_respond.text)"""
url=f"https://pixe.la/v1/users/{USER}/graphs/manar-draw"
url_header={
    "X-USER-TOKEN":TOKEN,
}
url_params={
    "date":f"{day}",
    "quantity":input("How many hours did you Code Today ?"),

}
pix_respond=requests.post(url=url,json=url_params,headers=url_header)
print(pix_respond.text)
"""update_url=f"https://pixe.la/v1/users/a-mna/graphs/manar-draw/20230213"
update_params={
"quantity":"3.5",
"optionalData":"{\"color\":\"sora\"}"

}"""
"""update_respond=requests.put(url=update_url,json=update_params,headers=graph_header)
print(update_respond.text)"""
"""delete_url="https://pixe.la/v1/users/a-mna/graphs/manar-draw/20230213"
delete_respond=requests.delete(url=delete_url,headers=url_header)
print(delete_respond.text)"""