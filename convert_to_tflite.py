import torch
import onnx
from onnx_tf.backend import prepare
import tensorflow as tf
import os

def convert_pytorch_to_tflite(model, dummy_input_shape, tflite_model_path):
    """
    Converts a PyTorch model to TensorFlow Lite format.

    Args:
        model (torch.nn.Module): The PyTorch model to be converted.
        dummy_input_shape (tuple): Shape of the dummy input used for tracing (e.g., (1, 3, 64, 64) for CIFAR-10 with AlexNet).
        tflite_model_path (str): File path to save the converted .tflite model.
    """
    # Step 1: Export the PyTorch model to ONNX
    onnx_model_path = "temp_model.onnx"
    dummy_input = torch.randn(dummy_input_shape)  # Create a dummy input tensor

    # Export the model to ONNX format
    torch.onnx.export(
        model,                   # PyTorch model to export
        dummy_input,             # Dummy input tensor
        onnx_model_path,         # File path to save the ONNX model
        opset_version=11,        # ONNX version to export
        input_names=['input'],   # Input names for the model
        output_names=['output'], # Output names for the model
    )

    # Step 2: Convert the ONNX model to TensorFlow
    onnx_model = onnx.load(onnx_model_path)  # Load the ONNX model
    tf_rep = prepare(onnx_model)             # Convert ONNX model to TensorFlow representation

    # Save the TensorFlow model in .pb format temporarily
    tf_model_path = "temp_model.pb"
    tf_rep.export_graph(tf_model_path)

    # Step 3: Convert the TensorFlow model to TensorFlow Lite
    converter = tf.lite.TFLiteConverter.from_saved_model(tf_model_path)  # Load the TensorFlow model
    tflite_model = converter.convert()  # Convert the model to TensorFlow Lite format

    # Step 4: Save the .tflite model to the specified path
    with open(tflite_model_path, "wb") as f:
        f.write(tflite_model)

    # Clean up temporary files
    os.remove(onnx_model_path)
    os.remove(tf_model_path)

    print(f"Model successfully converted to {tflite_model_path}")
