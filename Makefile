build:
	@docker build . -t nlopez/astp:latest

push:
	@docker push nlopez/astp:latest
