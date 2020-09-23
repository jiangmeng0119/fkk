# coding: utf-8
import sqlite3
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def con_db():
    """
    链接数据
    :return:
    """
    return sqlite3.connect(r'data.db', check_same_thread=False)


@app.route('/')
def login():
    """
    登录页面
    :return:
    """
    return render_template('login.html')


# @app.route('/dingdan/')
# def dingdan():
#     """
#     订单页面
#     :return:
#     """
#     return render_template('dingdan.html')


@app.route('/tuihuan/')
def tuihuan():
    """
    退换页面
    :return:
    """
    return render_template('tuihuan.html')


@app.route('/login/', methods=['POST'])
def login_():
    """
    登录流程
    :return:
    """
    user = request.form.get('user')
    pwd = request.form.get('pwd')
    if user == 'admin' and pwd == 'admin':
        return jsonify({'code': 0, 'msg': '登录成功'})
    return jsonify({'code': 1, 'msg': '账号或密码错误'})


@app.route('/index/')
def index():
    """
    搜索页面
    :return:
    """
    sc = request.args.get('sc')
    con = con_db()
    con.row_factory = dict_factory
    cu = con.cursor()
    cu.execute("""select * from d where spmc like '%{}%'""".format(sc))

    return render_template('index.html', **{'data': cu.fetchall()})

@app.route('/dingdan/')
def dingdan():
    """
    订单页面
    :return:
    """
    sc = request.args.get('sc')
    con = con_db()
    con.row_factory = dict_factory
    cu = con.cursor()
    cu.execute("""select * from d where spmc like '%{}%'""".format(sc))

    return render_template('dingdan.html', **{'data': cu.fetchall()})


if __name__ == '__main__':
    app.run()
