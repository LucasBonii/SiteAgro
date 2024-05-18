from flask import Flask, render_template, url_for
import requests
import datetime

app = Flask(__name__)

@app.route("/")
def homepage():
    try:
        #token = "eb9cd83f807d446ba483048dea6c8dee"
        token =  "8211122e34754b639a85fe95abeb0b02"

        link = f"https://api.weatherbit.io/v2.0/forecast/daily?city=Chopinzinho&key={token}"
        requisicao = requests.get(link)
        req_json = requisicao.json()
        previsoes_tempo = []

        for item in req_json["data"]:
            data = item['valid_date']
            data_obj = datetime.strptime(data, '%Y-%m-%d')
            data_formatada = data_obj.strftime('%d-%m')

            previsao = {
                "probabilidade_chuva": item["pop"],
                "icone_tempo": item["weather"]["icon"],
                "data_previsao": data_formatada
            }
            previsoes_tempo.append(previsao)
        return render_template("home.html", previsoes_tempo=previsoes_tempo)
    except:
        return render_template("home.html")
    
if __name__ == "__main__":
    app.run(debug=True)