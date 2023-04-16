scanned_dir:
	touch .env
	echo "SENSOR_DIR='$$(pwd)'" > src/.env

venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt

run: venv/bin/activate scanned_dir
	./venv/bin/python3 src/sensor.py

test: scanned_dir
	echo "Check config"
	./venv/bin/python3 src/config.py
	
clean:
	rm -rf __pycache__
	rm -rf venv