import pathlib
from typing import Union
import tensorflow as tf
import pandas as pd

import asyncio


# Define Function to Predict Spam
async def predict_Spam_RNN(email_content: Union[str, None], metadata_content: Union[str, None],
                             path_to_model: pathlib.Path, metadata_used: Union[bool, None]):
    """
    Predicts if an email is spam or not using a RNN model.
    :param email_content:
    :param metadata_content:
    :param path_to_model:
    :param metadata_used:
    :return:
    """
    # Prepare Data and find appropiate model
    if metadata_used:
        data = pd.DataFrame([metadata_content, email_content])
        full_model_path = pathlib.Path.joinpath(path_to_model, "rnn_model_meta.tf")
    else:
        data = pd.Series(email_content)
        full_model_path = pathlib.Path.joinpath(path_to_model, "rnn_model.tf")
        
    print(full_model_path)
    # Load module
    model = tf.keras.models.load_model(full_model_path)

    # Predict
    prediction = model.predict(data, verbose=1)

    print(prediction)
    return prediction


if __name__ == '__main__':
    asyncio.run(predict_Spam_RNN(
        email_content="Hello, could you please send me the report ?",
        metadata_content="This is a test metadata",
        path_to_model=pathlib.Path.joinpath(pathlib.Path.cwd(), "Application", "models", "text", "RNN"),
        metadata_used=False
    ))
