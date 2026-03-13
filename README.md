# Workshop 1

Small Python exercise built around a string calculator.

## Run it

Create a virtual environment, install the test dependency, then run the code however you want to poke at it:

```bash
git clone https://github.com/vushauv/SE2-vushau-workshop2.git
cd SE2-vushau-workshop2
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```


## Run tests

With the virtual environment active:

```bash
python3 -m pytest
```

If you only want one file:

```bash
python3 -m pytest tests/test_string_calculator.py
```
