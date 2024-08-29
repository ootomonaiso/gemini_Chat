import google.generativeai as genai
import tkinter as tk
from tkinter import filedialog, messagebox
import re
import sys

# コンソールログ出力用
def log(message):
    print(message)
    sys.stdout.flush()

# Google Generative AI の設定
log("Setting up Google Generative AI...")
genai.configure(api_key="AIzaSyCq-L4GHVc0heFeCRV45Fmo4cqZfJTVBZ4")

# モデルの初期化
log("Initializing the Generative Model...")
model = genai.GenerativeModel('gemini-1.0-pro-latest')

# 友達プロファイルをマークダウンファイルに保存
def save_friend_profile(profile):
    log("Saving friend profile...")
    file_path = filedialog.asksaveasfilename(defaultextension=".md",
                                             filetypes=[("Markdown files", "*.md"), ("All files", "*.*")],
                                             title="プロファイルの保存先を選択")
    if file_path:
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(f"# 友達クリエーター: 人格設定ファイル\n\n")
                file.write(f"## 名前\n- **name**: \"{profile['name']}\"\n")
                file.write(f"  - **説明**: {profile['name']}は{profile['personality']}で、{profile['hobbies']}が好きです。\n\n")
                file.write(f"## 性別\n- **gender**: \"{profile['gender']}\"\n")
                file.write(f"  - **説明**: {profile['name']}の性別は{profile['gender']}です。\n\n")
                file.write(f"## 年齢\n- **age**: \"{profile['age']}\"\n")
                file.write(f"  - **説明**: {profile['name']}の年齢は{profile['age']}歳です。\n\n")
                file.write(f"## ユーザーとの関係\n- **relationship**: \"{profile['relationship']}\"\n")
                file.write(f"  - **説明**: {profile['name']}とあなたの関係は{profile['relationship']}です。\n\n")
                file.write(f"## 趣味\n- **hobbies**: \"{profile['hobbies']}\"\n")
                file.write(f"  - **説明**: {profile['name']}は{profile['hobbies']}を楽しむことが好きです。\n\n")
                file.write(f"## 特技\n- **skills**: \"{profile['skills']}\"\n")
                file.write(f"  - **説明**: {profile['name']}の特技は{profile['skills']}です。\n\n")
                file.write(f"## 興味\n- **interests**: \"{profile['interests']}\"\n")
                file.write(f"  - **説明**: {profile['name']}は{profile['interests']}に興味を持っています。\n\n")
                file.write(f"## 話し方\n- **speech_style**: \"{profile['speech_style']}\"\n")
                file.write(f"  - **説明**: {profile['name']}の話し方は{profile['speech_style']}です。\n")
            messagebox.showinfo("保存完了", f"プロファイルが {file_path} に保存されました。")
            log(f"Profile saved to {file_path}")
            return file_path
        except Exception as e:
            log(f"Error saving profile: {str(e)}")
            messagebox.showerror("エラー", f"プロファイルの保存に失敗しました: {str(e)}")
            return None
    else:
        log("Profile save canceled.")
        messagebox.showwarning("キャンセル", "保存がキャンセルされました。")
        return None

# マークダウンファイルから友達プロファイルを読み込む
def load_friend_profile(file_path):
    log(f"Loading friend profile from {file_path}...")
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                log(f"Profile content: {content}")
                
                # 正規表現でプロファイル情報を抽出
                profile = {}
                for key in ['name', 'gender', 'age', 'relationship', 'hobbies', 'skills', 'interests', 'speech_style']:
                    match = re.search(rf'\*\*{key}\*\*: "([^"]*)"', content)
                    if match:
                        profile[key] = match.group(1)
                    else:
                        messagebox.showerror("エラー", f"プロファイルの項目「{key}」が見つかりません。")
                        return None
                
                profile['description'] = "未設定"
                log(f"Profile loaded: {profile}")
                return profile
        except Exception as e:
            log(f"Error loading profile: {str(e)}")
            messagebox.showerror("エラー", f"プロファイルの読み込みに失敗しました: {str(e)}")
            return None
    else:
        log("Profile load canceled.")
        messagebox.showwarning("キャンセル", "ファイルの読み込みがキャンセルされました。")
        return None

# Google Generative AIを使って友人を作成（同期バージョン）
def create_friend_from_profile(profile):
    log("Creating friend from profile...")
    prompt = (
        f"Create a friend with the following characteristics:\n"
        f"Name: {profile['name']}\n"
        f"Gender: {profile['gender']}\n"
        f"Age: {profile['age']}\n"
        f"Relationship: {profile['relationship']}\n"
        f"Hobbies: {profile['hobbies']}\n"
        f"Skills: {profile['skills']}\n"
        f"Interests: {profile['interests']}\n"
        f"Speech Style: {profile['speech_style']}\n"
    )
    
    try:
        log(f"Prompt for Generative AI: {prompt}")
        response = model.generate_content(prompt)
        friend_description = response.text.strip()
        profile['description'] = friend_description
        log(f"Friend description generated: {friend_description}")
        return profile
    except Exception as e:
        log(f"Error generating friend: {str(e)}")
        messagebox.showerror("エラー", f"友達の生成に失敗しました: {str(e)}")
        return None

# チャット機能の実装（同期バージョン）
def chat_with_friend(friend_profile, message):
    log(f"Chatting with friend: {friend_profile['name']}")
    prompt = (
        f"You are chatting with a friend named {friend_profile['name']} who has the following characteristics: "
        f"Gender: {friend_profile['gender']}, Age: {friend_profile['age']}, "
        f"Relationship: {friend_profile['relationship']}, Hobbies: {friend_profile['hobbies']}, "
        f"Skills: {friend_profile['skills']}, Interests: {friend_profile['interests']}, "
        f"Speech Style: {friend_profile['speech_style']}. "
        f"Friend's response to '{message}':"
    )
    
    try:
        log(f"Chat prompt: {prompt}")
        response = model.generate_content(prompt)
        reply = response.text.strip()
        log(f"Friend's reply: {reply}")
        return reply
    except Exception as e:
        log(f"Error during chat: {str(e)}")
        messagebox.showerror("エラー", f"チャット中にエラーが発生しました: {str(e)}")
        return "エラーが発生しました。"

# チャットの開始（同期バージョン）
def start_chat(file_path=None):
    log("Starting chat...")
    friend_profile = load_friend_profile(file_path)
    if friend_profile is None:
        return
    
    friend_profile = create_friend_from_profile(friend_profile)
    if friend_profile is None:
        return
    
    def send_message():
        user_message = user_input.get()
        log(f"User message: {user_message}")
        reply = chat_with_friend(friend_profile, user_message)
        chat_log.insert(tk.END, f"You: {user_message}\nFriend: {reply}\n")
        user_input.delete(0, tk.END)

    chat_window = tk.Toplevel(root)
    chat_window.title(f"{friend_profile['name']}とのチャット")

    chat_log = tk.Text(chat_window)
    chat_log.pack()

    user_input = tk.Entry(chat_window)
    user_input.pack()

    send_button = tk.Button(chat_window, text="送信", command=send_message)
    send_button.pack()

# 友達設定用の日本語GUI
def setup_friend_profile():
    log("Setting up friend profile...")
    def save_profile():
        name = name_entry.get()
        gender = gender_entry.get()
        age = age_entry.get()
        relationship = relationship_entry.get()
        hobbies = hobbies_entry.get()
        skills = skills_entry.get()
        interests = interests_entry.get()
        speech_style = speech_style_entry.get()
        
        if not all([name, gender, age, relationship, hobbies, skills, interests, speech_style]):
            log("Profile setup: missing fields.")
            messagebox.showwarning("入力エラー", "全てのフィールドに入力してください。")
            return
        
        profile = {
            "name": name,
            "gender": gender,
            "age": age,
            "relationship": relationship,
            "hobbies": hobbies,
            "skills": skills,
            "interests": interests,
            "speech_style": speech_style
        }
        
        file_path = save_friend_profile(profile)
        if file_path:
            setup_window.destroy()
            start_chat(file_path)  # 同期関数を実行

    setup_window = tk.Toplevel(root)
    setup_window.title("友達のプロファイル設定")

    tk.Label(setup_window, text="名前:").pack()
    name_entry = tk.Entry(setup_window)
    name_entry.pack()

    tk.Label(setup_window, text="性別:").pack()
    gender_entry = tk.Entry(setup_window)
    gender_entry.pack()

    tk.Label(setup_window, text="年齢:").pack()
    age_entry = tk.Entry(setup_window)
    age_entry.pack()

    tk.Label(setup_window, text="ユーザーとの関係:").pack()
    relationship_entry = tk.Entry(setup_window)
    relationship_entry.pack()

    tk.Label(setup_window, text="趣味:").pack()
    hobbies_entry = tk.Entry(setup_window)
    hobbies_entry.pack()

    tk.Label(setup_window, text="特技:").pack()
    skills_entry = tk.Entry(setup_window)
    skills_entry.pack()

    tk.Label(setup_window, text="興味:").pack()
    interests_entry = tk.Entry(setup_window)
    interests_entry.pack()

    tk.Label(setup_window, text="話し方:").pack()
    speech_style_entry = tk.Entry(setup_window)
    speech_style_entry.pack()

    tk.Button(setup_window, text="保存してチャットを開始", command=save_profile).pack()

# メインウィンドウの設定
log("Setting up main window...")
root = tk.Tk()
root.title("Google Generative AI 友達クリエーター")

tk.Button(root, text="友達のプロファイルを設定", command=setup_friend_profile).pack()
tk.Button(root, text="既存のプロファイルでチャット", command=lambda: start_chat(filedialog.askopenfilename())).pack()

log("Starting main loop...")
root.mainloop()
