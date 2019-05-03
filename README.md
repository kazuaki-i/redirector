# redirector

This program redirects a targets site by Python3 Flask.

# How to use

## Setup

Place this program on your Apache http available Server by `git clone` and so on.

Edit below two files:

### .htaccess
```
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule ^(.*)$ /your_placed_path/index.cgi/$1 [QSA,L]
```
- Root directory is your domain (not server path)

### index.cgi
```
#!/your_path/python
from wsgiref.handlers import CGIHandler
from app import app
CGIHandler().run(app)
```

## Try to use
When you placed *redirector* to domain top, you request `https://hogehoge.com/redirector/?l=target_link`

---

# redirector
このプログラムはPython3のFlaskで実装されたリダイレクトするだけのプログラムです。

# 使い方

## セットアップ
まず、Apacheがインストールされているサーバーに、`git clone`などで、ドメイン以下に配置してください。

その後、以下の２つのファイルを自分の環境に合わせて編集してください。

### .htaccess
```
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule ^(.*)$ /配置したパス/index.cgi/$1 [QSA,L]
```
- ※ ここでのルートはドメインのルートです。

### index.cgi
```
#!使いたいPython3のパス
from wsgiref.handlers import CGIHandler
from app import app
CGIHandler().run(app)
```

## 試してみる
ドメイン直下に*redirector*として保存した場合は、`https://hogehoge.com/redirector/?l=target_link`で使用できます。
