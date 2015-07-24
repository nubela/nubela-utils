from {{MODULE_NAME}}.app import app

def index():
    return "works"

app.add_url_rule('/',
                 "index", index, methods=['GET'])