from flask import Flask , jsonify , request

 #creo la app flask
app = Flask (__name__) 

todos = [{"label": "My first task", "done": False}, {"labe": "my second task", "done": }]

    

@app.route('/todos', methods=['GET'])
def hello_world():
  json_text = jsonify(todos)
  return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is yhe position to delete:", position)
    todos.pop(position)
    return jsonify(todos)

#ejecuto la app flask
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3245, debug = True)
    
    
    
  