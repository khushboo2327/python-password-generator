import customtkinter as ctk
import random
import string
import json
import os
from datetime import datetime

# ---------- CONFIGURATION ----------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("900x750")
app.title("🛡️ Ultimate Security Toolkit")

# Master Password for Manager
MASTER_PASSWORD = "admin123" 
DATA_FILE = "passwords_data.json"

# Color Definitions
COLOR_GENERATE = "#2CC985"  # Green
COLOR_CLEAR = "#E74C3C"     # Red
COLOR_REGEN = "#F39C12"     # Orange
COLOR_HOME = "#3498DB"      # Blue
COLOR_LOGIN = "#9B59B6"     # Purple

# ---------- MAIN FRAMES ----------
home_frame = ctk.CTkFrame(app)
password_frame = ctk.CTkFrame(app)
username_frame = ctk.CTkFrame(app)
strength_frame = ctk.CTkFrame(app)
manager_main_frame = ctk.CTkFrame(app)        # Manager Main (2 Options)
manager_generate_frame = ctk.CTkFrame(app)    # Manager Generate
manager_login_frame = ctk.CTkFrame(app)       # Manager Login Entry
manager_saved_frame = ctk.CTkFrame(app)       # Manager Saved Passwords
pin_frame = ctk.CTkFrame(app)

all_frames = [home_frame, password_frame, username_frame, strength_frame, 
              manager_main_frame, manager_generate_frame, manager_login_frame, 
              manager_saved_frame, pin_frame]

def hide_all_frames():
    for frame in all_frames:
        frame.pack_forget()

def show_home():
    hide_all_frames()
    home_frame.pack(fill="both", expand=True)

def show_password():
    hide_all_frames()
    password_frame.pack(fill="both", expand=True)

def show_username():
    hide_all_frames()
    username_frame.pack(fill="both", expand=True)

def show_strength():
    hide_all_frames()
    strength_frame.pack(fill="both", expand=True)

def show_pin():
    hide_all_frames()
    pin_frame.pack(fill="both", expand=True)

# ========== PASSWORD MANAGER FRAMES ==========

def show_manager_main():
    hide_all_frames()
    manager_main_frame.pack(fill="both", expand=True)

def show_manager_generate():
    hide_all_frames()
    manager_generate_frame.pack(fill="both", expand=True)

def show_manager_login():
    hide_all_frames()
    manager_login_frame.pack(fill="both", expand=True)

def show_manager_saved():
    hide_all_frames()
    manager_saved_frame.pack(fill="both", expand=True)

# ---------- HOME SCREEN ----------
title = ctk.CTkLabel(home_frame, text="🛡️ Security Toolkit", font=("Arial", 40, "bold"), text_color=COLOR_HOME)
title.pack(pady=40)

btn_style = {"height": 70, "corner_radius": 15, "font": ("Arial", 20, "bold")}

ctk.CTkButton(home_frame, text="🔐 Password Generator", command=show_password, fg_color=COLOR_GENERATE, **btn_style).pack(pady=15, padx=150, fill="x")
ctk.CTkButton(home_frame, text="👤 Username Generator", command=show_username, fg_color=COLOR_HOME, **btn_style).pack(pady=15, padx=150, fill="x")
ctk.CTkButton(home_frame, text="📊 Strength Analyzer", command=show_strength, fg_color=COLOR_REGEN, **btn_style).pack(pady=15, padx=150, fill="x")
ctk.CTkButton(home_frame, text="🗄️ Password Manager", command=show_manager_main, fg_color=COLOR_LOGIN, **btn_style).pack(pady=15, padx=150, fill="x")
ctk.CTkButton(home_frame, text="🔢 PIN / OTP Generator", command=show_pin, fg_color="#1ABC9C", **btn_style).pack(pady=15, padx=150, fill="x")

# ---------- 1. PASSWORD GENERATOR ----------
ctk.CTkButton(password_frame, text="← Home", command=show_home, fg_color=COLOR_HOME, height=50, font=("Arial", 18)).pack(anchor="w", padx=20, pady=20)
ctk.CTkLabel(password_frame, text="🔐 Password Generator", font=("Arial", 32, "bold"), text_color=COLOR_GENERATE).pack(pady=10)

input_frame = ctk.CTkFrame(password_frame, fg_color="transparent")
input_frame.pack(pady=10)

ctk.CTkLabel(input_frame, text="Username/Prefix:", font=("Arial", 18)).grid(row=0, column=0, padx=10, pady=5, sticky="e")
prefix_entry = ctk.CTkEntry(input_frame, placeholder_text="e.g. rahul", width=300, font=("Arial", 18))
prefix_entry.grid(row=0, column=1, padx=10, pady=5)

ctk.CTkLabel(input_frame, text="Length:", font=("Arial", 18)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
length_entry = ctk.CTkEntry(input_frame, placeholder_text="12", width=300, font=("Arial", 18))
length_entry.grid(row=1, column=1, padx=10, pady=5)

ctk.CTkLabel(input_frame, text="Count:", font=("Arial", 18)).grid(row=2, column=0, padx=10, pady=5, sticky="e")
count_entry = ctk.CTkEntry(input_frame, placeholder_text="5", width=300, font=("Arial", 18))
count_entry.grid(row=2, column=1, padx=10, pady=5)

opt_frame = ctk.CTkFrame(password_frame, fg_color="transparent")
opt_frame.pack()
letters_var = ctk.BooleanVar(value=True)
digits_var = ctk.BooleanVar(value=True)
symbols_var = ctk.BooleanVar(value=True)

ctk.CTkCheckBox(opt_frame, text="Letters (A-Z)", variable=letters_var, font=("Arial", 18)).pack(side="left", padx=15)
ctk.CTkCheckBox(opt_frame, text="Numbers (0-9)", variable=digits_var, font=("Arial", 18)).pack(side="left", padx=15)
ctk.CTkCheckBox(opt_frame, text="Symbols (!@#)", variable=symbols_var, font=("Arial", 18)).pack(side="left", padx=15)

result_box = ctk.CTkTextbox(password_frame, height=250, font=("Consolas", 18), text_color=COLOR_GENERATE)
result_box.pack(pady=20, padx=40, fill="both", expand=True)

action_frame = ctk.CTkFrame(password_frame, fg_color="transparent")
action_frame.pack(pady=10)

def clear_password():
    result_box.delete("0.0", "end")

def generate_password():
    clear_password()
    try:
        length = int(length_entry.get())
        count = int(count_entry.get())
        prefix = prefix_entry.get().strip()
    except ValueError:
        result_box.insert("end", "❌ Please enter valid numbers.\n")
        return

    chars = ""
    if letters_var.get(): chars += string.ascii_letters
    if digits_var.get(): chars += string.digits
    if symbols_var.get(): chars += "!@#$%^&*()"

    if not chars:
        result_box.insert("end", "❌ Select at least one character type.\n")
        return

    for i in range(count):
        core_pass = "".join(random.choice(chars) for _ in range(length))
        final_pass = f"{prefix}{core_pass}" if prefix else core_pass
        result_box.insert("end", f"{i+1}. {final_pass}\n")

ctk.CTkButton(action_frame, text="⚡ Generate", command=generate_password, fg_color=COLOR_GENERATE, height=50, width=200, font=("Arial", 18, "bold")).pack(side="left", padx=20)
ctk.CTkButton(action_frame, text="🔄 Regenerate", command=generate_password, fg_color=COLOR_REGEN, height=50, width=200, font=("Arial", 18, "bold")).pack(side="left", padx=20)
ctk.CTkButton(action_frame, text="🗑️ Clear", command=clear_password, fg_color=COLOR_CLEAR, height=50, width=200, font=("Arial", 18, "bold")).pack(side="left", padx=20)

# ---------- 2. USERNAME GENERATOR ----------
ctk.CTkButton(username_frame, text="← Home", command=show_home, fg_color=COLOR_HOME, height=50, font=("Arial", 18)).pack(anchor="w", padx=20, pady=20)
ctk.CTkLabel(username_frame, text="👤 Username Generator", font=("Arial", 32, "bold"), text_color=COLOR_HOME).pack(pady=10)

user_input_frame = ctk.CTkFrame(username_frame, fg_color="transparent")
user_input_frame.pack(pady=10)

ctk.CTkLabel(user_input_frame, text="Base Name:", font=("Arial", 18)).grid(row=0, column=0, padx=10, pady=5, sticky="e")
base_name_entry = ctk.CTkEntry(user_input_frame, placeholder_text="e.g. gamer", width=300, font=("Arial", 18))
base_name_entry.grid(row=0, column=1, padx=10, pady=5)

ctk.CTkLabel(user_input_frame, text="Count:", font=("Arial", 18)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
user_count_entry = ctk.CTkEntry(user_input_frame, placeholder_text="10", width=300, font=("Arial", 18))
user_count_entry.grid(row=1, column=1, padx=10, pady=5)

username_result = ctk.CTkTextbox(username_frame, height=250, font=("Consolas", 18), text_color=COLOR_HOME)
username_result.pack(pady=20, padx=40, fill="both", expand=True)

def clear_username():
    username_result.delete("0.0", "end")

def generate_username_logic():
    clear_username()
    try:
        count = int(user_count_entry.get())
        base = base_name_entry.get().strip()
        if not base: base = "user"
    except ValueError:
        username_result.insert("end", "❌ Invalid Count\n")
        return

    for i in range(count):
        suffix = random.randint(100, 9999)
        name = f"{base}_{suffix}"
        username_result.insert("end", name + "\n")

user_action_frame = ctk.CTkFrame(username_frame, fg_color="transparent")
user_action_frame.pack(pady=10)

ctk.CTkButton(user_action_frame, text="⚡ Generate", command=generate_username_logic, fg_color=COLOR_GENERATE, height=50, width=200, font=("Arial", 18, "bold")).pack(side="left", padx=20)
ctk.CTkButton(user_action_frame, text="🔄 Regenerate", command=generate_username_logic, fg_color=COLOR_REGEN, height=50, width=200, font=("Arial", 18, "bold")).pack(side="left", padx=20)
ctk.CTkButton(user_action_frame, text="🗑️ Clear", command=clear_username, fg_color=COLOR_CLEAR, height=50, width=200, font=("Arial", 18, "bold")).pack(side="left", padx=20)

# ---------- 3. PASSWORD STRENGTH ANALYZER ----------
ctk.CTkButton(strength_frame, text="← Home", command=show_home, fg_color=COLOR_HOME, height=50, font=("Arial", 18)).pack(anchor="w", padx=20, pady=20)
ctk.CTkLabel(strength_frame, text="📊 Strength Analyzer", font=("Arial", 32, "bold"), text_color=COLOR_REGEN).pack(pady=10)

analyze_entry = ctk.CTkEntry(strength_frame, placeholder_text="Enter Password to Check", show="*", height=50, font=("Arial", 20))
analyze_entry.pack(pady=20, padx=100, fill="x")

strength_result_label = ctk.CTkLabel(strength_frame, text="", font=("Arial", 28, "bold"))
strength_result_label.pack(pady=10)

time_result_label = ctk.CTkLabel(strength_frame, text="", font=("Arial", 18))
time_result_label.pack(pady=5)

suggestion_box = ctk.CTkTextbox(strength_frame, height=200, font=("Arial", 16))
suggestion_box.pack(pady=10, padx=40, fill="both")

def analyze_strength():
    pwd = analyze_entry.get()
    suggestion_box.delete("0.0", "end")
    
    score = 0
    suggestions = []

    if len(pwd) >= 8: score += 1
    else: suggestions.append("• Make password at least 8 characters long.")
    if len(pwd) >= 12: score += 1
    if any(c.islower() for c in pwd): score += 1
    else: suggestions.append("• Add lowercase letters.")
    if any(c.isupper() for c in pwd): score += 1
    else: suggestions.append("• Add uppercase letters.")
    if any(c.isdigit() for c in pwd): score += 1
    else: suggestions.append("• Add numbers.")
    if any(c in "!@#$%^&*" for c in pwd): score += 1
    else: suggestions.append("• Add special symbols (!@#$).")

    if score <= 2:
        strength = "Weak 🔴"
        color = COLOR_CLEAR
    elif score <= 4:
        strength = "Medium 🟠"
        color = COLOR_REGEN
    else:
        strength = "Strong 🟢"
        color = COLOR_GENERATE

    strength_result_label.configure(text=strength, text_color=color)

    pool = 0
    if any(c.islower() for c in pwd): pool += 26
    if any(c.isupper() for c in pwd): pool += 26
    if any(c.isdigit() for c in pwd): pool += 10
    if any(c in "!@#$%^&*" for c in pwd): pool += 10
    
    if pool > 0:
        combinations = pool ** len(pwd)
        seconds = combinations / 1000000000 
        if seconds < 60: time_str = f"{seconds:.2f} Seconds"
        elif seconds < 3600: time_str = f"{seconds/60:.2f} Minutes"
        elif seconds < 86400: time_str = f"{seconds/3600:.2f} Hours"
        else: time_str = "Years (Very Safe)"
        time_result_label.configure(text=f"⏳ Est. Crack Time: {time_str}", text_color=COLOR_HOME)
    else:
        time_result_label.configure(text="")

    if not suggestions:
        suggestion_box.insert("end", "✅ Great Password! No changes needed.")
    else:
        suggestion_box.insert("end", "💡 Suggestions to improve:\n")
        for s in suggestions:
            suggestion_box.insert("end", s + "\n")

ctk.CTkButton(strength_frame, text="🔍 Analyze", command=analyze_strength, fg_color=COLOR_REGEN, height=50, width=200, font=("Arial", 18, "bold")).pack(pady=10)

# ---------- 4. PIN GENERATOR ----------
ctk.CTkButton(pin_frame, text="← Home", command=show_home, fg_color=COLOR_HOME, height=50, font=("Arial", 18)).pack(anchor="w", padx=20, pady=20)
ctk.CTkLabel(pin_frame, text="🔢 PIN / OTP Generator", font=("Arial", 32, "bold"), text_color="#1ABC9C").pack(pady=10)

pin_var = ctk.StringVar(value="4")
ctk.CTkLabel(pin_frame, text="Select Length:", font=("Arial", 20)).pack()
pin_opt_frame = ctk.CTkFrame(pin_frame, fg_color="transparent")
pin_opt_frame.pack()
ctk.CTkRadioButton(pin_opt_frame, text="4 Digits (ATM)", variable=pin_var, value="4", font=("Arial", 18)).pack(side="left", padx=30)
ctk.CTkRadioButton(pin_opt_frame, text="6 Digits (OTP)", variable=pin_var, value="6", font=("Arial", 18)).pack(side="left", padx=30)

pin_result = ctk.CTkTextbox(pin_frame, height=150, font=("Consolas", 24), text_color=COLOR_CLEAR)
pin_result.pack(pady=20, padx=100, fill="x")

def clear_pin():
    pin_result.delete("0.0", "end")

def generate_pin_logic():
    clear_pin()
    length = int(pin_var.get())
    pin = "".join(random.choice(string.digits) for _ in range(length))
    pin_result.insert("end", f"🔑 {pin}\n")

pin_action_frame = ctk.CTkFrame(pin_frame, fg_color="transparent")
pin_action_frame.pack(pady=10)

ctk.CTkButton(pin_action_frame, text="⚡ Generate", command=generate_pin_logic, fg_color=COLOR_GENERATE, height=50, width=200, font=("Arial", 18, "bold")).pack(side="left", padx=20)
ctk.CTkButton(pin_action_frame, text="🔄 Regenerate", command=generate_pin_logic, fg_color=COLOR_REGEN, height=50, width=200, font=("Arial", 18, "bold")).pack(side="left", padx=20)
ctk.CTkButton(pin_action_frame, text="🗑️ Clear", command=clear_pin, fg_color=COLOR_CLEAR, height=50, width=200, font=("Arial", 18, "bold")).pack(side="left", padx=20)

# ========== 5. PASSWORD MANAGER (UPDATED WITH 2 OPTIONS) ==========

# --- Manager Main Frame (2 Options: Generate / Login) ---
ctk.CTkButton(manager_main_frame, text="← Home", command=show_home, fg_color="gray", height=40, font=("Arial", 16)).pack(anchor="w", padx=20, pady=20)
ctk.CTkLabel(manager_main_frame, text="🗄️ Password Manager", font=("Arial", 36, "bold"), text_color=COLOR_LOGIN).pack(pady=30)
ctk.CTkLabel(manager_main_frame, text="Select an Option", font=("Arial", 20), text_color="gray").pack(pady=10)

manager_btn_style = {"height": 80, "width": 350, "font": ("Arial", 22, "bold"), "corner_radius": 15}

ctk.CTkButton(manager_main_frame, text="🔓 Generate New Password", command=show_manager_generate, 
              fg_color=COLOR_GENERATE, **manager_btn_style).pack(pady=20)

ctk.CTkButton(manager_main_frame, text="🔐 Login to View Saved", command=show_manager_login, 
              fg_color=COLOR_LOGIN, **manager_btn_style).pack(pady=20)

# --- Manager Generate Frame ---
ctk.CTkButton(manager_generate_frame, text="← Back", command=show_manager_main, fg_color="gray", height=40, font=("Arial", 16)).pack(anchor="w", padx=20, pady=20)
ctk.CTkLabel(manager_generate_frame, text="🔓 Generate New Credentials", font=("Arial", 32, "bold"), text_color=COLOR_GENERATE).pack(pady=20)

gen_input_frame = ctk.CTkFrame(manager_generate_frame, fg_color="transparent")
gen_input_frame.pack(pady=10)

ctk.CTkLabel(gen_input_frame, text="Website/App:", font=("Arial", 18)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
gen_site_entry = ctk.CTkEntry(gen_input_frame, placeholder_text="e.g. Facebook", width=300, font=("Arial", 18))
gen_site_entry.grid(row=0, column=1, padx=10, pady=10)

ctk.CTkLabel(gen_input_frame, text="Username:", font=("Arial", 18)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
gen_user_entry = ctk.CTkEntry(gen_input_frame, placeholder_text="e.g. john@email.com", width=300, font=("Arial", 18))
gen_user_entry.grid(row=1, column=1, padx=10, pady=10)

ctk.CTkLabel(gen_input_frame, text="Password Length:", font=("Arial", 18)).grid(row=2, column=0, padx=10, pady=10, sticky="e")
gen_length_entry = ctk.CTkEntry(gen_input_frame, placeholder_text="12", width=300, font=("Arial", 18))
gen_length_entry.grid(row=2, column=1, padx=10, pady=10)

gen_result_frame = ctk.CTkFrame(manager_generate_frame, fg_color="#34495E")
gen_result_frame.pack(pady=20, padx=40, fill="x")

gen_site_label = ctk.CTkLabel(gen_result_frame, text="", font=("Arial", 18))
gen_site_label.pack(pady=5)
gen_user_label = ctk.CTkLabel(gen_result_frame, text="", font=("Arial", 18))
gen_user_label.pack(pady=5)
gen_pass_label = ctk.CTkLabel(gen_result_frame, text="", font=("Consolas", 20, "bold"), text_color=COLOR_GENERATE)
gen_pass_label.pack(pady=10)

def clear_manager_generate():
    gen_site_entry.delete(0, 'end')
    gen_user_entry.delete(0, 'end')
    gen_length_entry.delete(0, 'end')
    gen_site_label.configure(text="")
    gen_user_label.configure(text="")
    gen_pass_label.configure(text="")

def generate_manager_password():
    site = gen_site_entry.get().strip()
    username = gen_user_entry.get().strip()
    
    try:
        length = int(gen_length_entry.get())
    except ValueError:
        gen_pass_label.configure(text="❌ Invalid Length")
        return
    
    if not site or not username:
        gen_pass_label.configure(text="❌ Fill Site & Username")
        return
    
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = "".join(random.choice(chars) for _ in range(length))
    
    gen_site_label.configure(text=f"🌐 Site: {site}")
    gen_user_label.configure(text=f"👤 User: {username}")
    gen_pass_label.configure(text=f"🔑 Password: {password}")
    
    # Auto-save option
    save_frame = ctk.CTkFrame(manager_generate_frame, fg_color="transparent")
    save_frame.pack(pady=10)
    
    def save_this_password():
        data = load_data()
        data.append({"site": site, "user": username, "pass": password, "date": datetime.now().strftime("%Y-%m-%d")})
        save_data(data)
        ctk.CTkLabel(save_frame, text="✅ Saved Successfully!", text_color=COLOR_GENERATE, font=("Arial", 16)).pack()
    
    ctk.CTkButton(save_frame, text="💾 Save to Manager", command=save_this_password, 
                  fg_color=COLOR_LOGIN, height=40, font=("Arial", 16, "bold")).pack(side="left", padx=10)
    ctk.CTkButton(save_frame, text="🗑️ Clear", command=clear_manager_generate, 
                  fg_color=COLOR_CLEAR, height=40, font=("Arial", 16, "bold")).pack(side="left", padx=10)

gen_action_frame = ctk.CTkFrame(manager_generate_frame, fg_color="transparent")
gen_action_frame.pack(pady=10)

ctk.CTkButton(gen_action_frame, text="⚡ Generate", command=generate_manager_password, 
              fg_color=COLOR_GENERATE, height=50, width=200, font=("Arial", 18, "bold")).pack(side="left", padx=20)
ctk.CTkButton(gen_action_frame, text="🔄 Regenerate", command=generate_manager_password, 
              fg_color=COLOR_REGEN, height=50, width=200, font=("Arial", 18, "bold")).pack(side="left", padx=20)

# --- Manager Login Frame ---
ctk.CTkButton(manager_login_frame, text="← Back", command=show_manager_main, fg_color="gray", height=40, font=("Arial", 16)).pack(anchor="w", padx=20, pady=20)
ctk.CTkLabel(manager_login_frame, text="🔐 Master Password Login", font=("Arial", 32, "bold"), text_color=COLOR_LOGIN).pack(pady=50)
ctk.CTkLabel(manager_login_frame, text=f"(Demo: {MASTER_PASSWORD})", font=("Arial", 14), text_color="gray").pack()

master_entry = ctk.CTkEntry(manager_login_frame, placeholder_text="Enter Master Password", show="*", height=50, font=("Arial", 20), width=300)
master_entry.pack(pady=30)

login_status_label = ctk.CTkLabel(manager_login_frame, text="", font=("Arial", 16))
login_status_label.pack()

def check_master():
    if master_entry.get() == MASTER_PASSWORD:
        show_manager_saved()
    else:
        login_status_label.configure(text="❌ Wrong Password!", text_color=COLOR_CLEAR)

ctk.CTkButton(manager_login_frame, text="🔓 Login", command=check_master, fg_color=COLOR_LOGIN, height=50, width=200, font=("Arial", 18, "bold")).pack(pady=10)

# --- Manager Saved Passwords Frame ---
ctk.CTkButton(manager_saved_frame, text="← Logout", command=show_manager_login, fg_color="gray", height=40, font=("Arial", 16)).pack(anchor="w", padx=20, pady=20)
ctk.CTkLabel(manager_saved_frame, text="🗄️ Saved Passwords", font=("Arial", 32, "bold"), text_color=COLOR_LOGIN).pack(pady=10)

# Search
search_entry = ctk.CTkEntry(manager_saved_frame, placeholder_text="🔍 Search Site or User...", height=40, font=("Arial", 16))
search_entry.pack(pady=10, padx=40, fill="x")
search_entry.bind("<KeyRelease>", lambda e: refresh_saved_list())

# List Display
saved_list_frame = ctk.CTkScrollableFrame(manager_saved_frame)
saved_list_frame.pack(pady=10, padx=40, fill="both", expand=True)

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def copy_to_clipboard(text):
    app.clipboard_clear()
    app.clipboard_append(text)

def refresh_saved_list():
    for widget in saved_list_frame.winfo_children():
        widget.destroy()
    
    data = load_data()
    query = search_entry.get().lower()
    
    if not data:
        ctk.CTkLabel(saved_list_frame, text="📭 No passwords saved yet.", font=("Arial", 18)).pack(pady=20)
        return

    found = False
    for entry in data:
        if query in entry['site'].lower() or query in entry['user'].lower():
            found = True
            row = ctk.CTkFrame(saved_list_frame, fg_color="#34495E")
            row.pack(fill="x", pady=5, padx=5)
            
            ctk.CTkLabel(row, text=f"🌐 {entry['site']}", width=150, anchor="w", font=("Arial", 16, "bold"), text_color=COLOR_HOME).pack(side="left", padx=10)
            ctk.CTkLabel(row, text=f"👤 {entry['user']}", width=180, anchor="w", font=("Arial", 16), text_color="white").pack(side="left", padx=10)
            ctk.CTkLabel(row, text="🔑 ****", width=100, anchor="w", font=("Arial", 16), text_color=COLOR_CLEAR).pack(side="left", padx=10)
            
            ctk.CTkButton(row, text="📋 Copy", width=90, height=35, fg_color=COLOR_HOME, font=("Arial", 14, "bold"),
                          command=lambda p=entry['pass']: copy_to_clipboard(p)).pack(side="right", padx=5)
            
            ctk.CTkButton(row, text="🗑️", width=50, height=35, fg_color=COLOR_CLEAR, font=("Arial", 14, "bold"),
                          command=lambda s=entry['site'], u=entry['user']: delete_saved_entry(s, u)).pack(side="right", padx=2)
    
    if not found:
        ctk.CTkLabel(saved_list_frame, text="🔍 No results found.", font=("Arial", 18)).pack(pady=20)

def delete_saved_entry(site, user):
    data = load_data()
    data = [x for x in data if not (x['site'] == site and x['user'] == user)]
    save_data(data)
    refresh_saved_list()

refresh_saved_list()

# ---------- START APP ----------
show_home()
app.mainloop()
