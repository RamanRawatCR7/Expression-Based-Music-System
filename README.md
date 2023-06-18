# Emotion Detection using AI

This project focuses on emotion detection using Artificial Intelligence (AI) techniques. It leverages deep learning models to recognize facial expressions and classify them into different emotions.

## Dataset

The dataset used for this project is sourced from Kaggle's "Challenges in Representation Learning: Facial Expression Recognition Challenge". You can find the dataset at the following link: [Kaggle Dataset](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data)

## Usage

1. **Training**: To train the emotion detection model, use the `train.py` file. You may need to modify the code to suit your requirements, such as changing the number of classes based on your specific use case. Experiment with different pre-trained models to find the one that works best for your needs.

2. **Testing**: Execute the `test.py` file to run the emotion detection system. This script will utilize the trained model to recognize emotions in real-time or on provided input data.

## To run the Django web application

```python manage.py runserver```

This command starts the development server, and the web application will be accessible at http://localhost:8000 by default. Remember to grant permission to access your camera when prompted by the browser. Press Ctrl + C in the terminal to stop the server.

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository:

```git clone https://github.com/your-username/emotion-detection-ai.git
```

2. Install the necessary dependencies:

```pip install -r requirements.txt
```

3. Prepare the dataset:

   a. Download the dataset from the Kaggle link mentioned above.
   
   b. Extract the dataset files and place them in the appropriate directory within the project structure.
   
   c. Perform any necessary preprocessing steps on the dataset if required.

4. Train the model:

   a. Modify the `train.py` file to suit your specific requirements, such as adjusting hyperparameters or selecting a different pre-trained model.
   
   b. Run the training script:
   
```python train.py
```

c. Monitor the training process and adjust parameters as needed.

5. Test the model:

a. Utilize the `test.py` script to run the emotion detection system on real-time data or provided input.

```python test.py
```

b. Evaluate the performance of the model and analyze the emotion detection results.

## Contributing

Contributions to this project are welcome. If you find any issues or have ideas for improvements, please feel free to open an issue or submit a pull request. Your contributions can help enhance the accuracy and effectiveness of the emotion detection system.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute the codebase as per the terms of the license.

Enjoy exploring the exciting world of AI-powered emotion detection!

