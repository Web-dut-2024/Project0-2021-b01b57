from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# 首页 (Google 搜索页面)
@app.route('/')
def index():
    return render_template('index.html')

# 图片搜索页面
@app.route('/image')
def image_search():
    return render_template('image.html')

# 高级搜索页面
@app.route('/advanced')
def advanced_search():
    return render_template('advanced.html')

# 处理 “I'm Feeling Lucky” 的按钮请求
@app.route('/feeling_lucky', methods=['GET'])
def feeling_lucky():
    query = request.args.get('q')
    if query:
        return redirect(f"https://www.google.com/search?q={query}&btnI=1")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
