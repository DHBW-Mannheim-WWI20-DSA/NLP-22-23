import pathlib
from typing import Union
import tensorflow as tf
import pandas as pd


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
        data = pd.Series([metadata_content, email_content])
        full_model_path = pathlib.Path.joinpath(path_to_model, "rnn_model_meta.tf")
    else:
        data = pd.Series(email_content)
        full_model_path = pathlib.Path.joinpath(path_to_model, "rnn_model.tf")
        
    # Load module
    model = tf.keras.models.load_model(full_model_path, compile=True)

    # Predict
    prediction = model.predict(data, verbose=1)
    print(prediction[0][0])
    return prediction[0][0]


if __name__ == '__main__':
    predict_Spam_RNN(
        email_content="Hello, could you please send me the report ?",
        metadata_content="This is a test metadata",
        path_to_model=pathlib.Path.joinpath(pathlib.Path.cwd(), "models", "text", "RNN"),
        metadata_used=False
    )
