from taipy import Config, Scope, Frequency

from taipy.core import Scenario

import datetime as dt

from algos.algos import clean_data, predict, evaluate


## Input Data Nodes
initial_dataset_cfg = Config.configure_data_node(id="initial_dataset",
                                                 storage_type="csv",
                                                 path="data/dataset.csv",
                                                 scope=Scope.GLOBAL)

# We assume the current day is the 26th of July 2021.
# This day can be changed to simulate multiple executions of scenarios on different days
day_cfg = Config.configure_data_node(id="day", default_data=dt.datetime(2021, 7, 26))

## Remaining Data Node
cleaned_dataset_cfg = Config.configure_data_node(id="cleaned_dataset",
                                                 storage_type="parquet",
                                                 scope=Scope.GLOBAL)
predictions_cfg = Config.configure_data_node(id="predictions")

# Task config objects
clean_data_task_cfg = Config.configure_task(id="clean_data",
                                            function=clean_data,
                                            input=initial_dataset_cfg,
                                            output=cleaned_dataset_cfg,
                                            skippable=True)

predict_task_cfg = Config.configure_task(id="predict",
                                         function=predict,
                                         input=[cleaned_dataset_cfg, day_cfg],
                                         output=predictions_cfg,
                                         skippable=True)

evaluation_cfg = Config.configure_data_node(id="evaluation")
evaluate_task_cfg = Config.configure_task(id="evaluate",
                                          function=evaluate,
                                          input=[predictions_cfg, cleaned_dataset_cfg, day_cfg],
                                          output=evaluation_cfg,
                                          skippable=True)

# 
# Configure our scenario config.
scenario_cfg = Config.configure_scenario(id="scenario", task_configs=[clean_data_task_cfg, predict_task_cfg,evaluate_task_cfg], frequency=Frequency.MONTHLY)

Config.export('config/config.toml')
