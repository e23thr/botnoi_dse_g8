from learning_model.helper import load_data, clean_data, split_train_test, extract_feature, train_model, eval_acc, \
    predict_with_model


def run_pipeline():
    # Get data
    raw_data_df = load_data()

    # Clean
    clean_data_df = clean_data(raw_data_df)

    # Separate Train, Test
    train_df, test_df = split_train_test(clean_data_df)

    # Extract feature
    train_feat, train_label = extract_feature(train_df)
    test_feat, test_label = extract_feature(test_df)

    # Train Model
    model = train_model(train_feat, train_label)

    # Predict Test
    predict = model.predict(test_feat)

    accuracy = eval_acc(predict, test_label)
    return accuracy


print(predict_with_model(123, 2, 3, 2))
