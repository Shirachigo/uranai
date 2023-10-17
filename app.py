from flask import Flask, render_template, request

import service.aisyou_rank_service as ars
import service.soul_number_service as sns

# インスタンス生成
app = Flask(__name__)

# ◆◆◆◆◆◆◆ ルーティング ◆◆◆◆◆◆◆
from forms import UserInfoForm

# TOPページ
@app.route('/', methods=['GET','POST'])
def index():
    # フォームの作成
    form = UserInfoForm(request.form)
    # POST
    if request.method == "POST" and form.validate():
        birthday = form.birthday.data
        no = sns.get_soulno(birthday)
        rankings = ars.aisyou_check(no)
        return render_template('compatibility_soul.html', rankings=rankings)
    return render_template('top.html', form=form)

# 相性ランキング（ソールナンバー）
@app.route('/soul')
def compatibility_soul():
    birthday = '19740402'
    no = sns.get_soulno(birthday)
    rankings = ars.aisyou_check(no)
    return render_template('compatibility_soul.html', rankings=rankings)

@app.route('/soul/no01')
def soulno_01():
    return render_template('soulno01.html')

# 相性ランキング（六星占術）
@app.route('/sixstar')
def compatibility_six_stars():
    return render_template('compatibility_six_stars.html')

if __name__ == '__main__':
    app.run()