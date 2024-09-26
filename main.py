from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Создаем приложение Flask
app = Flask(__name__)

# Настраиваем базу данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Создаем объект SQLAlchemy
db = SQLAlchemy(app)

# Определяем модель данных (таблицу в базе данных)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)\

    def __repr__(self):
        return f'<User {self.username}>'

# Создаем таблицу в базе данных
with app.app_context():
    db.create_all()

# Добавляем запись в таблицу
@app.route('/add_user')
def add_user():
    new_user = User(username='John Doe')
    db.session.add(new_user)
    db.session.commit()
    return 'User added successfully!'

# Получаем записи из таблицы
@app.route('/users')
def get_users():
    users = User.query.all()
    return str(users)

# Запускаем приложение Flask
if __name__ == '__main__':
    app.run(debug=True)


