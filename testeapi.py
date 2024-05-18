import requests

token = "eb9cd83f807d446ba483048dea6c8dee"
link = f"https://api.weatherbit.io/v2.0/forecast/daily?city=Chopinzinho&key={token}"

requisicao = requests.get(link)


req_json = requisicao.json()
print(req_json)

# previsoes_tempo = []
# for item in req_json["data"]:
#     previsao = {
#         "probabilidade_chuva": item["pop"],
#         "icone_tempo": item["weather"]["icon"]
#     }
#     previsoes_tempo.append(previsao)

# print(previsoes_tempo)
