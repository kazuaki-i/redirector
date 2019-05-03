import string
from flask import Flask, request


HTML = '''\
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <title>redirect</title>
  <meta http-equiv="refresh" content="0; URL='${link}'" />'
</head>
<body>
    このページは自動的に転送されます。<br>
    転送されない場合は<a href="${link}">こちら</a>をクリックしてください
</body>
</html>
'''

app = Flask(__name__)


@app.route('/')
def index():
    link = request.args.get('l', '')
    assert link, 'Cannot get l parameter querystring'
    return string.Template(HTML).safe_substitute({'link': link})


if __name__ == '__main__':
    app.debug = True # デバッグモード有効化
    app.run(host='0.0.0.0') # どこからでもアクセス可能に
