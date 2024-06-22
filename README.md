## How to set up Ogani

### Install Ogani from GitHub

```bash
git clone https://github.com/EduVector/ogani.git
```

### Open on VS Code

```bash
cd ogani && code .
```

### Create virtual environment

```bash
py -m venv venv
```

### Install Python libraries from requirements.txt

```bash
pip install -r requirements.txt
```

### Set migrations

```bash
py manage.py makemigrations
py manage.py migrate
```

### Create default Superuser of Django

```bash
py manage.py createsuperuser
```

### Run project on your localhost

```bash
py manage.py runserver
```
