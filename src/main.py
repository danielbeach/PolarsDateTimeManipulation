import polars as pl


def main():
    # Setup base dataframe
    data = {"string_date": ['2023-10-01', '2023-10-02']}
    df = pl.DataFrame(data)
    print(df)

    # Convert string to date
    df_date = df.with_columns(dt = pl.col('string_date').str.to_datetime().cast(pl.Date))
    print(df_date)

    # Convert string to date with strptime
    df_date_str = df.with_columns(dt = pl.col('string_date').str.strptime(pl.Date))
    print(df_date_str)

    # try string to date with SQL
    ctx = pl.SQLContext(bugger=df)
    results = ctx.execute('SELECT *, CAST(string_date as DATE) as date FROM bugger',eager=True)
    print(results)

    # try again in SQL
    ctx = pl.SQLContext(bugger=df)
    results = ctx.execute('SELECT *, DATE(string_date) as dt FROM bugger',eager=True)
    print(results)

    # string to datetime
    df_datetime = df.with_columns(dt = pl.col('string_date').str.to_datetime().cast(pl.Datetime))
    print(df_datetime)

    #convert a date to a string
    df_date = df.with_columns(dt = pl.col('string_date').str.to_datetime().cast(pl.Date))
    df_string = df_date.with_columns(date_string = pl.col('dt').dt.strftime('%Y-%m-%d'))
    print(df_string)

    # pull the year, month, and day from a date column.
    date_parts_df = df_date.with_columns([
                                         pl.col('dt').dt.year().alias('year'),
                                         pl.col('dt').dt.month().alias('month'),
                                         pl.col('dt').dt.day().alias('day'),
                                          ])
    print(date_parts_df.drop(['string_date']))

    # add one day to a date
    date_parts_df = df_date.with_columns(date_add = pl.col("dt") + pl.duration(days=1))
    print(date_parts_df.drop(['string_date']))

    # difference bewteen two dates
    date_parts_df = df_date.with_columns(date_add = pl.col("dt") + pl.duration(days=1))
    date_parts_df = date_parts_df.with_columns(date_diff = pl.col("date_add") - pl.col("dt"))
    print(date_parts_df.drop(['string_date']))



if __name__ == '__main__':
    main()