# 🏡 **(Re)Selling Seattle: Determining House Sell Prices** 🏡

**Author**: Benjamin McCarty

---
</br></br>
**<p style="text-align: center;">If you are considering selling your house, one of the highest priorities is getting the best price for it.</p>**

You want to make sure that the hedges are trimmed; that the basement isn't leaking; and that new coat of paint is covering up all of the "art" covering the walls from your kids.

*But what else can do you?* Would that extra bathroom under the stairs be a worthwhile addition? What about that addition you always talked about building?

---
**<p style="text-align: center;">When you are exploring the option of selling, you may ask such questions as:</p>**

>* How do the different aspects of your house impact the price?
>
>
>* What can you do to improve the house's value?


---
You may have some ideas already (and if you don't, watch a few episodes of "This Old House" and you will have *plenty* of inspiration).

But how do you *really* know what features are best? How can you be sure that your intuition or expectations are based on fact and not assumptions? **Turn to the data for answers!**

---
**<p style="text-align: center;">Revisiting King County</p>**

My [prior exploration](https://github.com/BenJMcCarty/Phase_2_Project_Final) of the King County House Sales dataset yielded some recommendations, but I wanted to see if I can improve them. I am revisiting the data with new techniques and approaches to see how much I can improve the results.

---
</br></br>

# 📋 **The Process**

**<p style="text-align: center;">This project uses data from house sales in King County, WA. to determine the impact of different features on determining the sell price of a home.</p>**

</br></br>

>* **First, I explored the data using Pandas.** I reviewed the different features included in my dataset and their respective values; the descriptive statistics for the numerical data; and the overall size and shape of the data (how many rows and columns).
>
>
>* **Then, I used Seaborn to plot the data and a fitted linear regression model for each feature against the sell price.** These visualizations helped differentiate which features to treat as *categorical* variables (e.g. features that would be one of a select number of options) versus *continuous* variables (which would have a range of values).
>
>
>* **In order to give more depth to my data, I engineered six new features based on the original features and data.** I determined the age of each house at sale; whether or not a home was renovated; how many years since a renovation; and whether or not a house had a basement.
>
>
>* **I wanted to make sure all of the features and their data were relevant to apply to my future model.** I performed correlational comparisons to determine which features were too closely related (indicating multicollinearity), which would affect my modeling process later on.

</br>

**Once my data was cleaned and prepared, I started the modeling process.**

</br>

>  * I started off with a baseline model created using the average price. It provided me with the baseline RMSE with which I could compare additional models.
>
>
>  * For further processing, I created a simple ColumnTransformer to process missing values and to perform encoding of my categorical variables for modeling.
>
>
>  * Next, I created a Statsmodels version of a linear regression model. I am most familiar with this method of creating linear regression models and used it to generate an $r^2$ value against which to compare my next models.
>
>
>  * I fully crafted my pipeline by combining my preprocessor transformer and a linear regression model class from the Scikit-Learn package. Using this pipeline was a new approach for me, and so I kept it simple and didn't add additional processing before the model.
>
>
>  * For comparison purposes, I created a second pipeline containing a scaler for my input data. The scaling did not impact my $r^2$ or RMSE, but it did shuffle around the rankings for my top positive coefficients for determining price. In the end, though, I felt the data was too hard to explain to my homeowners. I decided to use my non-scaled data for my presentation and recommendations.
>
>
> **After creating my model, I generated predictions for new housing data.** For my predictions, I performed the same transformations to my data as before, minus the train/test split. After transforming the data, I utilized my trained pipeline to produce my final predictions for submission.

</br></br>

# 💡 **Recommendations**

</br>

> **Based on my model's results,** I would make the following recommendations to a homeowner interested in renovating to ***increase*** the sell price of their home (*all changes in price assume no other changes to the house*):
>
> * **Add another bathroom** - Adding another bathroom would increase the price by \\$23,452.61.
>
>
> * **Increase the above-ground square-footage of the house** -  the price increases by \\$153.15 for each additional square foot.
>
>
> * **Increase the square-footage of the basement** -  the price increases by \\$112.64 for each additional square foot.
>
>---
> **Furthermore,** I would advise homeowners ***not*** to make the following changes as they *decrease* the price (*all changes in price assume no other changes to the house*):
>
> * **Adding another floor** decreases price by \\$24,944.90 - quite a hit considering the potential construction costs of that extra level!
>
>
> * **Building a bedroom** decreases price by \\$11,372.35 - assuming you don't add more square footage to the house, building an extra bedroom would take away from the pre-existing space - a home needs more rooms than just bedrooms!

</br></br>


# 🔬 **Exploring Fresh Data**

## Basic Overviews

After importing the data, I start with a basic overview of the data via a Pandas DataFrame. The DataFrame shows the columns; select rows; and the size at the bottom.

After the initial review, I use one of my hand-crafted functions to add to the normal DataFrame.describe() function, including reviewing each column's datatype; unique values; and the null values for each column. I use this information for data cleaning in the next section.
</br></br></br>

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>bedrooms</th>
      <th>bathrooms</th>
      <th>sqft_living</th>
      <th>sqft_lot</th>
      <th>floors</th>
      <th>waterfront</th>
      <th>view</th>
      <th>condition</th>
      <th>grade</th>
      <th>sqft_above</th>
      <th>sqft_basement</th>
      <th>yr_built</th>
      <th>yr_renovated</th>
      <th>zipcode</th>
      <th>lat</th>
      <th>long</th>
      <th>sqft_living15</th>
      <th>sqft_lot15</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3/4/2015</td>
      <td>3</td>
      <td>2.50</td>
      <td>1880</td>
      <td>4499</td>
      <td>2.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>3</td>
      <td>8</td>
      <td>1880</td>
      <td>0.0</td>
      <td>1993</td>
      <td>0.00</td>
      <td>98029</td>
      <td>47.57</td>
      <td>-122.00</td>
      <td>2130</td>
      <td>5114</td>
      <td>529,000.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10/7/2014</td>
      <td>3</td>
      <td>2.50</td>
      <td>2020</td>
      <td>6564</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>3</td>
      <td>7</td>
      <td>1310</td>
      <td>710.0</td>
      <td>1994</td>
      <td>0.00</td>
      <td>98042</td>
      <td>47.35</td>
      <td>-122.16</td>
      <td>1710</td>
      <td>5151</td>
      <td>253,000.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/16/2015</td>
      <td>5</td>
      <td>4.00</td>
      <td>4720</td>
      <td>493534</td>
      <td>2.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>5</td>
      <td>9</td>
      <td>3960</td>
      <td>760.0</td>
      <td>1975</td>
      <td>0.00</td>
      <td>98027</td>
      <td>47.45</td>
      <td>-122.01</td>
      <td>2160</td>
      <td>219542</td>
      <td>745,000.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3/30/2015</td>
      <td>2</td>
      <td>2.00</td>
      <td>1430</td>
      <td>3880</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4</td>
      <td>7</td>
      <td>1430</td>
      <td>0.0</td>
      <td>1949</td>
      <td>0.00</td>
      <td>98117</td>
      <td>47.68</td>
      <td>-122.39</td>
      <td>1430</td>
      <td>3880</td>
      <td>545,000.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>10/14/2014</td>
      <td>3</td>
      <td>2.25</td>
      <td>2270</td>
      <td>32112</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4</td>
      <td>8</td>
      <td>1740</td>
      <td>530.0</td>
      <td>1980</td>
      <td>0.00</td>
      <td>98042</td>
      <td>47.35</td>
      <td>-122.09</td>
      <td>2310</td>
      <td>41606</td>
      <td>390,000.00</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>16192</th>
      <td>9/15/2014</td>
      <td>3</td>
      <td>2.50</td>
      <td>2230</td>
      <td>5800</td>
      <td>2.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>3</td>
      <td>7</td>
      <td>2230</td>
      <td>0.0</td>
      <td>2004</td>
      <td>0.00</td>
      <td>98065</td>
      <td>47.53</td>
      <td>-121.85</td>
      <td>2230</td>
      <td>6088</td>
      <td>440,000.00</td>
    </tr>
    <tr>
      <th>16193</th>
      <td>10/2/2014</td>
      <td>4</td>
      <td>2.75</td>
      <td>2770</td>
      <td>3852</td>
      <td>2.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>3</td>
      <td>8</td>
      <td>2770</td>
      <td>0.0</td>
      <td>2014</td>
      <td>nan</td>
      <td>98178</td>
      <td>47.50</td>
      <td>-122.23</td>
      <td>1810</td>
      <td>5641</td>
      <td>572,000.00</td>
    </tr>
    <tr>
      <th>16194</th>
      <td>7/21/2014</td>
      <td>4</td>
      <td>1.50</td>
      <td>1530</td>
      <td>9000</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4</td>
      <td>6</td>
      <td>1530</td>
      <td>0.0</td>
      <td>1976</td>
      <td>0.00</td>
      <td>98014</td>
      <td>47.65</td>
      <td>-121.91</td>
      <td>1520</td>
      <td>8500</td>
      <td>299,800.00</td>
    </tr>
    <tr>
      <th>16195</th>
      <td>6/20/2014</td>
      <td>1</td>
      <td>0.75</td>
      <td>380</td>
      <td>15000</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>3</td>
      <td>5</td>
      <td>380</td>
      <td>0.0</td>
      <td>1963</td>
      <td>0.00</td>
      <td>98168</td>
      <td>47.48</td>
      <td>-122.32</td>
      <td>1170</td>
      <td>15000</td>
      <td>245,000.00</td>
    </tr>
    <tr>
      <th>16196</th>
      <td>3/25/2015</td>
      <td>4</td>
      <td>2.50</td>
      <td>2755</td>
      <td>11612</td>
      <td>2.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>3</td>
      <td>8</td>
      <td>2755</td>
      <td>0.0</td>
      <td>2001</td>
      <td>0.00</td>
      <td>98019</td>
      <td>47.74</td>
      <td>-121.97</td>
      <td>2820</td>
      <td>12831</td>
      <td>545,000.00</td>
    </tr>
  </tbody>
</table>
<p>16197 rows × 20 columns</p>
</div>

</br></br>

```python
## Review summary of dataframe details
report_df(df)
```

    (16197, 20)
    

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>datatypes</th>
      <th>num_unique</th>
      <th>null_sum</th>
      <th>null_pct</th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>date</th>
      <td>object</td>
      <td>366</td>
      <td>0</td>
      <td>0.00</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
    </tr>
    <tr>
      <th>bedrooms</th>
      <td>int64</td>
      <td>11</td>
      <td>0</td>
      <td>0.00</td>
      <td>16,197.00</td>
      <td>3.37</td>
      <td>0.91</td>
      <td>1.00</td>
      <td>3.00</td>
      <td>3.00</td>
      <td>4.00</td>
      <td>11.00</td>
    </tr>
    <tr>
      <th>bathrooms</th>
      <td>float64</td>
      <td>26</td>
      <td>0</td>
      <td>0.00</td>
      <td>16,197.00</td>
      <td>2.12</td>
      <td>0.77</td>
      <td>0.50</td>
      <td>1.75</td>
      <td>2.25</td>
      <td>2.50</td>
      <td>8.00</td>
    </tr>
    <tr>
      <th>sqft_living</th>
      <td>int64</td>
      <td>896</td>
      <td>0</td>
      <td>0.00</td>
      <td>16,197.00</td>
      <td>2,083.69</td>
      <td>918.21</td>
      <td>370.00</td>
      <td>1,430.00</td>
      <td>1,912.00</td>
      <td>2,560.00</td>
      <td>13,540.00</td>
    </tr>
    <tr>
      <th>sqft_lot</th>
      <td>int64</td>
      <td>8015</td>
      <td>0</td>
      <td>0.00</td>
      <td>16,197.00</td>
      <td>15,071.89</td>
      <td>40,775.85</td>
      <td>520.00</td>
      <td>5,058.00</td>
      <td>7,620.00</td>
      <td>10,720.00</td>
      <td>1,651,359.00</td>
    </tr>
    <tr>
      <th>floors</th>
      <td>float64</td>
      <td>6</td>
      <td>0</td>
      <td>0.00</td>
      <td>16,197.00</td>
      <td>1.49</td>
      <td>0.54</td>
      <td>1.00</td>
      <td>1.00</td>
      <td>1.50</td>
      <td>2.00</td>
      <td>3.50</td>
    </tr>
    <tr>
      <th>waterfront</th>
      <td>float64</td>
      <td>2</td>
      <td>1756</td>
      <td>0.11</td>
      <td>14,441.00</td>
      <td>0.01</td>
      <td>0.09</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
    </tr>
    <tr>
      <th>view</th>
      <td>float64</td>
      <td>5</td>
      <td>49</td>
      <td>0.00</td>
      <td>16,148.00</td>
      <td>0.23</td>
      <td>0.77</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4.00</td>
    </tr>
    <tr>
      <th>condition</th>
      <td>int64</td>
      <td>5</td>
      <td>0</td>
      <td>0.00</td>
      <td>16,197.00</td>
      <td>3.41</td>
      <td>0.65</td>
      <td>1.00</td>
      <td>3.00</td>
      <td>3.00</td>
      <td>4.00</td>
      <td>5.00</td>
    </tr>
    <tr>
      <th>grade</th>
      <td>int64</td>
      <td>11</td>
      <td>0</td>
      <td>0.00</td>
      <td>16,197.00</td>
      <td>7.66</td>
      <td>1.17</td>
      <td>3.00</td>
      <td>7.00</td>
      <td>7.00</td>
      <td>8.00</td>
      <td>13.00</td>
    </tr>
    <tr>
      <th>sqft_above</th>
      <td>int64</td>
      <td>814</td>
      <td>0</td>
      <td>0.00</td>
      <td>16,197.00</td>
      <td>1,790.47</td>
      <td>827.60</td>
      <td>370.00</td>
      <td>1,200.00</td>
      <td>1,560.00</td>
      <td>2,220.00</td>
      <td>9,410.00</td>
    </tr>
    <tr>
      <th>sqft_basement</th>
      <td>object</td>
      <td>280</td>
      <td>0</td>
      <td>0.00</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
    </tr>
    <tr>
      <th>yr_built</th>
      <td>int64</td>
      <td>116</td>
      <td>0</td>
      <td>0.00</td>
      <td>16,197.00</td>
      <td>1,971.02</td>
      <td>29.33</td>
      <td>1,900.00</td>
      <td>1,952.00</td>
      <td>1,975.00</td>
      <td>1,997.00</td>
      <td>2,015.00</td>
    </tr>
    <tr>
      <th>yr_renovated</th>
      <td>float64</td>
      <td>66</td>
      <td>2879</td>
      <td>0.18</td>
      <td>13,318.00</td>
      <td>81.99</td>
      <td>396.21</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>2,015.00</td>
    </tr>
    <tr>
      <th>zipcode</th>
      <td>int64</td>
      <td>70</td>
      <td>0</td>
      <td>0.00</td>
      <td>16,197.00</td>
      <td>98,078.10</td>
      <td>53.49</td>
      <td>98,001.00</td>
      <td>98,033.00</td>
      <td>98,065.00</td>
      <td>98,117.00</td>
      <td>98,199.00</td>
    </tr>
    <tr>
      <th>lat</th>
      <td>float64</td>
      <td>4783</td>
      <td>0</td>
      <td>0.00</td>
      <td>16,197.00</td>
      <td>47.56</td>
      <td>0.14</td>
      <td>47.16</td>
      <td>47.47</td>
      <td>47.57</td>
      <td>47.68</td>
      <td>47.78</td>
    </tr>
    <tr>
      <th>long</th>
      <td>float64</td>
      <td>720</td>
      <td>0</td>
      <td>0.00</td>
      <td>16,197.00</td>
      <td>-122.21</td>
      <td>0.14</td>
      <td>-122.52</td>
      <td>-122.33</td>
      <td>-122.23</td>
      <td>-122.12</td>
      <td>-121.31</td>
    </tr>
    <tr>
      <th>sqft_living15</th>
      <td>int64</td>
      <td>691</td>
      <td>0</td>
      <td>0.00</td>
      <td>16,197.00</td>
      <td>1,987.81</td>
      <td>685.19</td>
      <td>399.00</td>
      <td>1,490.00</td>
      <td>1,840.00</td>
      <td>2,360.00</td>
      <td>6,210.00</td>
    </tr>
    <tr>
      <th>sqft_lot15</th>
      <td>int64</td>
      <td>7230</td>
      <td>0</td>
      <td>0.00</td>
      <td>16,197.00</td>
      <td>12,784.07</td>
      <td>26,833.38</td>
      <td>651.00</td>
      <td>5,100.00</td>
      <td>7,620.00</td>
      <td>10,086.00</td>
      <td>871,200.00</td>
    </tr>
    <tr>
      <th>price</th>
      <td>float64</td>
      <td>3089</td>
      <td>0</td>
      <td>0.00</td>
      <td>16,197.00</td>
      <td>541,284.46</td>
      <td>366,344.75</td>
      <td>78,000.00</td>
      <td>323,500.00</td>
      <td>450,000.00</td>
      <td>645,000.00</td>
      <td>7,700,000.00</td>
    </tr>
  </tbody>
</table>
</div>

</br></br>

## Data Cleaning and Processing

For cleaning and processing, I converted the 'date' field to the datetime datatype: "sqft_basement" to the float datatype; and I chose to fill missing values with zeroes to allow for feature engineering and modeling later in the notebook.

</br>

```python
## Converting 'date' column to datetime

df['date'] = pd.to_datetime(df['date'])
df['date']
```




    0       2015-03-04
    1       2014-10-07
    2       2015-01-16
    3       2015-03-30
    4       2014-10-14
               ...    
    16192   2014-09-15
    16193   2014-10-02
    16194   2014-07-21
    16195   2014-06-20
    16196   2015-03-25
    Name: date, Length: 16197, dtype: datetime64[ns]




```python
## Converting 'sqft_basement' to numeric and filling any null values with zero

df['sqft_basement'] = pd.to_numeric(df['sqft_basement'], errors='coerce')
df['sqft_basement']
```




    0         0.00
    1       710.00
    2       760.00
    3         0.00
    4       530.00
             ...  
    16192     0.00
    16193     0.00
    16194     0.00
    16195     0.00
    16196     0.00
    Name: sqft_basement, Length: 16197, dtype: float64




```python
df.isna().sum()
```




    date                0
    bedrooms            0
    bathrooms           0
    sqft_living         0
    sqft_lot            0
    floors              0
    waterfront       1756
    view               49
    condition           0
    grade               0
    sqft_above          0
    sqft_basement     340
    yr_built            0
    yr_renovated     2879
    zipcode             0
    lat                 0
    long                0
    sqft_living15       0
    sqft_lot15          0
    price               0
    dtype: int64




```python
##Filling null values with the most frequent value

for col in df:
    if df[col].isna().sum() > 0:
        df[col].fillna(0, inplace=True)
```


```python
## Reviewing dataframe post-fill

report_df(df)
```

    (16197, 20)
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>datatypes</th>
      <th>num_unique</th>
      <th>null_sum</th>
      <th>null_pct</th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>date</th>
      <td>datetime64[ns]</td>
      <td>366</td>
      <td>0</td>
      <td>0.00</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
    </tr>
    <tr>
      <th>bedrooms</th>
      <td>int64</td>
      <td>11</td>
      <td>0</td>
      <td>0.00</td>
      <td>16,197.00</td>
      <td>3.37</td>
      <td>0.91</td>
      <td>1.00</td>
      <td>3.00</td>
      <td>3.00</td>
      <td>4.00</td>
      <td>11.00</td>
    </tr>
    <tr>
      <th>bathrooms</th>
      <td>float64</td>
      <td>26</td>
      <td>0</td>
      <td>0.00</td>
      <td>16,197.00</td>
      <td>2.12</td>
      <td>0.77</td>
      <td>0.50</td>
      <td>1.75</td>
      <td>2.25</td>
      <td>2.50</td>
      <td>8.00</td>
    </tr>
    <tr>
      <th>sqft_living</th>
      <td>int64</td>
      <td>896</td>
      <td>0</td>
      <td>0.00</td>
      <td>16,197.00</td>
      <td>2,083.69</td>
      <td>918.21</td>
      <td>370.00</td>
      <td>1,430.00</td>
      <td>1,912.00</td>
      <td>2,560.00</td>
      <td>13,540.00</td>
    </tr>
    <tr>
      <th>sqft_lot</th>
      <td>int64</td>
      <td>8015</td>
      <td>0</td>
      <td>0.00</td>
      <td>16,197.00</td>
      <td>15,071.89</td>
      <td>40,775.85</td>
      <td>520.00</td>
      <td>5,058.00</td>
      <td>7,620.00</td>
      <td>10,720.00</td>
      <td>1,651,359.00</td>
    </tr>
    <tr>
      <th>floors</th>
      <td>float64</td>
      <td>6</td>
      <td>0</td>
      <td>0.00</td>
      <td>16,197.00</td>
      <td>1.49</td>
      <td>0.54</td>
      <td>1.00</td>
      <td>1.00</td>
      <td>1.50</td>
      <td>2.00</td>
      <td>3.50</td>
    </tr>
    <tr>
      <th>waterfront</th>
      <td>float64</td>
      <td>2</td>
      <td>0</td>
      <td>0.00</td>
      <td>16,197.00</td>
      <td>0.01</td>
      <td>0.08</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
    </tr>
    <tr>
      <th>view</th>
      <td>float64</td>
      <td>5</td>
      <td>0</td>
      <td>0.00</td>
      <td>16,197.00</td>
      <td>0.23</td>
      <td>0.77</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4.00</td>
    </tr>
    <tr>
      <th>condition</th>
      <td>int64</td>
      <td>5</td>
      <td>0</td>
      <td>0.00</td>
      <td>16,197.00</td>
      <td>3.41</td>
      <td>0.65</td>
      <td>1.00</td>
      <td>3.00</td>
      <td>3.00</td>
      <td>4.00</td>
      <td>5.00</td>
    </tr>
    <tr>
      <th>grade</th>
      <td>int64</td>
      <td>11</td>
      <td>0</td>
      <td>0.00</td>
      <td>16,197.00</td>
      <td>7.66</td>
      <td>1.17</td>
      <td>3.00</td>
      <td>7.00</td>
      <td>7.00</td>
      <td>8.00</td>
      <td>13.00</td>
    </tr>
    <tr>
      <th>sqft_above</th>
      <td>int64</td>
      <td>814</td>
      <td>0</td>
      <td>0.00</td>
      <td>16,197.00</td>
      <td>1,790.47</td>
      <td>827.60</td>
      <td>370.00</td>
      <td>1,200.00</td>
      <td>1,560.00</td>
      <td>2,220.00</td>
      <td>9,410.00</td>
    </tr>
    <tr>
      <th>sqft_basement</th>
      <td>float64</td>
      <td>279</td>
      <td>0</td>
      <td>0.00</td>
      <td>16,197.00</td>
      <td>287.66</td>
      <td>440.73</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>550.00</td>
      <td>4,820.00</td>
    </tr>
    <tr>
      <th>yr_built</th>
      <td>int64</td>
      <td>116</td>
      <td>0</td>
      <td>0.00</td>
      <td>16,197.00</td>
      <td>1,971.02</td>
      <td>29.33</td>
      <td>1,900.00</td>
      <td>1,952.00</td>
      <td>1,975.00</td>
      <td>1,997.00</td>
      <td>2,015.00</td>
    </tr>
    <tr>
      <th>yr_renovated</th>
      <td>float64</td>
      <td>66</td>
      <td>0</td>
      <td>0.00</td>
      <td>16,197.00</td>
      <td>67.42</td>
      <td>360.64</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>2,015.00</td>
    </tr>
    <tr>
      <th>zipcode</th>
      <td>int64</td>
      <td>70</td>
      <td>0</td>
      <td>0.00</td>
      <td>16,197.00</td>
      <td>98,078.10</td>
      <td>53.49</td>
      <td>98,001.00</td>
      <td>98,033.00</td>
      <td>98,065.00</td>
      <td>98,117.00</td>
      <td>98,199.00</td>
    </tr>
    <tr>
      <th>lat</th>
      <td>float64</td>
      <td>4783</td>
      <td>0</td>
      <td>0.00</td>
      <td>16,197.00</td>
      <td>47.56</td>
      <td>0.14</td>
      <td>47.16</td>
      <td>47.47</td>
      <td>47.57</td>
      <td>47.68</td>
      <td>47.78</td>
    </tr>
    <tr>
      <th>long</th>
      <td>float64</td>
      <td>720</td>
      <td>0</td>
      <td>0.00</td>
      <td>16,197.00</td>
      <td>-122.21</td>
      <td>0.14</td>
      <td>-122.52</td>
      <td>-122.33</td>
      <td>-122.23</td>
      <td>-122.12</td>
      <td>-121.31</td>
    </tr>
    <tr>
      <th>sqft_living15</th>
      <td>int64</td>
      <td>691</td>
      <td>0</td>
      <td>0.00</td>
      <td>16,197.00</td>
      <td>1,987.81</td>
      <td>685.19</td>
      <td>399.00</td>
      <td>1,490.00</td>
      <td>1,840.00</td>
      <td>2,360.00</td>
      <td>6,210.00</td>
    </tr>
    <tr>
      <th>sqft_lot15</th>
      <td>int64</td>
      <td>7230</td>
      <td>0</td>
      <td>0.00</td>
      <td>16,197.00</td>
      <td>12,784.07</td>
      <td>26,833.38</td>
      <td>651.00</td>
      <td>5,100.00</td>
      <td>7,620.00</td>
      <td>10,086.00</td>
      <td>871,200.00</td>
    </tr>
    <tr>
      <th>price</th>
      <td>float64</td>
      <td>3089</td>
      <td>0</td>
      <td>0.00</td>
      <td>16,197.00</td>
      <td>541,284.46</td>
      <td>366,344.75</td>
      <td>78,000.00</td>
      <td>323,500.00</td>
      <td>450,000.00</td>
      <td>645,000.00</td>
      <td>7,700,000.00</td>
    </tr>
  </tbody>
</table>
</div>

</br></br>

### Overview Summary

The dataset contains 20 columns of data, most of which seem useful for evaluations and modeling. I manually fixed null values at this stage - I will start the pipeline later on. After processing, I do not have any null values and all of the datatypes are correct.

</br>

# Exploring Features<a name='features'></a>

In this stage of the notebook, I procedurally reviewed each feature in the dataset. I produced a regression plot and histogram via Seaborn for each feature, the used the visualizations to determine whether or not to use each feature as a categorical or continuous variable.

</br>

***Details and the visualizations are available in the Jupyter notebook.***

</br></br>
# 🛠 **Feature Engineering**

## `'yrs_old_sold'`

I create this feature to differentiate between houses that were built recently versus older houses.

In order to determine this feature, I need to determine the year the house was sold first.

</br>

### Determine `'year_sold'`

</br>

```python
## Pull the year from the "date" column
df['year_sold'] = pd.DatetimeIndex(df['date']).year

## Review the values to ensure data integrity
df['year_sold'].value_counts()
```




    2014    10974
    2015     5223
    Name: year_sold, dtype: int64



### Calculate `'yr_old_sold'`


```python
## Calculating the age of the house at the time of sale
df['yr_old_sold'] = df['year_sold'] - df['yr_built']

## Minimum age is -1 due to a house being sold before it was finished being built
display(df['yr_old_sold'].value_counts().sort_index(), df['yr_old_sold'].describe())
```


    -1       10
     0      312
     1      208
     2      128
     3      124
           ... 
     111     41
     112     21
     113     21
     114     51
     115     19
    Name: yr_old_sold, Length: 117, dtype: int64



    count   16,197.00
    mean        43.30
    std         29.33
    min         -1.00
    25%         18.00
    50%         40.00
    75%         63.00
    max        115.00
    Name: yr_old_sold, dtype: float64


>**Results:** Half of the homes sold fall between the ages of 18 and 63 years old, with the average age of 43 years. Our min and max ages indicate a house was sold before it was built, while another house was 115 years old.

</br>

## `'was_renovated'`

What impact would a renovation have on the price?
</br>
</br>

```python
## Using the year that the home was renovated to deterine whether or not the home was renovated
reno_y_n = np.where(df['yr_renovated']>0, 1, 0 )
df = df.assign(was_renovated = reno_y_n)
df.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>bedrooms</th>
      <th>bathrooms</th>
      <th>sqft_living</th>
      <th>sqft_lot</th>
      <th>floors</th>
      <th>waterfront</th>
      <th>view</th>
      <th>condition</th>
      <th>grade</th>
      <th>sqft_above</th>
      <th>sqft_basement</th>
      <th>yr_built</th>
      <th>yr_renovated</th>
      <th>zipcode</th>
      <th>lat</th>
      <th>long</th>
      <th>sqft_living15</th>
      <th>sqft_lot15</th>
      <th>price</th>
      <th>year_sold</th>
      <th>yr_old_sold</th>
      <th>was_renovated</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2015-03-04</td>
      <td>3</td>
      <td>2.50</td>
      <td>1880</td>
      <td>4499</td>
      <td>2.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>3</td>
      <td>8</td>
      <td>1880</td>
      <td>0.00</td>
      <td>1993</td>
      <td>0.00</td>
      <td>98029</td>
      <td>47.57</td>
      <td>-122.00</td>
      <td>2130</td>
      <td>5114</td>
      <td>529,000.00</td>
      <td>2015</td>
      <td>22</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2014-10-07</td>
      <td>3</td>
      <td>2.50</td>
      <td>2020</td>
      <td>6564</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>3</td>
      <td>7</td>
      <td>1310</td>
      <td>710.00</td>
      <td>1994</td>
      <td>0.00</td>
      <td>98042</td>
      <td>47.35</td>
      <td>-122.16</td>
      <td>1710</td>
      <td>5151</td>
      <td>253,000.00</td>
      <td>2014</td>
      <td>20</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2015-01-16</td>
      <td>5</td>
      <td>4.00</td>
      <td>4720</td>
      <td>493534</td>
      <td>2.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>5</td>
      <td>9</td>
      <td>3960</td>
      <td>760.00</td>
      <td>1975</td>
      <td>0.00</td>
      <td>98027</td>
      <td>47.45</td>
      <td>-122.01</td>
      <td>2160</td>
      <td>219542</td>
      <td>745,000.00</td>
      <td>2015</td>
      <td>40</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2015-03-30</td>
      <td>2</td>
      <td>2.00</td>
      <td>1430</td>
      <td>3880</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4</td>
      <td>7</td>
      <td>1430</td>
      <td>0.00</td>
      <td>1949</td>
      <td>0.00</td>
      <td>98117</td>
      <td>47.68</td>
      <td>-122.39</td>
      <td>1430</td>
      <td>3880</td>
      <td>545,000.00</td>
      <td>2015</td>
      <td>66</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2014-10-14</td>
      <td>3</td>
      <td>2.25</td>
      <td>2270</td>
      <td>32112</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4</td>
      <td>8</td>
      <td>1740</td>
      <td>530.00</td>
      <td>1980</td>
      <td>0.00</td>
      <td>98042</td>
      <td>47.35</td>
      <td>-122.09</td>
      <td>2310</td>
      <td>41606</td>
      <td>390,000.00</td>
      <td>2014</td>
      <td>34</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
## Checking values
df['was_renovated'].value_counts()
```




    0    15650
    1      547
    Name: was_renovated, dtype: int64



>**Results:** Most of the houses were not renovated at the time of sale. This feature may not have a significant impact on determining the sale price due to the small number of renovated houses.

</br>

## `"yrs_since_reno"`

If a house was renovated, how long ago was the renovation? Would more newly-renovated houses increase price?

</br>

```python
## Ensuring there are no null values in the new feature and replacing any with zeroes

df['yrs_since_reno'] = np.where((df['was_renovated']==1),
                                (df['year_sold'] - df['yr_renovated']), 0)

display(df['yrs_since_reno'].describe(),df['yrs_since_reno'].value_counts(ascending=False))
```


    count   16,197.00
    mean         0.61
    std          4.28
    min         -1.00
    25%          0.00
    50%          0.00
    75%          0.00
    max         74.00
    Name: yrs_since_reno, dtype: float64



    0.00     15698
    8.00        25
    1.00        25
    10.00       20
    11.00       20
             ...  
    74.00        1
    64.00        1
    65.00        1
    54.00        1
    48.00        1
    Name: yrs_since_reno, Length: 65, dtype: int64



```python
## Checking for which properties show a renovation year post-sale

df[df['year_sold'] < df['yr_renovated']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>bedrooms</th>
      <th>bathrooms</th>
      <th>sqft_living</th>
      <th>sqft_lot</th>
      <th>floors</th>
      <th>waterfront</th>
      <th>view</th>
      <th>condition</th>
      <th>grade</th>
      <th>sqft_above</th>
      <th>sqft_basement</th>
      <th>yr_built</th>
      <th>yr_renovated</th>
      <th>zipcode</th>
      <th>lat</th>
      <th>long</th>
      <th>sqft_living15</th>
      <th>sqft_lot15</th>
      <th>price</th>
      <th>year_sold</th>
      <th>yr_old_sold</th>
      <th>was_renovated</th>
      <th>yrs_since_reno</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1304</th>
      <td>2014-05-22</td>
      <td>4</td>
      <td>3.25</td>
      <td>3090</td>
      <td>6744</td>
      <td>2.00</td>
      <td>0.00</td>
      <td>4.00</td>
      <td>3</td>
      <td>9</td>
      <td>3090</td>
      <td>0.00</td>
      <td>1923</td>
      <td>2,015.00</td>
      <td>98177</td>
      <td>47.77</td>
      <td>-122.39</td>
      <td>2020</td>
      <td>6656</td>
      <td>850,000.00</td>
      <td>2014</td>
      <td>91</td>
      <td>1</td>
      <td>-1.00</td>
    </tr>
    <tr>
      <th>3241</th>
      <td>2014-10-06</td>
      <td>3</td>
      <td>2.50</td>
      <td>3400</td>
      <td>38400</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>4.00</td>
      <td>3</td>
      <td>8</td>
      <td>1870</td>
      <td>1,530.00</td>
      <td>1955</td>
      <td>2,015.00</td>
      <td>98177</td>
      <td>47.76</td>
      <td>-122.37</td>
      <td>3400</td>
      <td>24338</td>
      <td>825,000.00</td>
      <td>2014</td>
      <td>59</td>
      <td>1</td>
      <td>-1.00</td>
    </tr>
    <tr>
      <th>4094</th>
      <td>2014-07-28</td>
      <td>5</td>
      <td>2.75</td>
      <td>2350</td>
      <td>4178</td>
      <td>1.50</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>3</td>
      <td>8</td>
      <td>1520</td>
      <td>830.00</td>
      <td>1922</td>
      <td>2,015.00</td>
      <td>98112</td>
      <td>47.64</td>
      <td>-122.30</td>
      <td>1920</td>
      <td>4178</td>
      <td>585,000.00</td>
      <td>2014</td>
      <td>92</td>
      <td>1</td>
      <td>-1.00</td>
    </tr>
    <tr>
      <th>10830</th>
      <td>2014-10-28</td>
      <td>4</td>
      <td>3.50</td>
      <td>2770</td>
      <td>10505</td>
      <td>2.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>3</td>
      <td>8</td>
      <td>2770</td>
      <td>0.00</td>
      <td>1940</td>
      <td>2,015.00</td>
      <td>98133</td>
      <td>47.74</td>
      <td>-122.36</td>
      <td>1760</td>
      <td>10505</td>
      <td>285,000.00</td>
      <td>2014</td>
      <td>74</td>
      <td>1</td>
      <td>-1.00</td>
    </tr>
    <tr>
      <th>11412</th>
      <td>2014-07-01</td>
      <td>4</td>
      <td>3.00</td>
      <td>2890</td>
      <td>6885</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>3</td>
      <td>7</td>
      <td>1590</td>
      <td>1,300.00</td>
      <td>1945</td>
      <td>2,015.00</td>
      <td>98115</td>
      <td>47.68</td>
      <td>-122.28</td>
      <td>2180</td>
      <td>6885</td>
      <td>476,000.00</td>
      <td>2014</td>
      <td>69</td>
      <td>1</td>
      <td>-1.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
## Reviewing stats for those houses that were renovated

yrs_and_reno = df[df['yrs_since_reno'] > 0]
yrs_and_reno['yrs_since_reno'].describe()
```




    count   494.00
    mean     19.87
    std      14.79
    min       1.00
    25%       8.25
    50%      16.00
    75%      28.00
    max      74.00
    Name: yrs_since_reno, dtype: float64



>**Results:** As expected, most of the houses were not renovated (indicated by the number of years being zero). 
>
>
>Of those renovated, half of the homes had between 9 and 28 years between the years sold and renovated, with an average ages of roughly 20 years old.
>
>
>Interestingly, this dataset also shows *six records for which the renovation is shown to be post-sale.* While this may be an error, I am leaving it in the dataset since I cannot confidently rule it out. 
>
>
>If this feature does not show statistical significance, I may drops these values and reevaluate the significance.

</br>

## "`has_bsmnt`"

I noticed that there were fewer houses with a value for "sqft_basement" during my data exploration. I am curious if the presence or absence of a basement would have any impact.

</br>

```python
## Determining whether or not a house has a basement based on the square footage
df['has_bsmnt'] = np.where(df['sqft_basement'] > 0, 1, 0)

# Reviewing the results
display(df['has_bsmnt'].describe(), df['has_bsmnt'].value_counts())
```


    count   16,197.00
    mean         0.39
    std          0.49
    min          0.00
    25%          0.00
    50%          0.00
    75%          1.00
    max          1.00
    Name: has_bsmnt, dtype: float64



    0    9926
    1    6271
    Name: has_bsmnt, dtype: int64



```python
6271/16197
```




    0.387170463666111



>**Results:** Surprisingly, it seems that 38% of homes have basements, which is  

</br></br>

# 🔗 **Correlations**

Once I completed the feature engineering, I evaluated the correlations of each feature with 'price' to address any high correlation issues. The results were acceptable, and so I proceeded with reviewing multicollinearity between each feature.

After reviewing the multicollinearity, I decided to remove select features to increase my linear regression modeling in the next section. I dropped 'sqft_living', 'was_renovated', and 'has_basement' due to their high multicollinearity.

</br></br>

# 🪓 **Performing Train/Test Split**

Now I will split the data into the train/test groups. Then, I will run the first linear regression on the "train" data, then another regression on the "test" data.


```python
## Creating features matrix minus target variable
X = df_dropped.drop('price', axis = 1).copy()#
```


```python
## Creating the y values by setting them equal to the 'price' values from the dataframe
y = df_dropped['price'].copy()
```


```python
## Verifying the two groups are of equal length
X.shape[0] == y.shape[0]
```




    True




```python
## Establishing the train and test sets for modeling

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25,
                                                    random_state=505)
```

</br></br>

# 📊 **Creating Baseline Model**


```python
baseline = DummyRegressor()

baseline.fit(X_train, y_train)
print(f'The baseline r^2 score is: {baseline.score(X_train, y_train):.2f}\n\n')
eval_perf_total(baseline, X_train, y_train, X_test, y_test)
```

    The baseline r^2 score is: 0.00
    
    
    Evaluating Performance on Training Data:
    
        Train Mean Absolute Error: 235,136.58
        Train Mean Squared Error:  133,873,926,742.51
    
    Train Root Mean Squared Error: 365,887.86
    Train R-Square Value: 0.0
    
    ---------------------------------------------------------------------------
    
    Evaluating Performance on Testing Data:
    
        Test Mean Absolute Error: 232,942.80
        Test Mean Squared Error:  135,179,768,884.63
    
    Test Root Mean Squared Error: 367,668.01
    Test R-Square Value: -0.0
    

>**Analysis:** The baseline RMSE for the training data shows an error of over 365,000, a substantial amount of error. On the testing data, it seems the model did slightly worse than the training.
>
>
>* My goal is to build a model that performs better than this baseline model in terms of both RMSE and r$^2$

</br></br>

# 🚿 **Developing Data Preprocessor**

## Preprocessing Pipeline via ColumnTransformer

> This combination of transformers is designed to handle any missing values by imputing either a '0' or the mean value for the feature. Additionally, this transformer will perform one-hot encoding for my categorical variables.


```python
## Specifying features for each transformer (below)

imp_zero_cols = ['sqft_basement']
imp_mode_cols = ['view','waterfront','yr_renovated']
ohe_cols = ['condition','grade', 'zipcode']

xf_cols = [*imp_zero_cols, *imp_mode_cols, *ohe_cols]

remaining_cols = [i for i in X.drop('date', axis=1).columns if i not in xf_cols]

imp_zero_cols.extend(remaining_cols)
```


```python
## Creating ColumnTransformer and sub-transformers for imputation and encoding

# Adding zeroes for missing values in sqft_basement
zero_transformer = SimpleImputer(strategy='constant', fill_value=0)

## Adding the mode value to view, waterfront, and yr_renovated missing values 
mode_transformer = SimpleImputer(strategy='mean')

## Encoding categoricals - handling errors to prevent issues w/ test set
categorical_transformer = OneHotEncoder(handle_unknown='ignore', sparse=False)

## Instantiating the ColumnTransformer and including all transformers
preprocessor = ColumnTransformer(
    transformers=[('zero', zero_transformer, imp_zero_cols),
                  ('mode', mode_transformer, imp_mode_cols),
                  ('cats', categorical_transformer, ohe_cols)])
```

</br></br>

# 📊 **Statsmodels Non-Formula OLS Model**

>I create a Statsmodels version of the regression model to compare against my later SKLearn models. I use this comparison to ensure that the SKLearn pipeline below creates the same predictions for the same transformed data


```python
preprocessor.fit(X_train)

## Getting feature names from OHE
ohe_cat_names = preprocessor.named_transformers_['cats'].get_feature_names(ohe_cols)

## Generating list for column index
final_cols = [*imp_zero_cols, *imp_mode_cols, *ohe_cat_names]

## Fit and transform the data via the ColumnTransformer
X_train_tf = preprocessor.transform(X_train)
X_train_tf_df = pd.DataFrame(X_train_tf, columns=final_cols, index=X_train.index)

## Transforming the test set and saving
X_test_tf = preprocessor.transform(X_test)
X_test_tf_df = pd.DataFrame(X_test_tf, columns=final_cols, index=X_test.index)

display(X_train_tf_df.head(5),X_test_tf_df.head(5))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sqft_basement</th>
      <th>bedrooms</th>
      <th>bathrooms</th>
      <th>sqft_lot</th>
      <th>floors</th>
      <th>sqft_above</th>
      <th>yr_built</th>
      <th>lat</th>
      <th>long</th>
      <th>sqft_living15</th>
      <th>sqft_lot15</th>
      <th>year_sold</th>
      <th>yr_old_sold</th>
      <th>yrs_since_reno</th>
      <th>view</th>
      <th>waterfront</th>
      <th>yr_renovated</th>
      <th>condition_1</th>
      <th>condition_2</th>
      <th>condition_3</th>
      <th>condition_4</th>
      <th>condition_5</th>
      <th>grade_3</th>
      <th>grade_4</th>
      <th>grade_5</th>
      <th>grade_6</th>
      <th>grade_7</th>
      <th>grade_8</th>
      <th>grade_9</th>
      <th>grade_10</th>
      <th>grade_11</th>
      <th>grade_12</th>
      <th>grade_13</th>
      <th>zipcode_98001</th>
      <th>zipcode_98002</th>
      <th>zipcode_98003</th>
      <th>zipcode_98004</th>
      <th>zipcode_98005</th>
      <th>zipcode_98006</th>
      <th>zipcode_98007</th>
      <th>zipcode_98008</th>
      <th>zipcode_98010</th>
      <th>zipcode_98011</th>
      <th>zipcode_98014</th>
      <th>zipcode_98019</th>
      <th>zipcode_98022</th>
      <th>zipcode_98023</th>
      <th>zipcode_98024</th>
      <th>zipcode_98027</th>
      <th>zipcode_98028</th>
      <th>zipcode_98029</th>
      <th>zipcode_98030</th>
      <th>zipcode_98031</th>
      <th>zipcode_98032</th>
      <th>zipcode_98033</th>
      <th>zipcode_98034</th>
      <th>zipcode_98038</th>
      <th>zipcode_98039</th>
      <th>zipcode_98040</th>
      <th>zipcode_98042</th>
      <th>zipcode_98045</th>
      <th>zipcode_98052</th>
      <th>zipcode_98053</th>
      <th>zipcode_98055</th>
      <th>zipcode_98056</th>
      <th>zipcode_98058</th>
      <th>zipcode_98059</th>
      <th>zipcode_98065</th>
      <th>zipcode_98070</th>
      <th>zipcode_98072</th>
      <th>zipcode_98074</th>
      <th>zipcode_98075</th>
      <th>zipcode_98077</th>
      <th>zipcode_98092</th>
      <th>zipcode_98102</th>
      <th>zipcode_98103</th>
      <th>zipcode_98105</th>
      <th>zipcode_98106</th>
      <th>zipcode_98107</th>
      <th>zipcode_98108</th>
      <th>zipcode_98109</th>
      <th>zipcode_98112</th>
      <th>zipcode_98115</th>
      <th>zipcode_98116</th>
      <th>zipcode_98117</th>
      <th>zipcode_98118</th>
      <th>zipcode_98119</th>
      <th>zipcode_98122</th>
      <th>zipcode_98125</th>
      <th>zipcode_98126</th>
      <th>zipcode_98133</th>
      <th>zipcode_98136</th>
      <th>zipcode_98144</th>
      <th>zipcode_98146</th>
      <th>zipcode_98148</th>
      <th>zipcode_98155</th>
      <th>zipcode_98166</th>
      <th>zipcode_98168</th>
      <th>zipcode_98177</th>
      <th>zipcode_98178</th>
      <th>zipcode_98188</th>
      <th>zipcode_98198</th>
      <th>zipcode_98199</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1910</th>
      <td>0.00</td>
      <td>4.00</td>
      <td>2.00</td>
      <td>7,767.00</td>
      <td>1.00</td>
      <td>2,020.00</td>
      <td>1,995.00</td>
      <td>47.34</td>
      <td>-122.31</td>
      <td>1,940.00</td>
      <td>8,239.00</td>
      <td>2,014.00</td>
      <td>19.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>1740</th>
      <td>0.00</td>
      <td>3.00</td>
      <td>2.00</td>
      <td>7,456.00</td>
      <td>1.00</td>
      <td>1,520.00</td>
      <td>1,949.00</td>
      <td>47.47</td>
      <td>-122.34</td>
      <td>1,740.00</td>
      <td>8,464.00</td>
      <td>2,014.00</td>
      <td>65.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2960</th>
      <td>240.00</td>
      <td>3.00</td>
      <td>1.75</td>
      <td>8,560.00</td>
      <td>1.00</td>
      <td>1,500.00</td>
      <td>1,948.00</td>
      <td>47.65</td>
      <td>-122.41</td>
      <td>2,240.00</td>
      <td>5,800.00</td>
      <td>2,014.00</td>
      <td>66.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
    </tr>
    <tr>
      <th>8148</th>
      <td>950.00</td>
      <td>4.00</td>
      <td>2.00</td>
      <td>2,250.00</td>
      <td>1.00</td>
      <td>840.00</td>
      <td>1,909.00</td>
      <td>47.65</td>
      <td>-122.34</td>
      <td>1,440.00</td>
      <td>1,545.00</td>
      <td>2,014.00</td>
      <td>105.00</td>
      <td>0.00</td>
      <td>2.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>11109</th>
      <td>0.00</td>
      <td>3.00</td>
      <td>2.25</td>
      <td>8,378.00</td>
      <td>2.00</td>
      <td>1,860.00</td>
      <td>1,995.00</td>
      <td>47.39</td>
      <td>-122.03</td>
      <td>1,870.00</td>
      <td>8,378.00</td>
      <td>2,015.00</td>
      <td>20.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sqft_basement</th>
      <th>bedrooms</th>
      <th>bathrooms</th>
      <th>sqft_lot</th>
      <th>floors</th>
      <th>sqft_above</th>
      <th>yr_built</th>
      <th>lat</th>
      <th>long</th>
      <th>sqft_living15</th>
      <th>sqft_lot15</th>
      <th>year_sold</th>
      <th>yr_old_sold</th>
      <th>yrs_since_reno</th>
      <th>view</th>
      <th>waterfront</th>
      <th>yr_renovated</th>
      <th>condition_1</th>
      <th>condition_2</th>
      <th>condition_3</th>
      <th>condition_4</th>
      <th>condition_5</th>
      <th>grade_3</th>
      <th>grade_4</th>
      <th>grade_5</th>
      <th>grade_6</th>
      <th>grade_7</th>
      <th>grade_8</th>
      <th>grade_9</th>
      <th>grade_10</th>
      <th>grade_11</th>
      <th>grade_12</th>
      <th>grade_13</th>
      <th>zipcode_98001</th>
      <th>zipcode_98002</th>
      <th>zipcode_98003</th>
      <th>zipcode_98004</th>
      <th>zipcode_98005</th>
      <th>zipcode_98006</th>
      <th>zipcode_98007</th>
      <th>zipcode_98008</th>
      <th>zipcode_98010</th>
      <th>zipcode_98011</th>
      <th>zipcode_98014</th>
      <th>zipcode_98019</th>
      <th>zipcode_98022</th>
      <th>zipcode_98023</th>
      <th>zipcode_98024</th>
      <th>zipcode_98027</th>
      <th>zipcode_98028</th>
      <th>zipcode_98029</th>
      <th>zipcode_98030</th>
      <th>zipcode_98031</th>
      <th>zipcode_98032</th>
      <th>zipcode_98033</th>
      <th>zipcode_98034</th>
      <th>zipcode_98038</th>
      <th>zipcode_98039</th>
      <th>zipcode_98040</th>
      <th>zipcode_98042</th>
      <th>zipcode_98045</th>
      <th>zipcode_98052</th>
      <th>zipcode_98053</th>
      <th>zipcode_98055</th>
      <th>zipcode_98056</th>
      <th>zipcode_98058</th>
      <th>zipcode_98059</th>
      <th>zipcode_98065</th>
      <th>zipcode_98070</th>
      <th>zipcode_98072</th>
      <th>zipcode_98074</th>
      <th>zipcode_98075</th>
      <th>zipcode_98077</th>
      <th>zipcode_98092</th>
      <th>zipcode_98102</th>
      <th>zipcode_98103</th>
      <th>zipcode_98105</th>
      <th>zipcode_98106</th>
      <th>zipcode_98107</th>
      <th>zipcode_98108</th>
      <th>zipcode_98109</th>
      <th>zipcode_98112</th>
      <th>zipcode_98115</th>
      <th>zipcode_98116</th>
      <th>zipcode_98117</th>
      <th>zipcode_98118</th>
      <th>zipcode_98119</th>
      <th>zipcode_98122</th>
      <th>zipcode_98125</th>
      <th>zipcode_98126</th>
      <th>zipcode_98133</th>
      <th>zipcode_98136</th>
      <th>zipcode_98144</th>
      <th>zipcode_98146</th>
      <th>zipcode_98148</th>
      <th>zipcode_98155</th>
      <th>zipcode_98166</th>
      <th>zipcode_98168</th>
      <th>zipcode_98177</th>
      <th>zipcode_98178</th>
      <th>zipcode_98188</th>
      <th>zipcode_98198</th>
      <th>zipcode_98199</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6942</th>
      <td>0.00</td>
      <td>3.00</td>
      <td>1.00</td>
      <td>6,530.00</td>
      <td>1.00</td>
      <td>980.00</td>
      <td>1,969.00</td>
      <td>47.71</td>
      <td>-122.21</td>
      <td>1,220.00</td>
      <td>6,723.00</td>
      <td>2,014.00</td>
      <td>45.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>4482</th>
      <td>1,260.00</td>
      <td>5.00</td>
      <td>2.50</td>
      <td>184,140.00</td>
      <td>1.00</td>
      <td>1,410.00</td>
      <td>1,980.00</td>
      <td>47.34</td>
      <td>-122.10</td>
      <td>1,860.00</td>
      <td>35,719.00</td>
      <td>2,015.00</td>
      <td>35.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>11389</th>
      <td>0.00</td>
      <td>3.00</td>
      <td>1.00</td>
      <td>7,560.00</td>
      <td>1.00</td>
      <td>1,250.00</td>
      <td>1,959.00</td>
      <td>47.45</td>
      <td>-122.17</td>
      <td>1,270.00</td>
      <td>7,615.00</td>
      <td>2,015.00</td>
      <td>56.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>9048</th>
      <td>0.00</td>
      <td>3.00</td>
      <td>1.75</td>
      <td>6,557.00</td>
      <td>1.00</td>
      <td>1,890.00</td>
      <td>1,967.00</td>
      <td>47.70</td>
      <td>-122.29</td>
      <td>1,920.00</td>
      <td>6,793.00</td>
      <td>2,014.00</td>
      <td>47.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>5315</th>
      <td>180.00</td>
      <td>3.00</td>
      <td>3.50</td>
      <td>1,077.00</td>
      <td>2.00</td>
      <td>1,300.00</td>
      <td>2,007.00</td>
      <td>47.54</td>
      <td>-122.32</td>
      <td>1,140.00</td>
      <td>2,003.00</td>
      <td>2,014.00</td>
      <td>7.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
  </tbody>
</table>
</div>



```python
## Running a Statsmodels OLS model for verification
sm_reg = sms.OLS(y_train, X_train_tf_df).fit()#sms.add_constant()

sm_reg.summary()
```




<table class="simpletable">
<caption>OLS Regression Results</caption>
<tr>
  <th>Dep. Variable:</th>          <td>price</td>      <th>  R-squared:         </th>  <td>   0.844</td>  
</tr>
<tr>
  <th>Model:</th>                   <td>OLS</td>       <th>  Adj. R-squared:    </th>  <td>   0.843</td>  
</tr>
<tr>
  <th>Method:</th>             <td>Least Squares</td>  <th>  F-statistic:       </th>  <td>   660.9</td>  
</tr>
<tr>
  <th>Date:</th>             <td>Fri, 16 Jul 2021</td> <th>  Prob (F-statistic):</th>   <td>  0.00</td>   
</tr>
<tr>
  <th>Time:</th>                 <td>10:34:19</td>     <th>  Log-Likelihood:    </th> <td>-1.6154e+05</td>
</tr>
<tr>
  <th>No. Observations:</th>      <td> 12147</td>      <th>  AIC:               </th>  <td>3.233e+05</td> 
</tr>
<tr>
  <th>Df Residuals:</th>          <td> 12047</td>      <th>  BIC:               </th>  <td>3.240e+05</td> 
</tr>
<tr>
  <th>Df Model:</th>              <td>    99</td>      <th>                     </th>      <td> </td>     
</tr>
<tr>
  <th>Covariance Type:</th>      <td>nonrobust</td>    <th>                     </th>      <td> </td>     
</tr>
</table>

</br>

<table class="simpletable">
<tr>
         <td></td>           <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  
</tr>
<tr>
  <th>sqft_basement</th>  <td>  112.6360</td> <td>    4.334</td> <td>   25.988</td> <td> 0.000</td> <td>  104.140</td> <td>  121.132</td>
</tr>
<tr>
  <th>bedrooms</th>       <td>-1.137e+04</td> <td> 1956.152</td> <td>   -5.814</td> <td> 0.000</td> <td>-1.52e+04</td> <td>-7537.977</td>
</tr>
<tr>
  <th>bathrooms</th>      <td> 2.345e+04</td> <td> 3206.243</td> <td>    7.315</td> <td> 0.000</td> <td> 1.72e+04</td> <td> 2.97e+04</td>
</tr>
<tr>
  <th>sqft_lot</th>       <td>    0.2476</td> <td>    0.045</td> <td>    5.460</td> <td> 0.000</td> <td>    0.159</td> <td>    0.336</td>
</tr>
<tr>
  <th>floors</th>         <td>-2.494e+04</td> <td> 3874.592</td> <td>   -6.438</td> <td> 0.000</td> <td>-3.25e+04</td> <td>-1.74e+04</td>
</tr>
<tr>
  <th>sqft_above</th>     <td>  153.1484</td> <td>    3.819</td> <td>   40.102</td> <td> 0.000</td> <td>  145.663</td> <td>  160.634</td>
</tr>
<tr>
  <th>yr_built</th>       <td> 1.044e+04</td> <td>  946.559</td> <td>   11.024</td> <td> 0.000</td> <td> 8579.836</td> <td> 1.23e+04</td>
</tr>
<tr>
  <th>lat</th>            <td> 1.926e+05</td> <td> 7.64e+04</td> <td>    2.522</td> <td> 0.012</td> <td> 4.29e+04</td> <td> 3.42e+05</td>
</tr>
<tr>
  <th>long</th>           <td>-1.796e+05</td> <td> 5.44e+04</td> <td>   -3.299</td> <td> 0.001</td> <td>-2.86e+05</td> <td>-7.29e+04</td>
</tr>
<tr>
  <th>sqft_living15</th>  <td>   26.0867</td> <td>    3.515</td> <td>    7.422</td> <td> 0.000</td> <td>   19.197</td> <td>   32.976</td>
</tr>
<tr>
  <th>sqft_lot15</th>     <td>   -0.0784</td> <td>    0.074</td> <td>   -1.061</td> <td> 0.289</td> <td>   -0.223</td> <td>    0.066</td>
</tr>
<tr>
  <th>year_sold</th>      <td> 2.111e+04</td> <td> 1889.453</td> <td>   11.175</td> <td> 0.000</td> <td> 1.74e+04</td> <td> 2.48e+04</td>
</tr>
<tr>
  <th>yr_old_sold</th>    <td> 1.068e+04</td> <td>  944.565</td> <td>   11.306</td> <td> 0.000</td> <td> 8827.377</td> <td> 1.25e+04</td>
</tr>
<tr>
  <th>yrs_since_reno</th> <td>-3662.9445</td> <td>  491.500</td> <td>   -7.453</td> <td> 0.000</td> <td>-4626.363</td> <td>-2699.526</td>
</tr>
<tr>
  <th>view</th>           <td> 5.237e+04</td> <td> 2101.489</td> <td>   24.920</td> <td> 0.000</td> <td> 4.83e+04</td> <td> 5.65e+04</td>
</tr>
<tr>
  <th>waterfront</th>     <td> 7.212e+05</td> <td> 1.73e+04</td> <td>   41.603</td> <td> 0.000</td> <td> 6.87e+05</td> <td> 7.55e+05</td>
</tr>
<tr>
  <th>yr_renovated</th>   <td>   58.1047</td> <td>    5.863</td> <td>    9.910</td> <td> 0.000</td> <td>   46.612</td> <td>   69.597</td>
</tr>
<tr>
  <th>condition_1</th>    <td>-6.182e+07</td> <td> 6.08e+06</td> <td>  -10.167</td> <td> 0.000</td> <td>-7.37e+07</td> <td>-4.99e+07</td>
</tr>
<tr>
  <th>condition_2</th>    <td>-6.174e+07</td> <td> 6.08e+06</td> <td>  -10.153</td> <td> 0.000</td> <td>-7.37e+07</td> <td>-4.98e+07</td>
</tr>
<tr>
  <th>condition_3</th>    <td>-6.174e+07</td> <td> 6.08e+06</td> <td>  -10.153</td> <td> 0.000</td> <td>-7.37e+07</td> <td>-4.98e+07</td>
</tr>
<tr>
  <th>condition_4</th>    <td>-6.171e+07</td> <td> 6.08e+06</td> <td>  -10.148</td> <td> 0.000</td> <td>-7.36e+07</td> <td>-4.98e+07</td>
</tr>
<tr>
  <th>condition_5</th>    <td>-6.166e+07</td> <td> 6.08e+06</td> <td>  -10.141</td> <td> 0.000</td> <td>-7.36e+07</td> <td>-4.97e+07</td>
</tr>
<tr>
  <th>grade_3</th>        <td>-2.826e+07</td> <td> 2.77e+06</td> <td>  -10.209</td> <td> 0.000</td> <td>-3.37e+07</td> <td>-2.28e+07</td>
</tr>
<tr>
  <th>grade_4</th>        <td>-2.837e+07</td> <td> 2.76e+06</td> <td>  -10.265</td> <td> 0.000</td> <td>-3.38e+07</td> <td> -2.3e+07</td>
</tr>
<tr>
  <th>grade_5</th>        <td>-2.838e+07</td> <td> 2.76e+06</td> <td>  -10.271</td> <td> 0.000</td> <td>-3.38e+07</td> <td> -2.3e+07</td>
</tr>
<tr>
  <th>grade_6</th>        <td>-2.838e+07</td> <td> 2.76e+06</td> <td>  -10.270</td> <td> 0.000</td> <td>-3.38e+07</td> <td> -2.3e+07</td>
</tr>
<tr>
  <th>grade_7</th>        <td>-2.838e+07</td> <td> 2.76e+06</td> <td>  -10.268</td> <td> 0.000</td> <td>-3.38e+07</td> <td> -2.3e+07</td>
</tr>
<tr>
  <th>grade_8</th>        <td>-2.836e+07</td> <td> 2.76e+06</td> <td>  -10.260</td> <td> 0.000</td> <td>-3.38e+07</td> <td>-2.29e+07</td>
</tr>
<tr>
  <th>grade_9</th>        <td>-2.829e+07</td> <td> 2.76e+06</td> <td>  -10.234</td> <td> 0.000</td> <td>-3.37e+07</td> <td>-2.29e+07</td>
</tr>
<tr>
  <th>grade_10</th>       <td>-2.816e+07</td> <td> 2.76e+06</td> <td>  -10.188</td> <td> 0.000</td> <td>-3.36e+07</td> <td>-2.27e+07</td>
</tr>
<tr>
  <th>grade_11</th>       <td>-2.796e+07</td> <td> 2.76e+06</td> <td>  -10.116</td> <td> 0.000</td> <td>-3.34e+07</td> <td>-2.25e+07</td>
</tr>
<tr>
  <th>grade_12</th>       <td>-2.751e+07</td> <td> 2.76e+06</td> <td>   -9.954</td> <td> 0.000</td> <td>-3.29e+07</td> <td>-2.21e+07</td>
</tr>
<tr>
  <th>grade_13</th>       <td>-2.661e+07</td> <td> 2.76e+06</td> <td>   -9.625</td> <td> 0.000</td> <td> -3.2e+07</td> <td>-2.12e+07</td>
</tr>
<tr>
  <th>zipcode_98001</th>  <td>-4.574e+06</td> <td> 4.31e+05</td> <td>  -10.616</td> <td> 0.000</td> <td>-5.42e+06</td> <td>-3.73e+06</td>
</tr>
<tr>
  <th>zipcode_98002</th>  <td>-4.557e+06</td> <td> 4.29e+05</td> <td>  -10.625</td> <td> 0.000</td> <td> -5.4e+06</td> <td>-3.72e+06</td>
</tr>
<tr>
  <th>zipcode_98003</th>  <td>-4.585e+06</td> <td> 4.33e+05</td> <td>  -10.600</td> <td> 0.000</td> <td>-5.43e+06</td> <td>-3.74e+06</td>
</tr>
<tr>
  <th>zipcode_98004</th>  <td>-3.868e+06</td> <td> 4.36e+05</td> <td>   -8.874</td> <td> 0.000</td> <td>-4.72e+06</td> <td>-3.01e+06</td>
</tr>
<tr>
  <th>zipcode_98005</th>  <td>-4.306e+06</td> <td> 4.34e+05</td> <td>   -9.911</td> <td> 0.000</td> <td>-5.16e+06</td> <td>-3.45e+06</td>
</tr>
<tr>
  <th>zipcode_98006</th>  <td>-4.363e+06</td> <td> 4.32e+05</td> <td>  -10.099</td> <td> 0.000</td> <td>-5.21e+06</td> <td>-3.52e+06</td>
</tr>
<tr>
  <th>zipcode_98007</th>  <td>-4.351e+06</td> <td> 4.34e+05</td> <td>  -10.037</td> <td> 0.000</td> <td> -5.2e+06</td> <td> -3.5e+06</td>
</tr>
<tr>
  <th>zipcode_98008</th>  <td>-4.341e+06</td> <td> 4.32e+05</td> <td>  -10.041</td> <td> 0.000</td> <td>-5.19e+06</td> <td>-3.49e+06</td>
</tr>
<tr>
  <th>zipcode_98010</th>  <td>-4.476e+06</td> <td> 4.22e+05</td> <td>  -10.616</td> <td> 0.000</td> <td> -5.3e+06</td> <td>-3.65e+06</td>
</tr>
<tr>
  <th>zipcode_98011</th>  <td> -4.51e+06</td> <td>  4.4e+05</td> <td>  -10.262</td> <td> 0.000</td> <td>-5.37e+06</td> <td>-3.65e+06</td>
</tr>
<tr>
  <th>zipcode_98014</th>  <td>-4.463e+06</td> <td> 4.25e+05</td> <td>  -10.508</td> <td> 0.000</td> <td>-5.29e+06</td> <td>-3.63e+06</td>
</tr>
<tr>
  <th>zipcode_98019</th>  <td> -4.51e+06</td> <td>  4.3e+05</td> <td>  -10.480</td> <td> 0.000</td> <td>-5.35e+06</td> <td>-3.67e+06</td>
</tr>
<tr>
  <th>zipcode_98022</th>  <td>-4.513e+06</td> <td> 4.18e+05</td> <td>  -10.789</td> <td> 0.000</td> <td>-5.33e+06</td> <td>-3.69e+06</td>
</tr>
<tr>
  <th>zipcode_98023</th>  <td>-4.614e+06</td> <td> 4.34e+05</td> <td>  -10.625</td> <td> 0.000</td> <td>-5.47e+06</td> <td>-3.76e+06</td>
</tr>
<tr>
  <th>zipcode_98024</th>  <td>  -4.4e+06</td> <td> 4.24e+05</td> <td>  -10.374</td> <td> 0.000</td> <td>-5.23e+06</td> <td>-3.57e+06</td>
</tr>
<tr>
  <th>zipcode_98027</th>  <td>-4.409e+06</td> <td> 4.27e+05</td> <td>  -10.317</td> <td> 0.000</td> <td>-5.25e+06</td> <td>-3.57e+06</td>
</tr>
<tr>
  <th>zipcode_98028</th>  <td>-4.523e+06</td> <td> 4.41e+05</td> <td>  -10.252</td> <td> 0.000</td> <td>-5.39e+06</td> <td>-3.66e+06</td>
</tr>
<tr>
  <th>zipcode_98029</th>  <td>-4.345e+06</td> <td> 4.27e+05</td> <td>  -10.177</td> <td> 0.000</td> <td>-5.18e+06</td> <td>-3.51e+06</td>
</tr>
<tr>
  <th>zipcode_98030</th>  <td> -4.56e+06</td> <td> 4.29e+05</td> <td>  -10.622</td> <td> 0.000</td> <td> -5.4e+06</td> <td>-3.72e+06</td>
</tr>
<tr>
  <th>zipcode_98031</th>  <td> -4.56e+06</td> <td>  4.3e+05</td> <td>  -10.608</td> <td> 0.000</td> <td> -5.4e+06</td> <td>-3.72e+06</td>
</tr>
<tr>
  <th>zipcode_98032</th>  <td>-4.592e+06</td> <td> 4.33e+05</td> <td>  -10.607</td> <td> 0.000</td> <td>-5.44e+06</td> <td>-3.74e+06</td>
</tr>
<tr>
  <th>zipcode_98033</th>  <td>-4.253e+06</td> <td> 4.37e+05</td> <td>   -9.732</td> <td> 0.000</td> <td>-5.11e+06</td> <td> -3.4e+06</td>
</tr>
<tr>
  <th>zipcode_98034</th>  <td>-4.435e+06</td> <td> 4.39e+05</td> <td>  -10.108</td> <td> 0.000</td> <td>-5.29e+06</td> <td>-3.57e+06</td>
</tr>
<tr>
  <th>zipcode_98038</th>  <td>-4.505e+06</td> <td> 4.23e+05</td> <td>  -10.643</td> <td> 0.000</td> <td>-5.33e+06</td> <td>-3.68e+06</td>
</tr>
<tr>
  <th>zipcode_98039</th>  <td>-3.315e+06</td> <td> 4.38e+05</td> <td>   -7.572</td> <td> 0.000</td> <td>-4.17e+06</td> <td>-2.46e+06</td>
</tr>
<tr>
  <th>zipcode_98040</th>  <td>-4.096e+06</td> <td> 4.35e+05</td> <td>   -9.410</td> <td> 0.000</td> <td>-4.95e+06</td> <td>-3.24e+06</td>
</tr>
<tr>
  <th>zipcode_98042</th>  <td>-4.551e+06</td> <td> 4.26e+05</td> <td>  -10.675</td> <td> 0.000</td> <td>-5.39e+06</td> <td>-3.72e+06</td>
</tr>
<tr>
  <th>zipcode_98045</th>  <td>-4.413e+06</td> <td> 4.16e+05</td> <td>  -10.615</td> <td> 0.000</td> <td>-5.23e+06</td> <td> -3.6e+06</td>
</tr>
<tr>
  <th>zipcode_98052</th>  <td> -4.37e+06</td> <td> 4.34e+05</td> <td>  -10.062</td> <td> 0.000</td> <td>-5.22e+06</td> <td>-3.52e+06</td>
</tr>
<tr>
  <th>zipcode_98053</th>  <td>-4.392e+06</td> <td> 4.31e+05</td> <td>  -10.191</td> <td> 0.000</td> <td>-5.24e+06</td> <td>-3.55e+06</td>
</tr>
<tr>
  <th>zipcode_98055</th>  <td>-4.553e+06</td> <td> 4.32e+05</td> <td>  -10.544</td> <td> 0.000</td> <td> -5.4e+06</td> <td>-3.71e+06</td>
</tr>
<tr>
  <th>zipcode_98056</th>  <td>-4.512e+06</td> <td> 4.32e+05</td> <td>  -10.436</td> <td> 0.000</td> <td>-5.36e+06</td> <td>-3.66e+06</td>
</tr>
<tr>
  <th>zipcode_98058</th>  <td>-4.544e+06</td> <td> 4.29e+05</td> <td>  -10.582</td> <td> 0.000</td> <td>-5.39e+06</td> <td> -3.7e+06</td>
</tr>
<tr>
  <th>zipcode_98059</th>  <td>-4.501e+06</td> <td>  4.3e+05</td> <td>  -10.460</td> <td> 0.000</td> <td>-5.34e+06</td> <td>-3.66e+06</td>
</tr>
<tr>
  <th>zipcode_98065</th>  <td>-4.448e+06</td> <td> 4.21e+05</td> <td>  -10.560</td> <td> 0.000</td> <td>-5.27e+06</td> <td>-3.62e+06</td>
</tr>
<tr>
  <th>zipcode_98070</th>  <td>-4.632e+06</td> <td> 4.41e+05</td> <td>  -10.494</td> <td> 0.000</td> <td> -5.5e+06</td> <td>-3.77e+06</td>
</tr>
<tr>
  <th>zipcode_98072</th>  <td>-4.482e+06</td> <td> 4.37e+05</td> <td>  -10.258</td> <td> 0.000</td> <td>-5.34e+06</td> <td>-3.63e+06</td>
</tr>
<tr>
  <th>zipcode_98074</th>  <td>-4.415e+06</td> <td>  4.3e+05</td> <td>  -10.265</td> <td> 0.000</td> <td>-5.26e+06</td> <td>-3.57e+06</td>
</tr>
<tr>
  <th>zipcode_98075</th>  <td>-4.417e+06</td> <td> 4.28e+05</td> <td>  -10.311</td> <td> 0.000</td> <td>-5.26e+06</td> <td>-3.58e+06</td>
</tr>
<tr>
  <th>zipcode_98077</th>  <td> -4.51e+06</td> <td> 4.34e+05</td> <td>  -10.385</td> <td> 0.000</td> <td>-5.36e+06</td> <td>-3.66e+06</td>
</tr>
<tr>
  <th>zipcode_98092</th>  <td>-4.577e+06</td> <td> 4.27e+05</td> <td>  -10.722</td> <td> 0.000</td> <td>-5.41e+06</td> <td>-3.74e+06</td>
</tr>
<tr>
  <th>zipcode_98102</th>  <td>-4.201e+06</td> <td> 4.41e+05</td> <td>   -9.528</td> <td> 0.000</td> <td>-5.07e+06</td> <td>-3.34e+06</td>
</tr>
<tr>
  <th>zipcode_98103</th>  <td>-4.314e+06</td> <td> 4.42e+05</td> <td>   -9.749</td> <td> 0.000</td> <td>-5.18e+06</td> <td>-3.45e+06</td>
</tr>
<tr>
  <th>zipcode_98105</th>  <td>-4.156e+06</td> <td>  4.4e+05</td> <td>   -9.435</td> <td> 0.000</td> <td>-5.02e+06</td> <td>-3.29e+06</td>
</tr>
<tr>
  <th>zipcode_98106</th>  <td>-4.506e+06</td> <td>  4.4e+05</td> <td>  -10.251</td> <td> 0.000</td> <td>-5.37e+06</td> <td>-3.64e+06</td>
</tr>
<tr>
  <th>zipcode_98107</th>  <td>-4.322e+06</td> <td> 4.44e+05</td> <td>   -9.739</td> <td> 0.000</td> <td>-5.19e+06</td> <td>-3.45e+06</td>
</tr>
<tr>
  <th>zipcode_98108</th>  <td>-4.502e+06</td> <td> 4.38e+05</td> <td>  -10.283</td> <td> 0.000</td> <td>-5.36e+06</td> <td>-3.64e+06</td>
</tr>
<tr>
  <th>zipcode_98109</th>  <td>-4.119e+06</td> <td> 4.42e+05</td> <td>   -9.324</td> <td> 0.000</td> <td>-4.99e+06</td> <td>-3.25e+06</td>
</tr>
<tr>
  <th>zipcode_98112</th>  <td>-4.015e+06</td> <td>  4.4e+05</td> <td>   -9.135</td> <td> 0.000</td> <td>-4.88e+06</td> <td>-3.15e+06</td>
</tr>
<tr>
  <th>zipcode_98115</th>  <td>-4.317e+06</td> <td> 4.41e+05</td> <td>   -9.785</td> <td> 0.000</td> <td>-5.18e+06</td> <td>-3.45e+06</td>
</tr>
<tr>
  <th>zipcode_98116</th>  <td>-4.341e+06</td> <td> 4.42e+05</td> <td>   -9.823</td> <td> 0.000</td> <td>-5.21e+06</td> <td>-3.48e+06</td>
</tr>
<tr>
  <th>zipcode_98117</th>  <td> -4.34e+06</td> <td> 4.44e+05</td> <td>   -9.771</td> <td> 0.000</td> <td>-5.21e+06</td> <td>-3.47e+06</td>
</tr>
<tr>
  <th>zipcode_98118</th>  <td>-4.458e+06</td> <td> 4.37e+05</td> <td>  -10.212</td> <td> 0.000</td> <td>-5.31e+06</td> <td> -3.6e+06</td>
</tr>
<tr>
  <th>zipcode_98119</th>  <td>-4.141e+06</td> <td> 4.42e+05</td> <td>   -9.360</td> <td> 0.000</td> <td>-5.01e+06</td> <td>-3.27e+06</td>
</tr>
<tr>
  <th>zipcode_98122</th>  <td>-4.295e+06</td> <td> 4.39e+05</td> <td>   -9.781</td> <td> 0.000</td> <td>-5.16e+06</td> <td>-3.43e+06</td>
</tr>
<tr>
  <th>zipcode_98125</th>  <td> -4.45e+06</td> <td> 4.42e+05</td> <td>  -10.066</td> <td> 0.000</td> <td>-5.32e+06</td> <td>-3.58e+06</td>
</tr>
<tr>
  <th>zipcode_98126</th>  <td>-4.449e+06</td> <td>  4.4e+05</td> <td>  -10.103</td> <td> 0.000</td> <td>-5.31e+06</td> <td>-3.59e+06</td>
</tr>
<tr>
  <th>zipcode_98133</th>  <td>-4.505e+06</td> <td> 4.44e+05</td> <td>  -10.138</td> <td> 0.000</td> <td>-5.38e+06</td> <td>-3.63e+06</td>
</tr>
<tr>
  <th>zipcode_98136</th>  <td>-4.376e+06</td> <td> 4.41e+05</td> <td>   -9.928</td> <td> 0.000</td> <td>-5.24e+06</td> <td>-3.51e+06</td>
</tr>
<tr>
  <th>zipcode_98144</th>  <td>-4.352e+06</td> <td> 4.39e+05</td> <td>   -9.922</td> <td> 0.000</td> <td>-5.21e+06</td> <td>-3.49e+06</td>
</tr>
<tr>
  <th>zipcode_98146</th>  <td>-4.523e+06</td> <td> 4.39e+05</td> <td>  -10.309</td> <td> 0.000</td> <td>-5.38e+06</td> <td>-3.66e+06</td>
</tr>
<tr>
  <th>zipcode_98148</th>  <td> -4.53e+06</td> <td> 4.37e+05</td> <td>  -10.377</td> <td> 0.000</td> <td>-5.39e+06</td> <td>-3.67e+06</td>
</tr>
<tr>
  <th>zipcode_98155</th>  <td>-4.521e+06</td> <td> 4.43e+05</td> <td>  -10.199</td> <td> 0.000</td> <td>-5.39e+06</td> <td>-3.65e+06</td>
</tr>
<tr>
  <th>zipcode_98166</th>  <td>-4.576e+06</td> <td> 4.37e+05</td> <td>  -10.461</td> <td> 0.000</td> <td>-5.43e+06</td> <td>-3.72e+06</td>
</tr>
<tr>
  <th>zipcode_98168</th>  <td>-4.552e+06</td> <td> 4.36e+05</td> <td>  -10.430</td> <td> 0.000</td> <td>-5.41e+06</td> <td> -3.7e+06</td>
</tr>
<tr>
  <th>zipcode_98177</th>  <td>-4.458e+06</td> <td> 4.45e+05</td> <td>  -10.009</td> <td> 0.000</td> <td>-5.33e+06</td> <td>-3.59e+06</td>
</tr>
<tr>
  <th>zipcode_98178</th>  <td>-4.577e+06</td> <td> 4.34e+05</td> <td>  -10.539</td> <td> 0.000</td> <td>-5.43e+06</td> <td>-3.73e+06</td>
</tr>
<tr>
  <th>zipcode_98188</th>  <td>-4.568e+06</td> <td> 4.35e+05</td> <td>  -10.509</td> <td> 0.000</td> <td>-5.42e+06</td> <td>-3.72e+06</td>
</tr>
<tr>
  <th>zipcode_98198</th>  <td>-4.589e+06</td> <td> 4.34e+05</td> <td>  -10.563</td> <td> 0.000</td> <td>-5.44e+06</td> <td>-3.74e+06</td>
</tr>
<tr>
  <th>zipcode_98199</th>  <td>-4.271e+06</td> <td> 4.44e+05</td> <td>   -9.620</td> <td> 0.000</td> <td>-5.14e+06</td> <td> -3.4e+06</td>
</tr>
</table>
<table class="simpletable">
<tr>
  <th>Omnibus:</th>       <td>7708.131</td> <th>  Durbin-Watson:     </th>  <td>   1.979</td> 
</tr>
<tr>
  <th>Prob(Omnibus):</th>  <td> 0.000</td>  <th>  Jarque-Bera (JB):  </th> <td>400669.470</td>
</tr>
<tr>
  <th>Skew:</th>           <td> 2.385</td>  <th>  Prob(JB):          </th>  <td>    0.00</td> 
</tr>
<tr>
  <th>Kurtosis:</th>       <td>30.729</td>  <th>  Cond. No.          </th>  <td>1.06e+16</td> 
</tr>
</table><br/><br/>Notes:<br/>[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.<br/>[2] The smallest eigenvalue is 2.76e-19. This might indicate that there are<br/>strong multicollinearity problems or that the design matrix is singular.




```python
## Pulling SM-OLS coefficients
model_params = sm_reg.params
model_params.sort_values(ascending=False)
```




    waterfront        721,238.91
    lat               192,622.33
    view               52,369.40
    bathrooms          23,452.61
    year_sold          21,114.11
                       ...      
    condition_5   -61,659,904.12
    condition_4   -61,708,716.97
    condition_3   -61,735,224.86
    condition_2   -61,741,976.70
    condition_1   -61,820,846.79
    Length: 103, dtype: float64



### Interpretation

>The r$^2$-score of .84 is good and almost all of my features are statistically-significant (with a p-value of .05, all but 2 exceed the threshold).
>
> Despite the strong scores, the coefficients are extremely high, raising questions about the quality of the data. As this model is only for comparison purposes, I will move on without digging into the results.
>
> **Now I will visualize the results to demonstrate the intensity of the results**

</br></br>

## Visualizing zipcode coefficients


```python
## Generating lists of coefficient names for filtering

zipcode_cols = [x for x in model_params.index if x.startswith('zipcode')]

only_zips = model_params[zipcode_cols]
no_zips = model_params.drop(zipcode_cols)
```


```python
## Generating list of index names for slicing

zips_idx = only_zips.index
no_zips_idx = no_zips.index
```


```python
## Formatting labels for visualizations

no_zips.index = [i.title().replace('_',' ').replace('Sqft','Square Footage of')\
               .replace('Yr', 'Year').replace('Lat', 'Latitude')\
               .replace('Long','Longitude')\
                 .replace('Grade', 'Material Grade: ') for i in no_zips.index]

only_zips.index = [i.replace('zipcode_', ' ') for i in only_zips.index]
```


```python
## Plotting zipcodes visualization

plot_coefs(data = only_zips, kind = "barh", figsize=(10,30),
           x_label = 'Zipcodes', y_label = 'Price ($)',
           title= 'Zip Code Effect on Price');
```


    
![png](output_152_0.png)
    
</br>

## Visualizing all parameters besides zipcodes


```python
## Plotting all features besides zip codes
plot_coefs(data = no_zips, kind = "bar", x_label = 'Features Other Than Zip Code',
           y_label = 'Price ($)', title= 'House Feature Effect on Price',
          figsize = (15,5));
```


    
![png](output_154_0.png)
    

</br></br>

## Interpretation

>As expected, the models demonstrate a very strong negative effect on price for most of the coefficients. The magnitude of the negative effects minimizes the visualization of the few positive coefficients

</br></br>

# 🚿 **Instantiating Pipeline**

> I create two different pipelines for my actual modeling process, one that does not include a scaler and another that does.
>
> The purpose behind the two pipelines is to visualize the impact of scaling data.

</br>

## Non-Scaled Pipeline


```python
## Instantiating full pipeline with ColumnTransformer and LinearRegression
reg_pipe = Pipeline(steps=[('preprocessor', preprocessor),
                      ('regressor', LinearRegression())])
```


```python
## Fitting pipeline to the training data
reg_pipe.fit(X_train, y_train)

## Evaluating model performance
eval_perf_total(reg_pipe, X_train, y_train, X_test, y_test)
```

    Evaluating Performance on Training Data:
    
        Train Mean Absolute Error: 87,165.81
        Train Mean Squared Error:  20,817,549,519.89
    
    Train Root Mean Squared Error: 144,282.88
    Train R-Square Value: 0.84
    
    ---------------------------------------------------------------------------
    
    Evaluating Performance on Testing Data:
    
        Test Mean Absolute Error: 88,696.56
        Test Mean Squared Error:  23,783,023,667.75
    
    Test Root Mean Squared Error: 154,217.46
    Test R-Square Value: 0.82

</br>

### Interpretation

> The model performs very well on both the training and test data with $r^2$ scores pf .84 and .82, respectively. The increase in RMSE and decrease in $r^2$ for the second model indicates some overfitting of the model, however. 
>
>These results indicate the model explains 82% of the data.

</br>

### Verifying Linear Regression Assumptions


```python
## Generating predictions for the unscaled pipeline
y_test_pred = reg_pipe.predict(X_test)
```


```python
## Determining residuals
residuals = (y_test - y_test_pred)

## Plotting to test for normality
sns.histplot(data=residuals);
```


    
![png](output_166_0.png)
    



```python
## Checking the homoscedasticity of the new model
sns.residplot(x=y_test, y=residuals, lowess=True, color="g");
```


    
![png](output_167_0.png)
    



```python
sms.graphics.qqplot(data=residuals, fit=True, line = "45");
```


    
![png](output_168_0.png)
    


### Interpretation

> The graphs above indicate that the model does not fully meet the assumptions of residual normality.
>
> Based on the the histogram and Q-Q plots, the model is not a fully normal distribution (skewed to the right due to outliers in price. Additionally, the residplot shows a slight cone form, violating the assumption of homoscedasticity.
>
> While this model's residual testing is not ideal, it is workable enough to use the model for now. In the future, I may perform outlier removal to clean up the data and address these issues.

</br></br>

### Non-Scaled Coefficients for Recommendations

</br>

> **The first model is complete and I can now provide recommendations based off the results.** I will review the model's coefficients to provide my recommendations to my stakeholders.

</br>

```python
## Retrieving the model coefficients from the model
reg_coefs = get_model_coefs(reg_pipe, final_cols)
```


```python
## Filtering out zipcode-related coefficients and sorting in a descending order
reg_coefs[no_zips_idx].sort_values(ascending=False)
```




    grade_13         1,450,072.92
    waterfront         721,238.91
    grade_12           547,872.23
    lat                192,622.33
    grade_11            99,544.92
    condition_5         73,429.77
    view                52,369.40
    condition_4         24,616.92
    bathrooms           23,452.61
    year_sold           21,114.12
    yr_old_sold         10,678.87
    yr_built            10,435.24
    sqft_above             153.15
    sqft_basement          112.64
    yr_renovated            58.10
    sqft_living15           26.09
    sqft_lot                 0.25
    sqft_lot15              -0.08
    condition_3         -1,890.97
    yrs_since_reno      -3,662.94
    condition_2         -8,642.81
    bedrooms           -11,372.35
    floors             -24,944.90
    condition_1        -87,512.90
    grade_10           -98,218.53
    long              -179,593.67
    grade_3           -200,133.14
    grade_9           -224,560.15
    grade_8           -298,034.28
    grade_4           -311,366.40
    grade_7           -318,867.29
    grade_5           -323,036.44
    grade_6           -323,273.82
    dtype: float64

</br></br>

## 💡 **Recommendations** - *Non-Scaled Data*

</br>
---
> **Based on these results,** I would make the following recommendations to a homeowner interested in renovating to ***increase*** the sell price of their home (*all changes in price assume no other changes to the house*):
>
> * **Add another bathroom** - Adding another bathroom would increase the price by \\$23,452.61.
>
>
> * **Increase the above-ground square-footage of the house** -  the price increases by \\$153.15 for each additional square foot.
>
>    * Depending on other factors affecting cost (including, but not limited to, materials, labor, etc.), *this may be the most reasonable approach for homeowners.*
>
>    * If a homeowner puts an addition on their house, for example, the additional square footage may exceed the benefit of adding a bathroom (assuming the bathroom is not an addition to the house/does not increase ft$^2$).
>
>
> * **Increase the square-footage of the basement** -  the price increases by \\$112.64 for each additional square foot.
>    * This approach may be more expensive than increasing above-ground space due to costs of removing dirt and adding support to maintain the structural integrity of the foundation/support for the rest of the house.
>
>---
> **Furthermore,** I would advise homeowners ***not*** to make the following changes that *decrease* the price (*all changes in price assume no other changes to the house*):
>
> * **Adding another floor** decreases price by \\$24,944.90 - quite a hit considering the potential construction costs of that extra level!
>
>
> * **Building a bedroom** decreases price by \\$11,372.35 - assuming you don't add more square footage to the house, building an extra bedroom would take away from the pre-existing space - a home needs more rooms than just bedrooms!
---
</br>

### Creating Visualizations for Presentation

These next few visualizations show each selected feature's increase on price. I will use these in my presentation to homeowners to demonstrate the impact of each recommended feature on price. 


```python
sns.regplot(data=df_dropped, x="bathrooms", y='price', line_kws={"color": "red"})
plt.suptitle('Impact of Number of Bathrooms on Price')
plt.xlabel('Number of Bathrooms')
plt.ylabel('Price ($)');
# plt.savefig('bath_price.png');
```


    
![png](output_179_0.png)
    



```python
sns.regplot(data=df_dropped, x="sqft_above", y='price', line_kws={"color": "red"})
plt.suptitle('Impact of Above-Ground Ft^2 on Price')
plt.xlabel('Above-Ground ft^2')
plt.ylabel('Price ($)');
# plt.savefig('abovesqft_price.png');
```


    
![png](output_180_0.png)
    



```python
sns.regplot(data=df_dropped, x="sqft_basement", y='price', line_kws={"color": "red"})
plt.suptitle('Impact of Basement Ft^2 on Price')
plt.xlabel('Basement Ft^2')
plt.ylabel('Price ($)');
# plt.savefig('base_price.png');
```


    
![png](output_181_0.png)
    
</br>

### Visualizing the Results

</br>

In the following plots, I separate the zip code coefficients from the rest of the data for clarity's sake. **Please make note of the different scales for price on the x_axis.** The second graph has a larger scale, shrinking the bars slightly in comparison to the first graph.


```python
## Generating lists of coefficient names for filtering

zipcode_cols = [x for x in reg_coefs.index if x.startswith('zipcode')]

only_zips = reg_coefs[zipcode_cols]
no_zips = reg_coefs.drop(zipcode_cols)
no_zips = no_zips.drop('intercept')
```


```python
## Generating list of index names for slicing

zips_idx = only_zips.index
no_zips_idx = no_zips.index
```


```python
## Formatting labels for visualizations

no_zips.index = [i.title().replace('_',' ').replace('Sqft','Square Footage of')\
               .replace('Yr', 'Year').replace('Y_', 'Year').replace('Lat', 'Latitude')\
               .replace('Long','Longitude')\
                 .replace('Grade', 'Material Grade: ') for i in no_zips.index]

only_zips.index = [i.replace('zipcode_', ' ') for i in only_zips.index]
```


```python
## Generating two plots: one for zip codes, then another for all other features

plot_coefs(data = only_zips, kind = "barh", figsize=(20,25), x_label = 'Price ($)',
           y_label = 'Zip Codes', title= 'Effects of Zip Codes on Price')

plt.show()

plot_coefs(data = no_zips, kind = "barh", figsize=(15,25), x_label = 'Price ($)',
           y_label = 'Features', title= 'Effects of House Features on Price');
```


    
![png](output_187_0.png)
    



    
![png](output_187_1.png)
    
</br></br>

## Scaled Pipeline


```python
## Creating full pipeline with ColumnTransformer, StandardScaler and LinearRegression
reg_pipe_scaled = Pipeline(steps=[('preprocessor', preprocessor),
                           ('scaler', StandardScaler()),
                      ('regressor', LinearRegression())])
```


```python
## Fittng pipeline to the training data
reg_pipe_scaled.fit(X_train, y_train)

## Ensuring same results as prior pipeline
eval_perf_total(reg_pipe_scaled, X_train, y_train, X_test, y_test)
```

    Evaluating Performance on Training Data:
    
        Train Mean Absolute Error: 87,212.78
        Train Mean Squared Error:  20,827,166,952.33
    
    Train Root Mean Squared Error: 144,316.20
    Train R-Square Value: 0.84
    
    ---------------------------------------------------------------------------
    
    Evaluating Performance on Testing Data:
    
        Test Mean Absolute Error: 88,732.18
        Test Mean Squared Error:  23,772,180,806.16
    
    Test Root Mean Squared Error: 154,182.30
    Test R-Square Value: 0.82

</br>

### Scaled Coefficients for Recommendations

</br>

> **The second model is complete and I can now provide updated recommendations based off the results.** As the data is now scaled based on the data's averages and standard deviations, the results are different than before.

</br>

```python
## Pulling model coefficients for visualizations

reg_pipe_scaled_coefs = get_model_coefs(reg_pipe_scaled, final_cols)

reg_scaled_zips = reg_pipe_scaled_coefs[zipcode_cols]

reg_scaled_no_zips = reg_pipe_scaled_coefs[no_zips_idx]
```


```python
reg_scaled_no_zips.sort_values(ascending=False)
```




    condition_3       761,963,372,536,106,624.00
    condition_4       700,328,615,200,460,800.00
    condition_5       434,489,924,099,404,224.00
    grade_7           385,669,291,768,366,592.00
    grade_8           352,928,505,818,818,496.00
    grade_9           254,541,414,623,016,128.00
    grade_6           228,243,625,591,567,744.00
    grade_10          174,019,354,129,066,656.00
    condition_2       144,494,525,552,917,664.00
    grade_11          104,646,841,362,640,816.00
    grade_5            84,452,711,321,043,216.00
    condition_1        56,159,569,310,495,624.00
    grade_12           53,509,779,719,303,808.00
    grade_4            25,600,960,311,432,024.00
    grade_13           17,397,443,695,114,854.00
    grade_3             7,103,938,994,693,152.00
    year_sold           2,925,006,817,309,833.50
    sqft_above                        126,130.41
    waterfront                         60,874.47
    sqft_basement                      49,277.69
    view                               39,805.00
    lat                                26,967.79
    yr_renovated                       20,979.77
    bathrooms                          18,284.62
    sqft_living15                      17,723.48
    sqft_lot                           10,412.66
    sqft_lot15                         -2,055.31
    bedrooms                          -10,871.69
    floors                            -13,486.94
    yrs_since_reno                    -15,341.36
    long                              -24,145.04
    yr_built         -183,264,906,897,637,664.00
    yr_old_sold      -183,295,047,950,527,648.00
    dtype: float64


</br></br>

## 💡 **Recommendations** - *Scaled Data*

</br>

---
> **Based on these results,** I stand by my earlier recommendations of increasing above-ground ft.$^2$, basement ft.$^2$, or adding another bathroom and avoiding adding additional floors or bedrooms.
>
>The results for this model are measured in units of standard deviation, making them harder to interpret and less presentation-friendly (i.e. to increase the price with above-ground square footage, you would need to add one unit of standard deviation's worth of square footage).
---

</br></br>

### Visualizing Scaled Results

To get an idea of how these scaled variables changed, I visualize the results. **Please make note of the different scales for price on the x_axis.**


```python
## Generating lists of coefficient names for filtering

zipcode_cols = [x for x in reg_pipe_scaled_coefs.index if x.startswith('zipcode')]

only_zips = reg_pipe_scaled_coefs[zipcode_cols]
no_zips = reg_pipe_scaled_coefs.drop(zipcode_cols)
no_zips = no_zips.drop('intercept')
```


```python
## Generating list of index names for slicing

zips_idx = only_zips.index
no_zips_idx = no_zips.index
```


```python
## Formatting labels for visualizations

no_zips.index = [i.title().replace('_',' ').replace('Sqft','Square Footage: ')\
               .replace('Yr', 'Year').replace('Lat', 'Latitude')\
               .replace('Long','Longitude')\
                 .replace('Grade', 'Material Grade: ') for i in no_zips.index]

only_zips.index = [i.replace('zipcode_', ' ') for i in only_zips.index]
```


```python
## Plotting coefficients

plot_coefs(data = only_zips, kind = "barh", figsize=(30,35), x_label = 'Zip Codes',
           y_label = 'Zip Codes', title= 'Zip Code Effect on Price ($)')

plt.show()

plot_coefs(data = no_zips, kind = "barh", figsize=(25,35), x_label = 'Features Other Than Zip Code',
           y_label = 'Features', title= 'Effects of House Features on Price ($)');
```


    
![png](output_202_0.png)
    



    
![png](output_202_1.png)
    

</br></br></br>

# 🔮 **Creating Predictions on Holdout Data**

> Now that I finished my model, I will read in the new test data and generate my final predictions.


```python
df_xtest = pd.read_csv('bakeoff_data/Xtest.csv')
df_xtest
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>bedrooms</th>
      <th>bathrooms</th>
      <th>sqft_living</th>
      <th>sqft_lot</th>
      <th>floors</th>
      <th>waterfront</th>
      <th>view</th>
      <th>condition</th>
      <th>grade</th>
      <th>sqft_above</th>
      <th>sqft_basement</th>
      <th>yr_built</th>
      <th>yr_renovated</th>
      <th>zipcode</th>
      <th>lat</th>
      <th>long</th>
      <th>sqft_living15</th>
      <th>sqft_lot15</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2/20/2015</td>
      <td>3</td>
      <td>0.75</td>
      <td>850</td>
      <td>8573</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>3</td>
      <td>6</td>
      <td>600</td>
      <td>250.0</td>
      <td>1945</td>
      <td>0.00</td>
      <td>98146</td>
      <td>47.50</td>
      <td>-122.36</td>
      <td>850</td>
      <td>8382</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10/8/2014</td>
      <td>3</td>
      <td>1.00</td>
      <td>1510</td>
      <td>6083</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4</td>
      <td>6</td>
      <td>860</td>
      <td>650.0</td>
      <td>1940</td>
      <td>0.00</td>
      <td>98115</td>
      <td>47.70</td>
      <td>-122.32</td>
      <td>1510</td>
      <td>5712</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3/25/2015</td>
      <td>4</td>
      <td>2.25</td>
      <td>1790</td>
      <td>42000</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>3</td>
      <td>7</td>
      <td>1170</td>
      <td>620.0</td>
      <td>1983</td>
      <td>0.00</td>
      <td>98045</td>
      <td>47.48</td>
      <td>-121.74</td>
      <td>2060</td>
      <td>50094</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2/17/2015</td>
      <td>2</td>
      <td>1.50</td>
      <td>1140</td>
      <td>2500</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>3</td>
      <td>7</td>
      <td>630</td>
      <td>510.0</td>
      <td>1988</td>
      <td>nan</td>
      <td>98106</td>
      <td>47.57</td>
      <td>-122.36</td>
      <td>1500</td>
      <td>5000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5/23/2014</td>
      <td>3</td>
      <td>1.00</td>
      <td>1500</td>
      <td>3920</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>3</td>
      <td>7</td>
      <td>1000</td>
      <td>500.0</td>
      <td>1947</td>
      <td>0.00</td>
      <td>98107</td>
      <td>47.67</td>
      <td>-122.36</td>
      <td>1640</td>
      <td>4017</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>5395</th>
      <td>6/27/2014</td>
      <td>5</td>
      <td>1.00</td>
      <td>1170</td>
      <td>6757</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4</td>
      <td>6</td>
      <td>800</td>
      <td>370.0</td>
      <td>1944</td>
      <td>0.00</td>
      <td>98125</td>
      <td>47.73</td>
      <td>-122.30</td>
      <td>1590</td>
      <td>6794</td>
    </tr>
    <tr>
      <th>5396</th>
      <td>1/20/2015</td>
      <td>3</td>
      <td>1.75</td>
      <td>1670</td>
      <td>5100</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>2.00</td>
      <td>5</td>
      <td>7</td>
      <td>990</td>
      <td>680.0</td>
      <td>1954</td>
      <td>0.00</td>
      <td>98144</td>
      <td>47.59</td>
      <td>-122.29</td>
      <td>2140</td>
      <td>4452</td>
    </tr>
    <tr>
      <th>5397</th>
      <td>3/24/2015</td>
      <td>4</td>
      <td>2.25</td>
      <td>3260</td>
      <td>4640</td>
      <td>2.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>5</td>
      <td>9</td>
      <td>2360</td>
      <td>900.0</td>
      <td>1907</td>
      <td>0.00</td>
      <td>98112</td>
      <td>47.63</td>
      <td>-122.31</td>
      <td>3240</td>
      <td>5800</td>
    </tr>
    <tr>
      <th>5398</th>
      <td>3/16/2015</td>
      <td>4</td>
      <td>5.00</td>
      <td>5820</td>
      <td>13906</td>
      <td>2.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>3</td>
      <td>11</td>
      <td>3750</td>
      <td>2070.0</td>
      <td>1993</td>
      <td>0.00</td>
      <td>98042</td>
      <td>47.38</td>
      <td>-122.16</td>
      <td>2980</td>
      <td>13000</td>
    </tr>
    <tr>
      <th>5399</th>
      <td>3/25/2015</td>
      <td>3</td>
      <td>1.00</td>
      <td>1040</td>
      <td>8122</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>5</td>
      <td>7</td>
      <td>1040</td>
      <td>0.0</td>
      <td>1971</td>
      <td>0.00</td>
      <td>98198</td>
      <td>47.37</td>
      <td>-122.31</td>
      <td>1470</td>
      <td>8676</td>
    </tr>
  </tbody>
</table>
<p>5400 rows × 19 columns</p>
</div>




```python
report_df(df_xtest)
```

    (5400, 19)
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>datatypes</th>
      <th>num_unique</th>
      <th>null_sum</th>
      <th>null_pct</th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>date</th>
      <td>object</td>
      <td>337</td>
      <td>0</td>
      <td>0.00</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
    </tr>
    <tr>
      <th>bedrooms</th>
      <td>int64</td>
      <td>11</td>
      <td>0</td>
      <td>0.00</td>
      <td>5,400.00</td>
      <td>3.38</td>
      <td>0.98</td>
      <td>1.00</td>
      <td>3.00</td>
      <td>3.00</td>
      <td>4.00</td>
      <td>33.00</td>
    </tr>
    <tr>
      <th>bathrooms</th>
      <td>float64</td>
      <td>25</td>
      <td>0</td>
      <td>0.00</td>
      <td>5,400.00</td>
      <td>2.11</td>
      <td>0.77</td>
      <td>0.75</td>
      <td>1.75</td>
      <td>2.25</td>
      <td>2.50</td>
      <td>7.75</td>
    </tr>
    <tr>
      <th>sqft_living</th>
      <td>int64</td>
      <td>612</td>
      <td>0</td>
      <td>0.00</td>
      <td>5,400.00</td>
      <td>2,070.21</td>
      <td>917.81</td>
      <td>410.00</td>
      <td>1,420.00</td>
      <td>1,910.00</td>
      <td>2,520.00</td>
      <td>10,040.00</td>
    </tr>
    <tr>
      <th>sqft_lot</th>
      <td>int64</td>
      <td>3528</td>
      <td>0</td>
      <td>0.00</td>
      <td>5,400.00</td>
      <td>15,181.94</td>
      <td>43,270.26</td>
      <td>609.00</td>
      <td>5,001.00</td>
      <td>7,616.50</td>
      <td>10,588.00</td>
      <td>1,164,794.00</td>
    </tr>
    <tr>
      <th>floors</th>
      <td>float64</td>
      <td>5</td>
      <td>0</td>
      <td>0.00</td>
      <td>5,400.00</td>
      <td>1.49</td>
      <td>0.54</td>
      <td>1.00</td>
      <td>1.00</td>
      <td>1.50</td>
      <td>2.00</td>
      <td>3.00</td>
    </tr>
    <tr>
      <th>waterfront</th>
      <td>float64</td>
      <td>2</td>
      <td>620</td>
      <td>0.11</td>
      <td>4,780.00</td>
      <td>0.01</td>
      <td>0.09</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.00</td>
    </tr>
    <tr>
      <th>view</th>
      <td>float64</td>
      <td>5</td>
      <td>14</td>
      <td>0.00</td>
      <td>5,386.00</td>
      <td>0.24</td>
      <td>0.76</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4.00</td>
    </tr>
    <tr>
      <th>condition</th>
      <td>int64</td>
      <td>5</td>
      <td>0</td>
      <td>0.00</td>
      <td>5,400.00</td>
      <td>3.41</td>
      <td>0.65</td>
      <td>1.00</td>
      <td>3.00</td>
      <td>3.00</td>
      <td>4.00</td>
      <td>5.00</td>
    </tr>
    <tr>
      <th>grade</th>
      <td>int64</td>
      <td>10</td>
      <td>0</td>
      <td>0.00</td>
      <td>5,400.00</td>
      <td>7.66</td>
      <td>1.18</td>
      <td>4.00</td>
      <td>7.00</td>
      <td>7.00</td>
      <td>8.00</td>
      <td>13.00</td>
    </tr>
    <tr>
      <th>sqft_above</th>
      <td>int64</td>
      <td>557</td>
      <td>0</td>
      <td>0.00</td>
      <td>5,400.00</td>
      <td>1,782.98</td>
      <td>828.29</td>
      <td>410.00</td>
      <td>1,190.00</td>
      <td>1,550.00</td>
      <td>2,200.00</td>
      <td>8,860.00</td>
    </tr>
    <tr>
      <th>sqft_basement</th>
      <td>object</td>
      <td>214</td>
      <td>0</td>
      <td>0.00</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
    </tr>
    <tr>
      <th>yr_built</th>
      <td>int64</td>
      <td>116</td>
      <td>0</td>
      <td>0.00</td>
      <td>5,400.00</td>
      <td>1,970.94</td>
      <td>29.53</td>
      <td>1,900.00</td>
      <td>1,951.00</td>
      <td>1,975.00</td>
      <td>1,997.00</td>
      <td>2,015.00</td>
    </tr>
    <tr>
      <th>yr_renovated</th>
      <td>float64</td>
      <td>52</td>
      <td>963</td>
      <td>0.18</td>
      <td>4,437.00</td>
      <td>88.57</td>
      <td>410.95</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>2,015.00</td>
    </tr>
    <tr>
      <th>zipcode</th>
      <td>int64</td>
      <td>70</td>
      <td>0</td>
      <td>0.00</td>
      <td>5,400.00</td>
      <td>98,077.51</td>
      <td>53.60</td>
      <td>98,001.00</td>
      <td>98,032.00</td>
      <td>98,065.00</td>
      <td>98,118.00</td>
      <td>98,199.00</td>
    </tr>
    <tr>
      <th>lat</th>
      <td>float64</td>
      <td>3152</td>
      <td>0</td>
      <td>0.00</td>
      <td>5,400.00</td>
      <td>47.56</td>
      <td>0.14</td>
      <td>47.16</td>
      <td>47.47</td>
      <td>47.57</td>
      <td>47.68</td>
      <td>47.78</td>
    </tr>
    <tr>
      <th>long</th>
      <td>float64</td>
      <td>602</td>
      <td>0</td>
      <td>0.00</td>
      <td>5,400.00</td>
      <td>-122.21</td>
      <td>0.14</td>
      <td>-122.52</td>
      <td>-122.33</td>
      <td>-122.23</td>
      <td>-122.13</td>
      <td>-121.31</td>
    </tr>
    <tr>
      <th>sqft_living15</th>
      <td>int64</td>
      <td>492</td>
      <td>0</td>
      <td>0.00</td>
      <td>5,400.00</td>
      <td>1,983.05</td>
      <td>685.41</td>
      <td>670.00</td>
      <td>1,480.00</td>
      <td>1,830.00</td>
      <td>2,370.00</td>
      <td>5,790.00</td>
    </tr>
    <tr>
      <th>sqft_lot15</th>
      <td>int64</td>
      <td>3322</td>
      <td>0</td>
      <td>0.00</td>
      <td>5,400.00</td>
      <td>12,680.95</td>
      <td>28,558.98</td>
      <td>659.00</td>
      <td>5,100.00</td>
      <td>7,619.50</td>
      <td>10,080.00</td>
      <td>858,132.00</td>
    </tr>
  </tbody>
</table>
</div>

</br></br>

# **🛠 Processing New Data**


```python
df_xtest['sqft_basement'] = pd.to_numeric(df_xtest['sqft_basement'], errors='coerce')
df_xtest['sqft_basement']
```




    0        250.00
    1        650.00
    2        620.00
    3        510.00
    4        500.00
             ...   
    5395     370.00
    5396     680.00
    5397     900.00
    5398   2,070.00
    5399       0.00
    Name: sqft_basement, Length: 5400, dtype: float64



## `'yrs_old_sold'`

### Determine `'year_sold'`

</br>

```python
## Pull the year from the "date" column
df_xtest['year_sold'] = pd.DatetimeIndex(df_xtest['date']).year

## Review the values to ensure data integrity
df_xtest['year_sold'].value_counts()
```




    2014    3648
    2015    1752
    Name: year_sold, dtype: int64



### Calculate `'yr_old_sold'`

</br>

```python
## Calculating the age of the house at the time of sale
df_xtest['yr_old_sold'] = df_xtest['year_sold'] - df_xtest['yr_built']

## Minimum age is -1 due to a house being sold before it was finished being built
display(df_xtest['yr_old_sold'].value_counts().sort_index(), df_xtest['yr_old_sold'].describe())
```


    -1        2
     0      118
     1       77
     2       46
     3       41
           ... 
     111      9
     112     12
     113      7
     114     18
     115      7
    Name: yr_old_sold, Length: 117, dtype: int64



    count   5,400.00
    mean       43.39
    std        29.52
    min        -1.00
    25%        18.00
    50%        39.00
    75%        63.00
    max       115.00
    Name: yr_old_sold, dtype: float64


## `'was_renovated'`

</br>

```python
## Using the year that the home was renovated to deterine whether or not the home was renovated
reno_y_n = np.where(df_xtest['yr_renovated']>0, 1, 0 )
df_xtest = df_xtest.assign(was_renovated = reno_y_n)
df_xtest.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>bedrooms</th>
      <th>bathrooms</th>
      <th>sqft_living</th>
      <th>sqft_lot</th>
      <th>floors</th>
      <th>waterfront</th>
      <th>view</th>
      <th>condition</th>
      <th>grade</th>
      <th>sqft_above</th>
      <th>sqft_basement</th>
      <th>yr_built</th>
      <th>yr_renovated</th>
      <th>zipcode</th>
      <th>lat</th>
      <th>long</th>
      <th>sqft_living15</th>
      <th>sqft_lot15</th>
      <th>year_sold</th>
      <th>yr_old_sold</th>
      <th>was_renovated</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2/20/2015</td>
      <td>3</td>
      <td>0.75</td>
      <td>850</td>
      <td>8573</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>3</td>
      <td>6</td>
      <td>600</td>
      <td>250.00</td>
      <td>1945</td>
      <td>0.00</td>
      <td>98146</td>
      <td>47.50</td>
      <td>-122.36</td>
      <td>850</td>
      <td>8382</td>
      <td>2015</td>
      <td>70</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10/8/2014</td>
      <td>3</td>
      <td>1.00</td>
      <td>1510</td>
      <td>6083</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>4</td>
      <td>6</td>
      <td>860</td>
      <td>650.00</td>
      <td>1940</td>
      <td>0.00</td>
      <td>98115</td>
      <td>47.70</td>
      <td>-122.32</td>
      <td>1510</td>
      <td>5712</td>
      <td>2014</td>
      <td>74</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3/25/2015</td>
      <td>4</td>
      <td>2.25</td>
      <td>1790</td>
      <td>42000</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>3</td>
      <td>7</td>
      <td>1170</td>
      <td>620.00</td>
      <td>1983</td>
      <td>0.00</td>
      <td>98045</td>
      <td>47.48</td>
      <td>-121.74</td>
      <td>2060</td>
      <td>50094</td>
      <td>2015</td>
      <td>32</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2/17/2015</td>
      <td>2</td>
      <td>1.50</td>
      <td>1140</td>
      <td>2500</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>1.00</td>
      <td>3</td>
      <td>7</td>
      <td>630</td>
      <td>510.00</td>
      <td>1988</td>
      <td>nan</td>
      <td>98106</td>
      <td>47.57</td>
      <td>-122.36</td>
      <td>1500</td>
      <td>5000</td>
      <td>2015</td>
      <td>27</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5/23/2014</td>
      <td>3</td>
      <td>1.00</td>
      <td>1500</td>
      <td>3920</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>3</td>
      <td>7</td>
      <td>1000</td>
      <td>500.00</td>
      <td>1947</td>
      <td>0.00</td>
      <td>98107</td>
      <td>47.67</td>
      <td>-122.36</td>
      <td>1640</td>
      <td>4017</td>
      <td>2014</td>
      <td>67</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
## Checking values
df_xtest['was_renovated'].value_counts()
```




    0    5203
    1     197
    Name: was_renovated, dtype: int64



## `"yrs_since_reno"`

</br>

```python
## Ensuring there are no null values in the new feature and replacing any with zeroes

df_xtest['yrs_since_reno'] = np.where((df_xtest['was_renovated']==1),
                                (df_xtest['year_sold'] - df_xtest['yr_renovated']), 0)

# display(df_xtest['yrs_since_reno'].describe(),df_xtest['yrs_since_reno'].value_counts(ascending=False))
```


```python
## Reviewing stats for those houses that were renovated

yrs_and_reno = df_xtest[df_xtest['yrs_since_reno'] > 0]
yrs_and_reno['yrs_since_reno'].describe()
```




    count   176.00
    mean     21.81
    std      15.99
    min       1.00
    25%      10.00
    50%      19.00
    75%      28.25
    max      80.00
    Name: yrs_since_reno, dtype: float64



## "`has_bsmnt`"

</br>

```python
## Determining whether or not a house has a basement based on the square footage
df_xtest['has_bsmnt'] = np.where(df_xtest['sqft_basement'] > 0, 1, 0)

# Reviewing the results
display(df_xtest['has_bsmnt'].describe(), df_xtest['has_bsmnt'].value_counts())
```


    count   5,400.00
    mean        0.38
    std         0.49
    min         0.00
    25%         0.00
    50%         0.00
    75%         1.00
    max         1.00
    Name: has_bsmnt, dtype: float64



    0    3354
    1    2046
    Name: has_bsmnt, dtype: int64

</br>

## Dropping Features to Address Multicollinearity


```python
df_xtest.drop(['was_renovated', 'sqft_living','has_bsmnt'], axis=1, inplace=True)
```

</br></br>

# 🔮 Generating Predictions


```python
X_test.columns
```




    Index(['date', 'bedrooms', 'bathrooms', 'sqft_lot', 'floors', 'waterfront',
           'view', 'condition', 'grade', 'sqft_above', 'sqft_basement', 'yr_built',
           'yr_renovated', 'zipcode', 'lat', 'long', 'sqft_living15', 'sqft_lot15',
           'year_sold', 'yr_old_sold', 'yrs_since_reno'],
          dtype='object')




```python
df_xtest = df_xtest[X_test.columns]
```


```python
final_predictions = reg_pipe.predict(df_xtest)
final_predictions = pd.Series(final_predictions)
```


```python
# final_predictions.to_csv('mccartyb_phase2_predict.csv')
```


# 💡 ** Final Recommendations**

</br>
---
> **Based on these results,** I would make the following recommendations to a homeowner interested in renovating to ***increase*** the sell price of their home (*all changes in price assume no other changes to the house*):
>
>---
>
> * **Add another bathroom** - Adding another bathroom would increase the price by \$23,452.61.
>
>![png](output_179_0.png)
>
>---
>
> * **Increase the above-ground square-footage of the house** -  the price increases by \$153.15 for each additional square foot.
>
>    * Depending on other factors affecting cost (including, but not limited to, materials, labor, etc.), *this may be the most reasonable approach for homeowners.*
>
>    * If a homeowner puts an addition on their house, for example, the additional square footage may exceed the benefit of adding a bathroom (assuming the bathroom is not an addition to the house/does not increase ft$^2$).
>
>![png](output_180_0.png)
>
>---
>
> * **Increase the square-footage of the basement** -  the price increases by \$112.64 for each additional square foot.
>    * This approach may be more expensive than increasing above-ground space due to costs of removing dirt and adding support to maintain the structural integrity of the foundation/support for the rest of the house.
>
>![png](output_181_0.png)
>
>---
> **Furthermore,** I would advise homeowners ***not*** to make the following changes that *decrease* the price (*all changes in price assume no other changes to the house*):
>
> * **Adding another floor** decreases price by \$24,944.90 - quite a hit considering the potential construction costs of that extra level!
>
>
> * **Building a bedroom** decreases price by \$11,372.35 - assuming you don't add more square footage to the house, building an extra bedroom would take away from the pre-existing space - a home needs more rooms than just bedrooms!

</br></br>

# Future Work

The results from my models are fairly strong, based on their $r^2$ scores and their RMSE values around $150,000.

To expand on this project, I would strengthen and expand the pipeline processes:

* My current processes are limited to fixing missing values and preparing categorical data for later modeling. I would like to include additional options for modeling, such as incorporating regularization methods (lasso or elsaticnet).

* Additionally, I would like to include additional feature engineering, such as polynomial features, to delve deeper into the mathematical relationships between features.

* Finally, I would perform hyperparameter tuning via a GridSearch with different settings for my imputers and regression models to see if any other settings would produce stronger modeling scores. 

</br></br>

# For More Information...

Please see the full analysis in the [Jupyter Notebook](./KC_Final.ipynb) as well as my [presentation](./(Re)Selling_Seattle_-_Presentation.pdf).

For any additional questions, please contact:

**Ben McCarty**

Email: [bmccarty@gmail.com](mailto:bmccarty505@gmail.com)

Github: [BenJMcCarty](https://github.com/BenJMcCarty)

</br></br>

# Repository Structure

```
├── README.md
├── KC_Final.ipynb
├── (Re)Selling_Seattle_-_Presentation.pdf
├── bakeoff_data
    └── mccartyb_phase2_predict.csv
    └── Xtest.csv
    └── Xtrain.csv
    └── ytrain.csv
├── img
├── p2pr_functions
    └── __init__.py
    └── functions.py
└── Workbooks
    └── Backups and Old

```
