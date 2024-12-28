# GoodbyeSE

GoodbyeSE project for Introduction to Software Engineering course

## Installation

Download the app at https://github.com/nmddmn/GoodbyeSE.

For updates and more information visit [our github](https://github.com/nmddmn/GoodbyeSE).

## Usage

Window

``` powershell
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine")

set FLASK_APP=app

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

.venv\Scripts\activate

cd GoodbyeSE

flask run -p 8080
```

Linux

``` bash
export FLASK_APP=app

source .venv/bin/activate

cd GoodbyeSE

flask run -p 8080
```

## References

WIP