**RC Tools Backend**
===========================
REST API built with Flask microframework.

<details open="open">
  <summary>Table of Contents</summary>
  <ul>
    <li>
        <a href="#getting-started"> Getting Started</a>
    </li>
    <li>
        <a href="#notes">Notes</a>
    </li>
    <li>
        <a href="#progress">  In Progress </a>
    </li>
  </ul>
</details>

<span id="getting-started">**Getting Started**</span>
----------------------------

### Backend

Creates a virtual environment
```bash
python -m venv env
```

Activates the environment

windows
```bash
./env/Scripts/activate
```

linux / mac 
```bash
. env/bin/activate
```

Installing dependencies
```
pip install -r requirements.txt
```

Starts flask server
```
python ./app.py
```

<span id="notes">**Notes**</span>
--------
<hr>

> If you want to change the baudrate 
1. Copy and paste the .env.example file and rename it to .env. 
2. Change the BAUDRATE variable in .env

The backend start on port 5000


<span id="progress">**In Progress**</span>
--------
<hr>

* CORS
* Routes