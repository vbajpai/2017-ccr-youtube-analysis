make:
	pip install -r requirements.txt

update:
	pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | \
	xargs pip install -U

run:
	jupyter notebook
