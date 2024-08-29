import PySimpleGUI as sg
import pytesseract
from pdf2image import convert_from_path
import google.generativeai as genai

# Tesseractのパスを設定（必要に応じて）
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Gemini APIの設定
genai.configure(api_key="AIzaSyCq-L4GHVc0heFeCRV45Fmo4cqZfJTVBZ4")
model = genai.GenerativeModel('models/gemini-1.0-pro-latest')

# GUIの設定
layout = [
    [sg.Text('PDFファイルを選択してください')],
    [sg.Input(key='-FILE-'), sg.FileBrowse()],
    [sg.Button('PDFを読み込む')],
    [sg.Multiline(size=(60, 20), key='-OUTPUT-')]
]

window = sg.Window('PDF要約ツール', layout)

# イベントループ
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'PDFを読み込む':
        pdf_path = values['-FILE-']
        try:
            # PDFを画像に変換
            images = convert_from_path(pdf_path)

            text = ""
            for image in images:
                # 画像からテキストを抽出
                text += pytesseract.image_to_string(image, lang='jpn')

            # テキストをGeminiで要約
            response = model.generate_content(text)
            summary = response.text

            # 要約結果をGUIに表示
            window['-OUTPUT-'].update(summary)

        except Exception as e:
            sg.popup_error(f'エラーが発生しました: {e}')

window.close()
