

build:
	docker build -t worker-exam-reminder .

run: 
	docker run --rm --name worker-exam-reminder worker-exam-reminder

venv:
	python3 -m venv venv

