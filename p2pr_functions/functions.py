## Name: Functions

## Description: functions created for purposes of Phase 2 Project (revisited)

## By Ben McCarty (bmccarty505@gmail.com)

#################################################################################################

## Check using z-score - sensitive to outliers

def find_outliers_z(data):
    """Detects outliers using the Z-score>3 cutoff.
    Returns a boolean Series where True=outlier
    
    Source: https://github.com/jirvingphd/dsc-phase-2-project/blob/main/functions_SG.py

    Args:
        data (pd.Series): Series for which to determine the outliers via the Z-score

    Returns:
        pd.Series: Boolean index indicating "True" if a value is an outlier
    """
    import numpy as np
    import scipy as stats
    import matplotlib.pyplot as plt
    import pandas as pd

    zFP = np.abs(stats.zscore(data))
    zFP = pd.Series(zFP, index=data.index)
    idx_outliers = zFP > 3
    return idx_outliers

###
## Check using IQR - less sensitive to outliers

def find_outliers_IQR(data):
    """Determines outliers using the 1.5*IQR thresholds.

    Source: https://github.com/jirvingphd/dsc-phase-2-project/blob/main/functions_SG.py

    Args:
        data (pd.Series): [description]

    Returns:
        pd.Series: Boolean Series where True=outlier
    """    
        
    res = data.describe()
    q1 = res['25%']
    q3 = res['75%']
    thresh = 1.5*(q3-q1)
    idx_outliers =(data < (q1-thresh)) | (data > (q3+thresh))
    return idx_outliers

###
def feature_vis(data, x, y = 'price', categorical = False, kde = True):
    """
    Prints the selected Series for reference.
    
    Creates two plots via Seaborn:

        * Scatter plot with regression line
        * Histogram of the data
            * Optional KDE ifkde = True

    Args:
        data (pd.DataFrame): Source dataframe
        x (pd.Series): Independent variable for visualizations
        y (str, optional): Dependent variable. Defaults to 'price'.
        categorical (bool, optional): Indicate if the values are categorical. Defaults to False.
        kde (bool, optional): Add KDE plot to histogram. Defaults to True.
    
    Returns:
        N/a
    """
    import matplotlib.pyplot as plt
    import seaborn as sns

    print(data[x].value_counts().sort_index())
      
    fig, axs = plt.subplots(ncols=2, figsize= (12,6))
    
    sns.regplot(data=data, x=x, y=y, ax=axs[0])
    sns.histplot(data=data, x=x, discrete=categorical, kde=kde, ax=axs[1])
    
    fig.suptitle(f'{x.title()} vs. {y.title()}', fontsize=16)
    plt.tight_layout();
    
    return

###
def filter_outliers(data):
    """Filters outliers from given data via the "find_outliers_IQR" function and saves filtered
    values to a new DataFrame

    Args:
        data (pd.Series): Selected Series

    Returns:
        pd.DataFrame: DataFrame of non-outlier data filtered from original DataFrame
    """    
       
    idx_out = find_outliers_IQR(data)
 
    cleaned = data[~idx_out].copy()

    print(f'There were {idx_out.sum()} outliers.')
    
    return cleaned

###
def show_cleaned_vis(data, x, y = 'price', categorical = False, kde = True):
    """Combines helper functions to filter outliers and to create the feature 
        visualizations.
    
    * Requres 'find_outliers_IQR' and 'feature_vis' to be pre-defined

    Args:
        data (pd.DataFrame): Source data
        x (str): Independent variable to visualize
        y (str, optional): Dependent variable against which to plot the independent variable. Defaults to 'price'.
        categorical (bool, optional): Indicates whether or not 'x' is categorical. Defaults to False.
        kde (bool, optional): Overlay a KDE plot. Defaults to True.

    Returns:
        None
    """
    
    import matplotlib.pyplot as plt
    import seaborn as sns

    ### Filter outliers first
    
    idx_out = find_outliers_IQR(data[x])
 
    df_cleaned = data[~idx_out].copy()

    ### Plot Data
        
    df_cleaned.value_counts().sort_index()
        
    fig, axs = plt.subplots(ncols=2, figsize= (12,6))
    
    sns.regplot(data=df_cleaned, x=x, y=y, ax=axs[0],line_kws={"color": "red"})
    sns.histplot(data=df_cleaned, x=x, discrete=categorical, kde=kde, ax=axs[1])
    
    fig.suptitle(f'{x.title()} vs. {y.title()}', fontsize=16)
    plt.tight_layout();
    
    return #df_cleaned

###
def ttest_review(sample_1, sample_2, alpha=.05):
    """Runs a t-test on two samples from the same independent variable; prints whether or not they are significant;
    and returns p-value as a variable called "p-value."

    Args:
        sample_1 (pd.Series): First sample of a Series from source DataFrame to evaluate
        sample_2 (pd.Series): Second sample of a Series from source DataFrame to evaluate
        alpha (float, optional): Significance level for test. Defaults to .05.

    Returns:
        int: Resulting p-value for reference
    """    
    import scipy as stats

    result = stats.ttest_ind(sample_1, sample_2)
    crit_val, p_val = result
    
    ## Creating interpretation based on p-value results.

    if p_val < .05:
        print(f'The feature is statistically significant with a p-value of {p_val}.')

    else:
         print(f'The feature is not statistically significant with a p-value of {p_val}.')
    
    return p_val

###
def corr_val(df,figsize=(15,15),cmap="OrRd",):
    """Generates a Seaborn heatmap of correlations between each independent variable.

    Args:
        df (pd.Dataframe): Source DataFrame
        figsize (tuple, optional): Size of resulting figure. Defaults to (15,15).
        cmap (str, optional): Color scheme. Defaults to "OrRd".

    Returns:
        fig, ax: resulting visualization
    """
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Calculate correlations
    corr = df.corr()
       
    # Create a mask of the same size as our correlation data
    mask = np.zeros_like(corr)
    
    # Set the upper values of the numpy array to "True" to ignore them
    mask[np.triu_indices_from(mask)] = True

    fig, ax = plt.subplots(figsize=figsize)
    
    # Mask=mask to hide the upper-right half of values (otherwise mirrored)
    sns.heatmap(corr, annot=True,cmap="Reds",mask=mask)
    return fig, ax

###
def diagnose_model(model, figsize=(10,5)):
    """ ---
    
    Argument:
        * model: provide the linear regression model for diagnostics
    
    Keyword Argument:
        * figsize: default (10,5); can increase/decrease for larger/smaller
    ---
    
    * Display the summary details of the provided model
    * Create two scatter plots to test assumptions of linearity
        * Predictions: verifying homoscedasticity (no cone-shapes)
        * Residuals: confirming normal distribution of residuals
    ---
    
    """
    import matplotlib.pyplot as plt
    import statsmodels.formula.api as smf
    import statsmodels.api as sms

    print(model.summary())
    
    fig, axes = plt.subplots(ncols=2, figsize=figsize)

    axes[0].scatter(model.predict(), model.resid)
    axes[0].axhline()
    axes[0].set_xlabel('Model Predictions')
    axes[0].set_ylabel('Model Residuals')
    axes[0].set_title('Testing for Homoscedasticity')

    sms.graphics.qqplot(data=model.resid, fit=True, line = "45", ax=axes[1])
    
    plt.tight_layout()
    
    return

###
def create_model(data, cont, cat, target):
    """Creates a linear regression model using Statsmodels OLS and 
    evaluates assumptions of linearity by plotting residuals for homoscedasticity
    and a Q-Q plot for normality.

    Args:
        data (pd.DataFrame): Source DataFrame
        cont (list): List of strings indicating which column names to treat as continuous data
        cat (list): List of strings indicating which column names to treat as categorical data

    Returns:
        model: Statsmodels OLS Linear Regression model
    """    
    import statsmodels.formula.api as smf

    cont_features = '+'.join(cont)

    cat_features = '+'.join([f'C({x})' for x in cat])

    f = f'{target}~+{cont_features}+{cat_features}'

    print(f)

    model = smf.ols(formula=f, data=data).fit()
   
    diagnose_model(model)
    
    return model

###
def plot_param_coef(model, kind = 'barh', figsize = (10,5)):
    """Plotting a figure to visualize parameter coefficients

    Args:
        model (Statsmodels OLS model object): linear regression model details to plot
        kind (str, optional): Plot type. Defaults to 'barh'.
        figsize (tuple, optional): Figure size. Defaults to (10,5).
    """
    import matplotlib.pyplot as plt
 
    ## Getting coefficients as a Series
    params = model.params[1:]
    params.sort_values(inplace=True)

    plt.figure(figsize=figsize) # Used if large number of params
    ax = params.plot(kind=kind)
    ax.axvline()
    ax.set_xlabel('Coefficient')
    ax.set_ylabel('Features')
    ax.set_title('Comparing Feature Coefficients')
    
    plt.tight_layout()
    
    return

###
def plot_p_values(model, kind = 'barh', figsize = (10,5), alpha = .05):
    """Plots a figure to visualize parameter p-values exceeding stated alpha.

    Args:
        model (Statsmodels OLS model object): Model details to plot.
        kind (str, optional): Plot type. Defaults to 'barh'.
        figsize (tuple, optional): Figure size. Defaults to (10,5).
        alpha (float, optional): Significance level (p-value). Defaults to .05.
    """   
    
    import matplotlib.pyplot as plt

    pv = model.pvalues[1:]
    pv_high = pv[pv > alpha]
    pv_low = pv[pv <= alpha]
    pv_high.sort_values(ascending=False, inplace=True)
    
    if len(pv_high) > 0:
        plt.figure(figsize=figsize) # Used if large number of params
        ax = pv_high.plot(kind=kind)
        ax = pv_low.plot(kind=kind)
        ax.axvline()
        plt.suptitle(f'P-Values')
        
    if len(pv_low) > 0:
        plt.figure(figsize=figsize) # Used if large number of params
        ax = pv_low.plot(kind=kind)
        ax.axvline()
        plt.suptitle(f'P-Values Below {alpha}')        

    ## Not used; keeping just in case        
#   else:
#         print(f'There are no p-values above {alpha}.')
        
    plt.tight_layout()
    
    return

###
def review_model(model):
    """Combines earlier functions into one all-purpose function for reviewing
    model performance.

    Args:
        model (Statsmodels OLS model object): Model details to plot.
    """    
    
    diagnose_model(model)
    
    plot_param_coef(model)
    
    plot_p_values(model)
    
    return

def report_df(dataframe):
    """Creates a summary of a given dataframe per column, including:
        * Datatypes
        * Number of unique values
        * Number of NaN values
        * Percent of NaN values

    Args:
        dataframe ([pd.DataFrame): Source DataFrame for summary

    Returns:
        pd.DataFrame: DataFrame containing results of summary
    """

    import pandas as pd

    report_df = pd.DataFrame({'datatypes':dataframe.dtypes,'num_unique':dataframe.nunique(),'null_sum':dataframe.isna().sum(),'null_pct':dataframe.isna().sum()/len(dataframe)})

    report_df = pd.concat([report_df, dataframe.describe().T], axis=1)

    display(dataframe.shape)

    return report_df

### End ###