# NBA Games Prediction

The National Basketball Association (NBA) is one of the most exciting professional sports organizations in America.  Major League Baseball has demonstrated the benefit of data and analytics to help make personell and strategy decisions to create positive outcomes, notably demonstrated in the movie Moneyball.  The NBA has much room to grow in terms of using an empirical approach to decision making.  This model will attempt to highlight the major characteristics that are present in a win.  With a predictive model for a team's success, coaches can run through different scenarios on how they want to gameplan against a specific team.

## Dataset

### Overview
The NBA Games Data Kaggle dataset (https://www.kaggle.com/datasets/nathanlauga/nba-games) is a dataset of all NBA games from 2004-2020.  The information was collected from the NBA stats website and contains key information about the perfromance of each team during the game.  I will be using this data to train a model on what the key characteristics are for an NBA team in a win.  Using a data-driven approach, NBA teams can choose their focus area for strategizing and practicing when preparing for a successful season.

### Task
The model will be a classification effort to predict if the home team will win the game.  Classifying a home win will help incorporate any advantage that occurs in a team's home stadium.  The features that will be used in the model are the raw values for:
- PTS_home: The number of points the home team scored
- FG_PCT_home: The field goal percentage for the home team
- FT_PCT_home: The free throw percentage for the home team
- FG3_PCT_home: The 3 point field goal percentage for the home team
- AST_home: The number of assists for the home team
- REB_home: The number of rebounds for the home team
- FG_PCT_away: The field goal percentage for the home team 
- FT_PCT_away: The free throw percentage for the home team
- FG3_PCT_away: The 3 point field goal percentage for the home team
- AST_away: The number of assists for the home team
- REB_away: The number of rebounds for the home team

There could additionally be another model that includes the home team and away team ID to identify which teams have a larger home advantage as well as identify teams/schemes that the home team struggles with.  For the purpose of this exercise, normalizing this approach over time is out of scope.  The model solely deals with data that occurred during the game.  An iteresting feature to highlight is PTS_home.  Knowing how many points will most likely result in a win will be an interesting feature to frame in-game strategies.

### Access
The dataset was downloaded from Kaggle and manually updated into Azure via the Datasets UI.

## Automated ML
*TODO*: Give an overview of the `automl` settings and configuration you used for this experiment

### Results
*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search


### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
