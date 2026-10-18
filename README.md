# House Price Prediction

Machine learning model that predicts California house prices, served through a Flask REST API.

## Dataset
California Housing dataset (scikit-learn), 20,640 rows, 8 features
(MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude).

## Approach
1. Explored data with Pandas and Matplotlib, checked missing values (none found)
2. Removed outliers in AveRooms, AveBedrms and AveOccup (20,532 rows left)
3. Split data 80/20 into train and test sets
4. Trained Linear Regression and Random Forest, compared MAE, RMSE and R2
5. Tuned Random Forest with GridSearchCV
6. Saved the model with joblib and served it with Flask

## Results (test set)
| Model | MAE | RMSE | R2 |
|---|---|---|---|
| Linear Regression | 0.49 | 0.67 | 0.66 |
| Random Forest | 0.33 | 0.51 | 0.81 |

Price unit is $100,000, so Random Forest average error is about $33,000.

## Run the API
    pip install -r requirements.txt
    python app.py

Send a POST request to `/predict` with the 8 features as JSON (see `test_api.py`).

## Tech stack
Python, Pandas, NumPy, Scikit-learn, Flask, Joblib, Git
