https://docs.taipy.io/en/release-3.0/knowledge_base/tutorials/understanding_gui/step_02/step_02/#visual-elements
1. Create a layout with 2 columns
1.1 In this layout, first create a side bar used to navigate through scenarios or create one
1.1.1 Also create a `scenario_selector` object inside the sidebar
1.2 On the second column of the layout, create a `part` object that represents the selected scenario (this object renders the {selected_scenario} variable dynamically)
1.2.1 Design a page containing at least a:
    - a slider to let the user define the importance of the holidays in the scenario
    - a file uploader to let the user submit holiday data for the given scenario
1.2.2 At the bottom of that page, include a scenario object representing the `selected_scenario` variable.
1.2.3 Include the predictions of the model for this scenario at the bottom of this page. The predictions should be made as a `data_node` object pointing to the `dn_result` object.