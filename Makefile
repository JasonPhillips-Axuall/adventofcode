.PHONY: install test

default: test

test:
	coverage run --source ./2023/ --omit "*__init__*,*_ut.py,*/test*" -m pytest --junitxml=reports/junit/junit.xml

cov:
	coverage report && coverage xml
badge: test cov
		genbadge tests -o ./badges/test.svg && genbadge coverage -i ./coverage.xml -o ./badges/coverage.svg