import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from src.custom_logger import setup_logger, INFO


def main():
    # Initialize the logger
    logger = setup_logger("main", log_level=INFO)

    try:
        # Load train and test data
        logger.info("Loading training and test data...")
        train_data = pd.read_json("data/raw/train.json")
        test_data = pd.read_json("data/raw/test.json")
        logger.info("Data loaded successfully.")

        # Combine ingredients into a single string for vectorization
        logger.info("Combining ingredients into a single string for vectorization...")
        train_data["ingredients_str"] = train_data["ingredients"].apply(
            lambda x: ",".join(x)
        )
        test_data["ingredients_str"] = test_data["ingredients"].apply(
            lambda x: ",".join(x)
        )

        # Prepare features (X) and labels (y) for the training set
        X_train_full = train_data["ingredients_str"]
        y_train_full = train_data["cuisine"]

        # Prepare features for the test set
        X_test = test_data["ingredients_str"]

        # Split the full training data into training and validation sets
        logger.info("Splitting data into training and validation sets...")
        X_train, X_val, y_train, y_val = train_test_split(
            X_train_full, y_train_full, test_size=0.2, random_state=42
        )

        # Create a Bag of Words model using CountVectorizer
        logger.info("Creating Bag of Words model...")
        vectorizer = CountVectorizer()

        # Vectorize the training and validation data
        logger.info("Vectorizing training and validation data...")
        X_train_vectorized = vectorizer.fit_transform(X_train)
        X_val_vectorized = vectorizer.transform(X_val)

        # Vectorize the test data
        X_test_vectorized = vectorizer.transform(X_test)

        # Initialize and train the Logistic Regression model on TRAINING data
        logger.info("Training the Logistic Regression model...")
        model = LogisticRegression(max_iter=1000)
        model.fit(X_train_vectorized, y_train)

        # Evaluate the model on training data
        y_train_pred = model.predict(X_train_vectorized)
        train_accuracy = accuracy_score(y_train, y_train_pred)
        logger.info(f"Train Accuracy: {train_accuracy * 100:.1f}%")

        # Validate the model using the validation data
        y_val_pred = model.predict(X_val_vectorized)
        val_accuracy = accuracy_score(y_val, y_val_pred)
        logger.info(f"Validation Accuracy: {val_accuracy * 100:.1f}%")

        # Generate predictions for submission using the test data
        logger.info("Generating predictions for submission...")
        y_test_pred = model.predict(X_test_vectorized)

        # Create a submission dataframe with predictions from test data
        submission = pd.DataFrame({"id": test_data["id"], "cuisine": y_test_pred})

        # Save the submission file
        submission_file = "data/submission.csv"
        submission.to_csv(submission_file, index=False)
        logger.info(f"Submission file '{submission_file}' created successfully.")

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise


if __name__ == "__main__":
    main()
