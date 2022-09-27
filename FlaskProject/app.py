from flask import Flask, request, jsonify render_template

app = Flask(__name__)

memcache={} 

@app.route("/")
def salute():
    return "Hello Dayo! Great Job"

@app.route("/about")
def about():
    return "A bio-datascientist"


@app.route("/about/<name>")
def name(name):
    return f"Tell more about {name}" 

@app.route("/cache", methods=["GET","POST"])
def cache():
    if request.method == "POST":
        memcache.update(request.json)
        return "Success"
    else:
        return jsonify(memcache)

