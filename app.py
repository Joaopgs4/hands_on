from flask import Flask,request

sabores_list = ['Baunilha', 'Chocolate', 'Limao', 'Uva', 'Menta']

app = Flask('Minha Sorveteria')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/sabores", methods=['GET'])
def sabores():

    dict_resposta = {'sabores': sabores_list}

    return dict_resposta

@app.route("/sabor/<int:id_list>", methods=['GET'])
def sabor_id(id_list):
    return sabores_list[id_list]

@app.route("/adiciona_sabor", methods=['POST'])
def adiciona_sabor():

    request_data = request.json
    if 'sabor' not in request_data:
        return "Sabor não informado", 400

    sabores_list.append(request_data['sabor'])

    return f'Sabor {request_data["sabor"]} foi adicionado com sucesso'

@app.route("/apaga_sabor", methods=['GET'])
def remove_sabor():

    request_sabor = request.args.get('sabor')
    if request_sabor not in sabores_list:
        return "Sabor não existe", 404

    sabores_list.remove(request_sabor)

    return f'Sabor {request_sabor} foi removido. Agora restam: \n {sabores_list}'




if __name__ == '__main__':
    app.run(debug=True)