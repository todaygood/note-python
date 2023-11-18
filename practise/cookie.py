from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def hello_world():
    resp = make_response("success")
    resp.set_cookie("name", "python")
    resp.set_cookie("name2", "go")
    return resp

app.run(debug=True)



cookie = requests.utils.dict_from_cookiejar(mid_cookies)