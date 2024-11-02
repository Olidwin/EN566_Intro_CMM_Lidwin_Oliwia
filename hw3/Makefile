PART := 1

.PHONY: all run clean

all: 
	python3 oscillator.py PART=${PART}
	python3 poisson.py PART=${PART}

oscillator:
	python3 oscillator.py PART=${WIDTH}

poisson:
	python3 poisson.py PART=${PART}

clean:
	@echo "Cleaning..."
	rm -f *.png