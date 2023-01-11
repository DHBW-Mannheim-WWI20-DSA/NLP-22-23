import pathlib
from typing import Union
import tensorflow as tf
import numpy as np
import autokeras as ak


# Define Function to Predict Spam
def predict_Spam_transformer(email_content: Union[str, None], metadata_content: Union[str, None],
                             path_to_model: pathlib.Path, metadata_used: Union[bool, None]):
    """
    Predicts if an email is spam or not using the Transformer model.
    :param email_content:
    :param metadata_content:
    :param path_to_model:
    :param metadata_used:
    :return:
    """
    # Load Model
    full_model_path = pathlib.Path.joinpath(path_to_model, "transformer-metadata.tf")
    model = None

    # Prepare Data
    if metadata_used:
        data = np.array([email_content, metadata_content])
    else:
        data = np.array([email_content])


if __name__ == '__main__':
    predict_Spam_transformer(
        email_content="Hello, this is a test email",
        metadata_content="This is a test metadata",
        path_to_model=pathlib.Path.joinpath(pathlib.Path.cwd(), "models", "meta", "Transformer"),
        metadata_used=True
    )
