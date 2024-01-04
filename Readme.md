## WIP integrate https://github.com/inorton/junit2html

### How to run E2E tests 
- `$ behave`

### How to run Unit tests 
- `$ python -m unittest tests.test_your_module1`

#### Convert Junit to HTML report based on `xml` files
- Install plugin (junit2html)[https://github.com/inorton/junit2html]
- `$ behave **/*.feature --junit` //Run tests
- `$ junit2html reports/*.xml --merge=merged_results.xml` // Merge all *.xml files in one
- `$ junit2html merged_results.xml --report-matrix=summary_report.html` // Generate HTML report
