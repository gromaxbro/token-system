from flask import Flask,request
import random
import string
app = Flask(__name__)


@app.route('/')
def hello():
    return request.remote_addr,'Hello, World!'

@app.route('/generate')
def gen():
    extraa = request.args.get('token')
    if extraa:
        if extraa == "gromaxbro":
            with open("tokens.txt","a") as f:
                length = 20  # You can change the length as needed
                characters = string.ascii_letters 
                token = ''.join(random.choice(characters) for _ in range(length))
                f.write("\n"+token)
                return token,200

    return 'error'


@app.route('/check',methods=["POST"])
def da():
    extra = request.get_json()
    for key, value in extra.items():
        print(value)
        extra = key
        ip = value

        got = ""
        with open("tokens.txt","r") as f:
            mr = f.read().split("\n")
            for tok in mr:
                if extra == tok:
                    got = tok
                    break
            if got == "":
                return "error no token found",200
        with open("ava.txt","r+") as rf:
            ad = rf.read().split("\n")
            for boom in ad:
                if got in boom:
                    hehe = boom.split(":")
                    if hehe[1] == str(ip):
                        return "Accepted valid",200
                    else:
                        return "error nope invalid",200
            rf.write("\n"+extra+":"+ip)

    return "gg",200

    print(extra)
    return "W",200



if __name__ == "__main__":
    app.run(debug=True)