.PHONY: test

test:
	@echo "*** Running Python tests with pytest *** \n"
	@pytest ./tests

.PHONY: deploy-infrastructure 

deploy-infrastructure:
	@echo "*** Deploying terraform infrastructure ***"
	@cd infrastructure && terraform apply

.PHONY: build-parser-lambda

build-parser-lambda:
	@echo "*** Building parser lambda ***"
	@./scripts/build_parser_lambda.sh
