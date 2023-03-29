test_code_standards:
	pylint ./src

unit_test_code:
	pytest --cov src