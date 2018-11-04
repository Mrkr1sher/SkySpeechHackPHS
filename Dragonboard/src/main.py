from flask import *
app = Flask("__name__")

#Dump function
def dumpData(data):
    print(data)

    f = open("messages.json","r")

    currentData = json.load(f)
    
    currentData.append(data)

    f.close()

    print(currentData)

    f = open("messages.json","w")
    json.dump(currentData, f)

    f.close()

    return

   
@app.route("/upload", methods=['POST'])
def handle():

    dumpData(request.data.decode('utf-8'))

    return "Success"

@app.route("/ping", methods=['GET'])
def pong():
    return "Pong!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)