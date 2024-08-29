import google.generativeai as genai

genai.configure(api_key="AIzaSyCq-L4GHVc0heFeCRV45Fmo4cqZfJTVBZ4")
# モデルを指定
model = genai.GenerativeModel('models/gemini-1.0-pro-latest')

# テキストを生成
response = model.generate_content("あなたはGemini？あなたにできることを5つ教えて？")

# 結果を表示
print(response.text)