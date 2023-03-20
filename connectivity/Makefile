build: clean
	pip freeze > requirements.txt
	python setup.py bdist_wheel
	pip wheel -r requirements.txt -w dist

clean:
	rm -rf build *.egg-info dist