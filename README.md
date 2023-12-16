# WebUI Style in Prompt

これは AUTOMATIC1111 氏の [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) 用の拡張です。

プロンプトにスタイル名を書くことでスタイルの内容をプロンプトに適用することができます。

## インストール

`stable-diffusion-webui` の `Install from URL` からこのリポジトリのURL `https://github.com/Taremin/webui-style-in-prompt` を入力してインストールしてください。

## 機能

- プロンプトにスタイルを読み込む

## 使用例

`style-name` というスタイルを読み込みます。

```
<style:style-name>
```

複数指定する場合は連続して書くことで読み込みます。

```
<style:style-a:style-b>
```

なお、プロンプトに記述した場合はスタイルのプロンプトのみ、ネガティブプロンプトに記述した場合はスタイルのネガティブプロンプトのみ置き換えられます。

## 注意事項

`Dynamic Prompts` などのプロンプトを変更する拡張よりも早いタイミングで置き換えを行うため、例えば以下のようにコメントアウトしようとしても置き換えが行われます。

```
# <style:style-name>
```

## 設定項目

### Trigger Word

`StyleInPronpt` を有効にする語句の変更が出来ます。
デフォルトでは `style` となっていますが別のものに変更することが可能です。

## ライセンス

[MIT](./LICENSE)
