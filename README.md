# Rise and Fall Civilizations at War Tools - DB Editor

![Python 3.13](https://img.shields.io/badge/Python-3.13-blue?logo=python\&logoColor=white)
![uv](https://img.shields.io/badge/Build-uv-orange?logo=astral-sh)

A lightweight tool for converting and editing `.dat` binary database files used in games. Easily transform `.dat` files to JSON and back, inspect object data, and make modifications in a user-friendly format.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/kotop21/RAF---DB-Editor.git
cd RAF---DB-Editor
```

### 2. Install **uv**

#### 🖥️ macOS / Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | less
```

#### 🪟 Windows

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | more"
```

### 3. Install Dependencies

```bash
uv sync
```

### 4. Activate Virtual Environment

```bash
source .venv/bin/activate
```

### 5. Run the Project

```bash
uv run main.py
```

---

## 🧰 Features

* Convert `.dat` files to `.json` for easy editing.
* Convert `.json` files back to `.dat`.
* Automatically detect and parse object structures.

---

## ⚠️ Notes

* Modifying **ID** or **Name** fields in JSON may cause the game to misread objects. Change them only if you know what you’re doing.
* When exporting to JSON, any existing file will be **overwritten**.

---

## 🧑‍💻 Requirements

* Python 3.10+
* [uv](https://docs.astral.sh/uv/)

Made with ❤️ by [kotop21](https://github.com/kotop21)
