TODO: Reflect on what you learned this week and what is still unclear.

# for each column in your dataset:
    * Describe it by recording/measuring/graphing:
        - Name
        - What the column describes
        - How that data was measured
        - Is it continuous or categorical data? Continuous is [1, 2, 4.6, -5] and categorical is ["cat", "dog", "mouse", "dog" , "dog"]
        - If categorical:
            + do a df["column_name"].value_counts() and get an idea of the counts that you’ll be working with.
            + do a df["column_name"].value_counts().plot(kind="bar") to get an idea of the distribution of the counts
            + Check for things that you might need to fold into each other. Do you have entries for sydney and Syd and Sydney and SYD in your data? Should they really be the same thing?
            + What is the distribution shape of this graph?
        - If continuous:
            + do a df["column_name"].hist() to get an idea of what your numbers are and how they’re distributed.
            + Is it a time series? A time series is data that changes over time, like the temperature at my desk, or the number of cookies I have left in the packet. If it is a time series
                ~ do a df["column_name"].plot() to see the trends.
                ~ are there any periods of time that are missing data? E.g. did they turn it off over the weekends?
            + What’s the biggest value (max)?
            + What’s the smallest value (min)?
            + What’s the mean value (mean)?
            + What’s the median value (median)?
            + What’s the most common value (mode)?
        - make some general comments about this column, based on what we see.
    * make some general comments about the dataframe, based on what we see.