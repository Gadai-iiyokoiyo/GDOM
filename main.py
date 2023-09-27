import Gdom as gdom


connect = gdom.Connect()
url = input("URL:\t")
print("----------------HTML----------------")
print(connect.get(url,None).text)
print("\n----------------INFO----------------")
print(connect.info(url))