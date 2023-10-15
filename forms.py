from wtforms import Form
from wtforms.fields import (
    StringField, SubmitField
)

#使用するvalidatorをインポートする
from wtforms.validators import (
    DataRequired, Length
)
#=============================================
# Formクラス
#=============================================
# 利用者情報クラス
class UserInfoForm(Form):
    # 生年月日
    birthday = StringField('生年月日:', validators=[
                DataRequired('生年月日は必須入力です。'),
                Length(8, 8, '数字8文字。YYYYMMDD')],
                render_kw={"placeholder":"（例）20020101"})
    submit = SubmitField('占い実行')