## Polars Date and Datetime Manipulation
## In both Dataframe API and SQL where possible.

This code base shows examples of doing a number of `date` and `datetime`
manipulations in Polars (Python).

The full blog post is here https://www.confessionsofadataguy.com/date-and-datetime-manipulation-in-polar/

- convert a string to a date
- convert a string to a datetime
- convert a date or datetime back to a string
- pull out year, month, and day from a date or datetime object.
- pull the quarter out of a date or datetime object.
- get the diff between two date or datetime objects.
- Add an arbitrary number of days to a date or datetime object.

- ## Run the code ...
- Build Docker image first `docker build . --tag=polarsdates`
- Run the code `docker-compose up test`
