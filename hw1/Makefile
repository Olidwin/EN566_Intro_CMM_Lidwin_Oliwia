FXN := "cos,sin"   # Default functions to plot (can be changed on the command line)
TXT := "output.txt"  # Default file for writing/reading data
FMT := "jpeg"

.PHONY: plot write read clean

plot:
	@echo "Plotting functions: $(FXN)"
	python3 trigonometry.py --function=$(FXN) --print=$(FMT)

write:
	@echo "Writing data to file: $(TXT)"
	python3 trigonometry.py --function=$(FXN) --write=$(TXT) --print=$(FMT)

read:
	@echo "Reading data from file: $(TXT)"
	python3 trigonometry.py --read_from_file=$(TXT) --function=$(FXN) --print=$(FMT)

clean:
	@echo "Cleaning/removing files of plots"
	rm -f plot.* plot_from_file.* $(TXT)