from flask import Flask

app = Flask(__name__)

def soma(a, b):
    return a + b

@app.route('/')
def home():
    return {"mensagem": "App rodando!", "resultado": soma(10, 5)}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)