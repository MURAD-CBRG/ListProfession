from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'INFORMATION_SECURITY'


@app.route('/list/<list_param>')
def list_func(list_param):
    profession_list = ['Инженер-конструктор',
                       'Специалист по защите информации',
                       'Радиофизик',
                       'Специалист по ионизирующему излучению',
                       'Астроном',
                       'Ядерный физик']

    return render_template('list_param.html',
                           profession_list=profession_list,
                           list_param=list_param)


def main():
    app.run(host='127.0.0.1', port=8080)


if __name__ == '__main__':
    main()
