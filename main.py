import time
from flask import Flask, render_template, request

from functions import crud, robot
# from sensors import buttons, dht, rgb, ultrassonic

app = Flask(__name__)

@app.route('/')
def index():
    # crud.create_bd()
    # dados = [15, 0, 0, 30]
    # crud.insert_bd('sensores', dados)
    return render_template('index.html')

@app.route('/auth', methods=['POST', 'GET'])
def auth():
    nome =  request.form.get('nome', False)
    idade = request.form.get('idade', 0)
    turma = [int(idade), nome]
    crud.insert_bd('aluno', turma)
    perguntas_cad = crud.read_bd('perguntas')
    aluno = crud.read_bd('aluno')
    dados = crud.read_bd('sensores')
    return render_template('pergunta.html', ultrassonico=dados[0], bt_verde=dados[1], bt_vermelho=dados[2], temperatura=dados[3], nome=aluno[1], perguntas_cad=reversed(perguntas_cad[-7:]))

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    pergunta = ''
    pergunta =  request.form.get('pergunta')
    resposta = request.form.get('resposta')
    questoes = [pergunta, resposta, '']
    if(pergunta is None):
        print('erro')
    else:
        crud.insert_bd('perguntas', questoes)
        pergunta = ''
    
    perguntas_cad = crud.read_bd('perguntas')
    aluno = crud.read_bd('aluno')
    dados = crud.read_bd('sensores')
    return render_template('pergunta.html', ultrassonico=dados[0], bt_verde=dados[1], bt_vermelho=dados[2], temperatura=dados[3], nome=aluno[1], perguntas_cad=reversed(perguntas_cad[-7:]))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)

# # Teste de acionamento do LED RGB
# def main():
#     setup()
#     try:
#         while True:
#             # Liga a cor vermelha
#             set_color(1, 0, 0)
#             time.sleep(1)
#             # Liga a cor verde
#             set_color(0, 1, 0)
#             time.sleep(1)
#             # Liga a cor azul
#             set_color(0, 0, 1)
#             time.sleep(1)
#     except KeyboardInterrupt:
#         GPIO.cleanup()

# if __name__ == "__main__":
#     main()