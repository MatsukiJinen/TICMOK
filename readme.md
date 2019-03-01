# Introduction to MockUp Automatic Generation Site
MockUp Automatic Generation Siteは、プログラマーのためにモックアップのHTMLファイルを自動生成するためのサイトです。

## 初期設定
インストール手順を下記に記載します

```bash
git clone https://github.com/MatsukiJinen/mockup-generator.git

cd mockup-generator
composer install
npm install
npm run watch

# 別のウィンドウを起動
php artisan queue:listen
```

## 動作確認

https://mockup.takeys.link/
にアクセスする


