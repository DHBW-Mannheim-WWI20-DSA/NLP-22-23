import pathlib
from typing import Union
import tensorflow as tf
import pandas as pd

import asyncio


# Define Function to Predict Spam
async def predict_Spam_RNN(email_content: Union[str, None], path_to_model: pathlib.Path):
    """
    Predicts if an email is spam or not using a RNN model.
    :param email_content:
    :param path_to_model:
    :return:
    """
    # Prepare Data and find appropiate model
    data = pd.Series(email_content)
    full_model_path = pathlib.Path.joinpath(path_to_model, "rnn_model_combined.tf")
    # Load module
    model = tf.keras.models.load_model(full_model_path)

    # Predict
    prediction = model.predict(data, verbose=0)

    print(prediction[0][0])
    return prediction[0][0]


if __name__ == '__main__':
    asyncio.run(predict_Spam_RNN(
        email_content="Hello, could you please send me the report?",
        path_to_model=pathlib.Path.joinpath(pathlib.Path.cwd()),
    ))
