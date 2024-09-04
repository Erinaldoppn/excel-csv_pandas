from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Carrega os dados de um arquivo Excel
    df = pd.read_excel("C:/Users/Erinaldo/Downloads/relatorio.xlsx")
    
    # Converte o DataFrame em uma lista de dicionários
    dados = df.to_dict(orient='records')
    
    # Passa os dados para o template
    return render_template('index.html', dados=dados)

if __name__ == '__main__':
    app.run(debug=True)

