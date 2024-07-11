# Copyright 2021-2024 Avaiga Private Limited
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

"""
Contain the application's configuration including the scenario configurations.

The configuration is run by the Core service.
"""

from algorithms import *

from taipy import Config

from taipy.config import Config, Scope
import datetime as dt


#Config.configure_job_executions(mode="standalone", nb_of_workers=2)
path_to_data = "data/modified_supermarkt_sales_plus.csv"
# TODO: we are going to configure all our data nodes into this config, start by configuring a csv data node
#       for the initial_data_cfg using id `initial_data`, storage_type `csv`, path `path_to_data` and scope `Scope.GLOBAL`
#       we'll use the `Config.configure_data_node` function for this
initial_data_cfg = ...

# TODO: do the same for holiday, level and date cfgs
# storage_type = "csv"
holiday_cfg = ...
# use default_data = 1 for level_cfg
level_cfg = ...
date_cfg = ...

# TODO: configure final_data_cfg
final_data_cfg =  ...

# TODO: we will build two models for forecasting: arima and xgboost, define their datanode config
model_arima_cfg = ...
model_xgboost_cfg = ...

predictions_arima_cfg = Config.configure_data_node(id="predictions_arima")
predictions_xgboost_cfg = Config.configure_data_node(id="predictions_xgboost")

# TODO: configure the result datanode
result_cfg = ...

"""
Now we are going to define the tasks.
Tasks are functions connecting multiple entry datanodes to multiple output datanodes
"""

# TODO: Take a look at the `algorithms/algorithms.py` file and functions

# TODO: Use the functions in `algorithms.py` to define the tasks.

# TODO: the preprocess task connects [initial_data_cfg, holiday_cfg, level_cfg] to [final_data_cfg, date_cfg]
#       with a function that you have to find..
task_preprocess_cfg = ...

# TODO: the `train_arima` task connects `final_data_cfg` datanode to the `model_arima_cfg` with the arima training function
task_train_arima_cfg = ...

# TODO: the `forecast arima` task connects `model_arima_cfg` to the `predictions_arima_cfg` using the arima prediction function
task_forecast_arima_cfg = ...

# TODO: do the same for xgboost
task_train_xgboost_cfg = ...

task_forecast_xgboost_cfg = ...

# TODO: harmonize results in the `result_cfg` datanode by taking the final_data, predictions_arima and predictions_xgboost datanodes
# as input
task_result_cfg = Config.configure_task(id="task_result",
                                        function=concat,
                                        input=[final_data_cfg, 
                                               predictions_arima_cfg, 
                                               predictions_xgboost_cfg],
                                        output=result_cfg)

# TODO: now configure the overall scenario.
# A scenario is a collection of multiple tasks that are performed sequentially.
scenario_cfg = ...

Config.export('configuration/config.toml')