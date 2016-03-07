.PHONY: clean build

clean:
	rm -rf ../static
	rm -f ../*.html

build:
	cp -r static ../
	python eval.py -d data.yaml -t ./ -r ../
