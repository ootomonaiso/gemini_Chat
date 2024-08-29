# 架空のお友達作成アプリケーション
あなたと話してくれるお友達を作ります。
apiの都合上、48時間記憶を保持するのでクリスマスイブとクリスマスをぎりぎり一緒に過ごしてくれます。

## Pythonの仮想環境をアクティベートする
```
.\test\Scripts\activate
```
*gemini_Chat*ディレクトリにいるときにこれ実行すれば動きます。仮想環境で開発を行えます。

### 仮想環境にインストールされている依存関係一覧
```
annotated-types==0.7.0
cachetools==5.5.0
certifi==2024.7.4
charset-normalizer==3.3.2
colorama==0.4.6
google-ai-generativelanguage==0.6.6
google-api-core==2.19.1
google-api-python-client==2.141.0
google-auth==2.34.0
google-auth-httplib2==0.2.0
google-generativeai==0.7.2
googleapis-common-protos==1.63.2
grpcio==1.65.5
grpcio-status==1.62.3
httplib2==0.22.0
idna==3.7
proto-plus==1.24.0
protobuf==4.25.4
pyasn1==0.6.0
pyasn1_modules==0.4.0
pydantic==2.8.2
pydantic_core==2.20.1
pyparsing==3.1.2
requests==2.32.3
rsa==4.9
tqdm==4.66.5
typing_extensions==4.12.2
uritemplate==4.1.1
urllib3==2.2.2
```
*requirements.txt*に上記と同様の内容のファイルがあります。
次のコマンドを実行することによりこの仮想環境と同様の環境を再現できます。
```
pip install -r requirements.txt
```