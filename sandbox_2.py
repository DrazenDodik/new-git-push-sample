import valohai

valohai.prepare(
    step= "train-model",
    image="tensorflow/tensorflow:2.6.0",
    default_parameters={
        "batch_size": 32,
        "image_width": 160,
        "image_height": 160,
        "image_channels": 3,
        "learning_rate": 0.0001,
        "metrics": "accuracy",
        "epochs": 5
    },
    default_inputs={
        "dataset": "https://valohaidemo.blob.core.windows.net/mnist/preprocessed_mnist.npz"
    }
)