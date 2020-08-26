import pandas as pd
import numpy as np
import pickle

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split


def load_data():
    town_home_df = pd.read_csv('Data/townhome.csv')
    none_town_home_df = pd.read_csv('Data/none_townhome.csv')
    return pd.concat([town_home_df, none_town_home_df])


def clean_data(df):
    feat = df.copy()
    feat = feat.drop('url', axis=1)
    feat = feat.drop('description', axis=1)
    feat = feat.drop('images', axis=1)
    feat = feat.drop('image_index', axis=1)
    feat = feat.drop('detached_house', axis=1)
    feat = feat.drop('semi_detached_house', axis=1)
    feat = feat.drop('town_home', axis=1)
    feat = feat.drop('Unnamed: 0', axis=1)

    feat._get_numeric_data()
    return feat


def extract_feature(df):
    label = df['price']
    data = df.drop('price', axis=1)
    return data, label


def split_train_test(df):
    train_df, test_df = train_test_split(df, test_size=0.5, random_state=2020, shuffle=True)
    return train_df, test_df


def train_model(feat, label):
    # random forrest
    # model = RandomForestRegressor(max_depth=1000, random_state=2020)

    # Gradient Boosting
    model = GradientBoostingRegressor(random_state=2020)

    # Decision Tree
    # model = tree.DecisionTreeRegressor(max_depth=20, random_state=200)

    # Linear Regression
    # model = LinearRegression()
    model.fit(feat, label)

    # save model
    filename = 'house_price_model.p'
    pickle.dump(model, open('./Model/' + filename, 'wb'))
    return model


def eval_acc(prediction, actual):
    acc = sum(prediction == actual) / len(actual)
    return acc


def predict_with_model(area, bedrooms, restrooms, floors):
    model = pickle.load(open("./Model/house_price_model.p", "rb"))
    predict = model.predict(pd.DataFrame([[area, bedrooms, restrooms, floors]]))

    return predict[0]
