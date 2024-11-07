from flask import Flask, render_template, request, redirect, url_for
import pandas as pd 
import joblib as jb

transformer = jb.load("./transformer_anunciante.joblib")    
predict = jb.load("./predict_anunciante.joblib")

app = Flask(__name__)


def processar_base_forms(base_forms: pd.DataFrame) -> pd.DataFrame:
    # Substituir valores ausentes nas colunas específicas
    base_forms["regiao"] = base_forms["regiao"].fillna("N/A Regiao")
    base_forms["dificuldade_divulgacao"] = base_forms["dificuldade_divulgacao"].fillna("Não")
    base_forms["difuculdade_participacao"] = base_forms["difuculdade_participacao"].fillna("Não")
    base_forms["is_microempreendedor"] = base_forms["is_microempreendedor"].fillna("Não")
    base_forms["meios_divulgacao"] = base_forms["meios_divulgacao"].fillna("Não costumo divulgar")
    base_forms["frequencia_divulgacao"] = base_forms["frequencia_divulgacao"].fillna("Não costumo divulgar")
    base_forms["pagar_divulgacao"] = base_forms["pagar_divulgacao"].fillna("Não pagaria")
    
    # Transformar strings: minúsculas e remover espaços extras
    for i in base_forms.columns:
        base_forms[i] = base_forms[i].apply(lambda x: x.lower().strip() if isinstance(x, str) else x)

    # Tratamento específico para a coluna 'meios_divulgacao'
    base_forms["meios_divulgacao"] = base_forms["meios_divulgacao"].apply(
        lambda x: x[:-1].lower().replace(" ","_").split(";") if x.split(";")[-1] == "" else x.lower().replace(" ","_").split(";")
    )
    
    # Explodir a coluna 'meios_divulgacao' para que cada item ocupe uma linha separada
    base_forms = base_forms.explode("meios_divulgacao")
    
    # Substituir valores específicos dentro da coluna 'meios_divulgacao'
    base_forms["meios_divulgacao"] = base_forms["meios_divulgacao"].replace({
        "não_costumo_divulga": "não_costumo_divulgar",
        "redes_sociais_(instagram,_facebook,_etc.)": "redes_sociais"
    })
    
    return base_forms



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def novos_dados():
    req = request.form
    
    registro = pd.DataFrame(
        data=[[req["faixa_etaria"], req["regiao"], req["tipo_usuario"], req["dificuldade_divulgacao"], 
               req["difuculdade_participacao"], req["is_microempreendedor"], req["frequencia_divulgacao"], 
               req["pagar_divulgacao"], req["meios_divulgacao"], req["receber_notificacao"]]],
        columns=["faixa_etaria", "regiao","tipo_usuario", "dificuldade_divulgacao", "difuculdade_participacao", 
                 "is_microempreendedor", "frequencia_divulgacao", "pagar_divulgacao", "meios_divulgacao", "receber_notificacao"]
    )
    
    regitro = processar_base_forms(registro)
    regitro = pd.get_dummies(regitro, columns=["meios_divulgacao"])
    regitro = regitro.reset_index()
    regitro = regitro.drop_duplicates(subset="index",keep="first").drop("index", axis=1)    
    
    # Lista de colunas obrigatórias
    required_columns = [
        "meios_divulgacao_boca_a_boca",
        "meios_divulgacao_redes_sociais",
        "meios_divulgacao_sites_ou_blogs",
        "meios_divulgacao_panfletos/flyers",
        "meios_divulgacao_não_costumo_divulgar"
    ]

    # Verificação e adição de colunas ausentes
    for column in required_columns:
        if column not in registro.columns:
            registro[column] = False  # Adiciona a coluna faltante com valor False

    # Realiza a transformação
    registro = transformer.transform(registro)
    result = predict.predict(registro)
    
    
    return redirect(url_for('sucesso', result=result[0]))
    
@app.route('/result/<result>')
def sucesso(result):
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')
