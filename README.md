# 🎓 Smart Attendance Portal

A production-grade, cloud-backed attendance management system built with Streamlit and Supabase. Designed for educators to manage classrooms and students to mark attendance — securely, reliably, and in real time.

---

## 🌟 Features

### 🧑‍🏫 Admin Panel
- **Classroom Management**: Create and delete classrooms with custom access codes
- **Attendance Gate Control**: Open and close attendance for any class with one click
- **Anti-Collision Guard**: Prevents multiple classes from being open simultaneously
- **Daily Limit Enforcement**: Set a cap on how many students can mark attendance per day
- **Live Analytics Dashboard**: Visual attendance breakdown per class with bar charts and pie charts
- **GitHub Integration**: Push attendance matrices directly to a GitHub repository as CSV files
- **Bulletproof Deletion**: Triple-confirmation system to prevent accidental class deletion

### 🎓 Student Panel
- **Open-Class Detection**: Only shows classes where attendance is currently active
- **Roll Number Locking**: Name is permanently locked to a roll number after first submission — preventing identity fraud
- **Duplicate Prevention**: Blocks a student from marking attendance twice on the same day
- **Attendance History**: Students can view their personal attendance matrix filtered by class and roll number

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | Streamlit 1.51 |
| **Database** | Supabase (PostgreSQL) |
| **Cloud Storage** | GitHub (via PyGitHub) |
| **Data Processing** | Pandas, Matplotlib |
| **Authentication** | Streamlit Secrets / `.env` |
| **Timezone** | `pytz` (America/Toronto) |
| **Language** | Python 3.12+ |

---

## 📁 Project Structure

```
Smart Attendance Portal with Supabase/
│
├── admin_main.py           # Admin entry point (Dashboard + Analytics)
├── student_main.py         # Student entry point (Mark + View Attendance)
│
├── Attendence/             # Core application package
│   ├── __init__.py
│   ├── admin.py            # Admin panel logic (classroom CRUD, GitHub push)
│   ├── student.py          # Student attendance submission logic
│   ├── attendance.py       # Student attendance viewing panel
│   ├── analytics.py        # Analytics dashboard (charts, filters, pivot tables)
│   ├── clients.py          # Supabase & GitHub client factory
│   ├── config.py           # get_env() — secrets/env fallback helper
│   ├── logger.py           # Centralized logging setup
│   └── utils.py            # Timezone utility (current_toronto_date)
│
├── .streamlit/
│   └── secrets.toml        # (gitignored) Streamlit Cloud secrets
│
├── .env                    # (gitignored) Local environment variables
├── requirements.txt        # Project dependencies
├── pyproject.toml          # Project metadata
└── .gitignore
```

---

## 🗄️ Database Schema (Supabase)

| Table | Purpose |
|---|---|
| `classroom_settings` | Stores class name, access code, daily limit, and open/closed status |
| `attendance` | Records each student's attendance entry with date |
| `roll_map` | Permanently locks a student's name to their roll number per class |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.12 or higher
- A [Supabase](https://supabase.com) account and project
- A GitHub Personal Access Token (for CSV push feature)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd "Smart Attendance Portal with Supabase"
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate       # Windows
   source .venv/bin/activate    # macOS / Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Create a `.env` file in the root directory:
   ```env
   SUPABASE_URL=your_supabase_project_url
   SUPABASE_KEY=your_supabase_anon_key
   GITHUB_TOKEN=your_github_personal_access_token
   GITHUB_REPO=your_username/your_repo_name
   ADMIN_USERNAME=your_admin_username
   ADMIN_PASSWORD=your_admin_password
   ```

   > **For Streamlit Cloud deployment**, add the same keys to `.streamlit/secrets.toml` instead.

5. **Run the Admin Dashboard**
   ```bash
   streamlit run admin_main.py
   ```

6. **Run the Student Portal**
   ```bash
   streamlit run student_main.py
   ```

   > Open your browser to `http://localhost:8501`

---

## 💡 How It Works

### Attendance Flow
```
Admin opens class → Student selects class → Enters roll number + name + code
→ System validates code ✅ → Checks duplicate ✅ → Checks daily limit ✅
→ Locks roll number to name → Inserts attendance record → ✅ Success
```

### GitHub Backup Flow
```
Admin clicks "Push to GitHub" → Pivot matrix built (P/A grid) →
GitHub checked for existing file → Updated or Created → CSV committed to repo
```

---

## 🔐 Security Design

- Admin credentials are stored only in environment variables / Streamlit secrets — never hardcoded
- `st.stop()` is used aggressively to prevent unauthorized UI rendering
- Classroom codes are stored in the database and compared server-side
- Roll number → Name mapping is locked after first submission (tamper-proof)

---

## 📊 Analytics Dashboard

The analytics panel (Admin only) provides:
- **Attendance Matrix**: Full pivot table (Student × Date) with P/A status
- **Top 30 Bar Chart**: Students ranked by attendance count
- **Attendance % per Student**: Auto-calculated and displayed in the matrix
- **Range Slider Filter**: Filter students by their attendance percentage
- **Pie Chart**: Overall class-wide Present vs. Absent breakdown
- **CSV Download**: One-click export of the full attendance matrix

---

## 🙏 Acknowledgments

- Built on [Supabase](https://supabase.com) — open source Firebase alternative
- UI powered by [Streamlit](https://streamlit.io)
- GitHub integration via [PyGitHub](https://github.com/PyGithub/PyGithub)

---

**Made with ❤️ for educators and students**
