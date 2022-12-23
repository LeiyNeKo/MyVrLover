from flask import Flask, request, render_template

global gap # 服务器储存的“时间差”
gap = '100'
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') # 响应视频页面

@app.route('/set_gap') # 接收来自FuckMyPet的“时间差”
def set_gap():
    global gap
    gap = request.args['gap'] # 更新“时间差”
    return ''

@app.route('/get_gap') # 向视频页面传递“时间差”
def get_gap():
    global gap
    return gap

app.run(host='0.0.0.0', port=80) # 开启服务器