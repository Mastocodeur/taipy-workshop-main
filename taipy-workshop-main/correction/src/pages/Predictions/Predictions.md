<|layout|columns=2 9|gap=50px|
<sidebar|sidebar|
Create and select **scenarios**

<|{selected_scenario}|scenario_selector|>
|sidebar>

<scenario|part|render={selected_scenario}|
# **Prediction**{: .color-primary} page

Predict **company sales** depending on the holidays that employees take. Create different scenarios and choose the best one.

Here are two dataframes representing employee holidays ([High](data/holiday_high.csv) and [Low](data/holiday_low.csv)) that you can upload to the application.

<|3 5|layout|
<date|
#### Level

A parameter to choose how holidays impact your predictions.

<|{selected_level}|slider|on_change=on_change_params|not continuous|min=70|max=150|>
|date>

<country|
#### **Holiday**{: .color-primary}

Upload the CSV of employee holidays:

<|{dn_holiday}|data_node|expanded=False|>


<|{selected_holiday}|file_selector|label=Holiday|on_action=on_change_params|>
|country>
|>

Run your scenario

<|{selected_scenario}|scenario|on_submission_change=on_submission_change|not expanded|>

---------------------------------------

## **Predictions**{: .color-primary}

<|{dn_result}|data_node|>
|scenario>
|>
