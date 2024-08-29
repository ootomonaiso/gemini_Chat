import tkinter as tk
from tkinter import filedialog, messagebox

# 詳細化された友達プロファイルをマークダウンファイルに保存
def save_detailed_friend_profile(profile):
    file_path = filedialog.asksaveasfilename(defaultextension=".md",
                                             filetypes=[("Markdown files", "*.md"), ("All files", "*.*")],
                                             title="プロファイルの保存先を選択")
    if file_path:
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(f"# 詳細友達プロファイル\n\n")
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
            return file_path
        except Exception as e:
            messagebox.showerror("エラー", f"プロファイルの保存に失敗しました: {str(e)}")
            return None
    else:
        messagebox.showwarning("キャンセル", "保存がキャンセルされました。")
        return None

# GUI で友達プロファイルを作成する
def create_friend_profile():
    def save_profile():
        name = name_entry.get()
        gender = gender_entry.get()
        age = age_entry.get()
        relationship = relationship_entry.get()
        hobbies = hobbies_entry.get()
        skills = skills_entry.get()
        interests = interests_entry.get()
        speech_style = speech_style_entry.get()
        
        if not (name and gender and age and relationship and hobbies and skills and interests and speech_style):
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
            "speech_style": speech_style,
            "personality": "未設定"  # 仮のデフォルト値
        }
        
        file_path = save_detailed_friend_profile(profile)
        if file_path:
            messagebox.showinfo("成功", "友達プロファイルが作成されました。")
            setup_window.destroy()

    setup_window = tk.Toplevel(root)
    setup_window.title("友達プロファイルの作成")

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

    tk.Button(setup_window, text="プロファイルを保存", command=save_profile).pack()

# メインウィンドウの設定
root = tk.Tk()
root.title("友達プロファイルクリエーター")

tk.Button(root, text="友達のプロファイルを作成", command=create_friend_profile).pack()

root.mainloop()
