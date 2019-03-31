# coding: utf-8

from requests import get
import JSON
from flask import Flask, render_template, make_response, request, redirect
from flask_wtf import FlaskForm
 
app = Flask(__name__)
@app.route('/')
def pereadress():
    return redirect('/news')

@app.errorhandler(404)
def not_found(error):
    return '''<img src="{}" alt="здесь должна была быть картинка, 
    но не нашлась">'''.format(url_for('static', filename='img/Риана.jpg'))


@app.route('/news',  methods=['GET'])
def get_news():
    news = NewsModel(db.get_connection()).get_all()
    return jsonify({'news': news})

@app.route('/news/<int:news_id>',  methods=['GET'])
def get_one_news(news_id):
    news = NewsModel(db.get_connection()).get(news_id)
    if not news:
        return jsonify({'error': 'Not found'})
    return jsonify({'news': news})

@app.route('/news', methods=['POST'])
def create_news():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in ['title', 'content', 'user_id']):
        return jsonify({'error': 'Bad request'})
    news = NewsModel(db.get_connection())
    news.insert(request.json['title'], request.json['content'],
                request.json['user_id'])
    return jsonify({'success': 'OK'})

@app.route('/news/<int:news_id>', methods=['DELETE'])
def delete_news(news_id):
    news = NewsModel(db.get_connection())
    if not news.get(news_id):
        return jsonify({'error': 'Not found'})
    news.delete(news_id)
    return jsonify({'success': 'OK'})

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
