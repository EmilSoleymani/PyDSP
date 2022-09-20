all: run

run: 
	python3 pydsp.py input.dat

static:
	mypy .

clean:
	rm *.pyc