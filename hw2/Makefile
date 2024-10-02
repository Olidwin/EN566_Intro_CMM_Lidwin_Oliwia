WIDTH := 10
THETA := 45

.PHONY: carbon golf

carbon:
	@echo "Plotting the carbon graph with $(WIDTH)"
	python3 carbon.py --plot=${WIDTH}

golf:
	@echo "Plotting the carbon graph with $(THETA)"
	python3 carbon.py --plot=${THETA}

clean:
	@echo "Cleaning..."
	rm -f *.png