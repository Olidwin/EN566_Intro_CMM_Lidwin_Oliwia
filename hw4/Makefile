PART := 4

.PHONY: all run clean

all: 
	python3 diffusion.py PART=${PART}
	python3 gases.py PART=${PART}
	python3 rnumbers.py PART=${PART}
	python3 rwalk.py PART=${PART}

walk:
	python3 rwalk.py PART=${PART}
rnumbers:
	python3 rnumbers.py PART=${PART}
gases:
	python3 gases.py PART=${PART}
diffusion:
	python3 diffusion.py PART=${PART}
clean:
	@echo "Cleaning..."
	rm -f *.png