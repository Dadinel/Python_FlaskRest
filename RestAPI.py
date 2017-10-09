from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/',methods=["GET"])
def api_root():
    if request.method == 'GET':
        return 'API REST, Welcome!'

@app.route('/html',methods=["GET"])
def api_html():
    html = ''
    html += '<html>'
    html += ' <head>'
    html += ' <title>HTML Return</title>'
    html += ' </head>'
    html += ' <body>'
    html += '  <script type="text/javascript">'
    html += '   function buttonClick() {'
    html += '       alert( "You can return a html with REST!" )'
    html += '   }'
    html += '  </script>'
    html += '  <p><b>This is a HTML example</b></p>'
    html += '  <button type="button" onClick="buttonClick()">Click Me!</button>'
    html += ' </body>'
    html += '</html>'
    return html

@app.route('/HelloWorld',methods=["GET"])
def api_HelloWorld():
    if request.method == 'GET':
        return jsonify(Text="Hello World! ^_^")

@app.route('/WithData/<id>',methods=["GET"])
def api_WithData(id):
    if request.method == 'GET':
        return 'Your ID: ' + str(id)

if __name__ == '__main__':
    app.run()
