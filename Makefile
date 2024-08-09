default:
	@cat Makefile

get_texts:
	wget https://www.gutenberg.org/cache/epub/17192/pg17192.txt
	wget https://www.gutenberg.org/cache/epub/932/pg932.txt
	wget https://www.gutenberg.org/cache/epub/1063/pg1063.txt
	wget https://www.gutenberg.org/cache/epub/51060/pg51060.txt
	wget https://www.gutenberg.org/cache/epub/10031/pg10031.txt
	wget https://www.gutenberg.org/cache/epub/1064/pg1064.txt
	wget https://www.gutenberg.org/cache/epub/10947/pg10947.txt
	wget https://www.gutenberg.org/cache/epub/32037/pg32037.txt
	wget https://www.gutenberg.org/cache/epub/2148/pg2148.txt
	wget https://www.gutenberg.org/cache/epub/2147/pg2147.txt

raven_line_count:
	@echo "line count in The Raven:"
	@wc -l pg17192.txt | cut -d' ' -f1

raven_word_count:
	@echo "word count in The Raven:"
	@wc -w pg17192.txt | cut -d' ' -f1


raven_counts:
	@echo "line count with 'raven':"
	@grep -c 'raven' pg17192.txt
	@echo "line count with 'Raven':" 
	@grep -c 'Raven' pg17192.txt
	@echo "line count with 'raven' or 'Raven':"
	@grep -ci 'raven' pg17192.txt

total_lines: 
	@echo "line count all files:"
	@wc -l *.txt | tail -n 1

total_words:
	@echo "word count all files:"
	@wc -w *.txt | tail -n 1

env:
	sudo apt-get update
	python3 -m venv env
	./env/bin/pip install --upgrade pip
	
update: env
	. ./env/bin/activate && pip install -r requirements.txt

clean:
	rm -rf env
format:
	./env/bin/black text_processing.py
	./env/bin/black test_text_processing.py

lint:
	./env/bin/pylint src/ffx3eb/*.py tests/*.py

lint_for_workflow: 
	pylint src/ffx3eb*py tests/*.py

tests: lint
	./env/bin/pytest tests/

tests_for_workflow: lint
	pytest tests/

