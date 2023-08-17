<h1 align="center">Aegasis Python Assessment Test👋</h1>

## ✨ Demo

requirements & Instruction to this project can be find in [requirement](https://docs.google.com/document/d/1Klsh-Y5ZQcDnYDPzD9AHAgv0z_GNGBbTPRaK4BqaOeU/edit) document file.

<p align="center">
  <img width="700" align="center" src="https://user-images.githubusercontent.com/9840435/60266022-72a82400-98e7-11e9-9958-f9004c2f97e1.gif" alt="demo"/>
</p>

<div align="center">

### Cloning the repository

--> Clone the repository using the command below :
```bash
git clone https://github.com/usamahassan00015/ChatgptBotApi-Flask.git

```

--> Move into the directory where we have the project files : 
```bash
cd <project_name>

```

--> Create a virtual environment :
```bash
# Let's install virtualenv first
pip install virtualenv

# Then we create our virtual environment
virtualenv envname

```

--> Activate the virtual environment :
```bash
envname\scripts\activate

```

--> Install the requirements :
```bash
pip install -r requirements.txt

```
--> migrate sqlite database :
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

```



### Running the App

--> To run the App, we use :
```bash
python run.py

```

> ⚠ Then, the development server will be started at http://127.0.0.1:5000/




