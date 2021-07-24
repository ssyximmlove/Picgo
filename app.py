import pixivpy3
import flask

app = flask.Flask(__name__)
app.config['JSON_AS_ASCII'] = False
apiApp = pixivpy3.AppPixivAPI()
apiApp.auth(refresh_token='MfuFPFrhfNIK1yhqo3GMNIyZSFCvj0DC1NxDWhQfBPM')


@app.route("/")
def index():
    return "这是一个简单的Pixiv Web Api"


@app.route("/illust/", methods=["get"])
def tips():
    return "请在地址栏后输入插画ID，E.G:illust/68912031"


@app.route("/illust/<pid>/", methods=["get"])
def illust(pid):
    json_result = apiApp.illust_detail(pid)
    return flask.jsonify(json_result),200


app.run()
