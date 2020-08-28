SHA := $(shell git rev-parse HEAD)

.PHONY: build push all

build:
	docker build -t mtik00/pyotp:latest -f ./pyotp.dockerfile .
	docker tag mtik00/pyotp:latest mtik00/pyotp:$(SHA)

push:
	docker push mtik00/pyotp:latest
	docker push mtik00/pyotp:$(SHA)

all : build push
