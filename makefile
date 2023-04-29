all:
	@ echo Choose a target!
	
install:
	@ pip install -r ./doc/requirements.txt

run:
	@ python3 main.py
