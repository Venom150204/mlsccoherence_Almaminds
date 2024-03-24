**Speech-to-Speech Recognition Chatbot with Customer Virtual Assistant**

**Author:**

**Vijesh Hingu**

**Bhoomika Singh**

**Rohit Mondal**

**Dhruv Patel**

**Team Name:**    **Almaminds**

**Description:**

This project builds a user-friendly speech-to-speech chatbot that
functions as a customer virtual assistant (CVA). It leverages natural
language processing techniques and machine learning to provide a
seamless interactive experience. This speech-to-speech customer virtual
assistant is designed to help businesses manage and rectify
order-related queries effectively. By leveraging speech recognition and
synthesis technologies, it enables seamless communication between
customers and the e-commerce platform.

**Features:**

-   **Speech Recognition:** Captures user input using Google
    Speech-to-Text API.

-   **Text Classification:** Classifies user intent using TF-IDF
    vectorization and an SVM classifier trained on a labelled dataset.

-   **Response Generation:** Generates appropriate responses based on
    user intent, using the pre-trained model created from the dataset.
    The model maps classified intents to corresponding responses in the
    knowledge base.

-   **Text-to-Speech:** Converts chatbot responses to audio output using
    Google Text-to-Speech API.

-   **User Interface:** Provides an intuitive front-end built with HTML,
    CSS, and Bootstrap for user interaction.

**Technologies Used:**

-   **Backend:**

    -   Python

    -   TensorFlow (for TF-IDF vectorization)

    -   scikit-learn (for SVM classification)

    -   Flask (for web framework)

-   **Natural Language Processing (NLP):**

    -   TF-IDF Vectorization

-   **Machine Learning:**

    -   Support Vector Machine (SVM) Classification

-   **Speech Services:**

    -   Google Speech-to-Text API

    -   Google Text-to-Speech API

-   **Front-end:**

    -   HTML

    -   CSS

    -   Bootstrap

**Installation:**

1.  **Prerequisites:**

    -   Ensure you have Python (version 3.x recommended) and pip
        (package manager) installed.

    -   Install required libraries:

> Bash
>
> pip install speech_recognition tensorflow scikit-learn flask
> Flask-Bootstrap

2.  **Clone or Download Project:**

    -   Clone the project repository using Git:

> Bash
>
> git clone https://github.com/\<your-username\>/\<project-name\>.git

-   Or, download the project files manually.

3.  **Unzip** the **Joblib** model and place it into the **root** directory  

4.  **Run the App:**

    -   Navigate to the project directory.

    -   Set up your Flask app (refer to Flask documentation for specific
        configuration).

    -   Start the development server:

> Bash
>
> python app.py

-   Access the chatbot in your web browser at http://localhost:5000/ (or
    the port you specified).

**Usage:**

1.  **Speak to the chatbot:**

    -   Use your microphone to interact with the chatbot.

    -   Clearly state your questions or requests.

2.  **Chatbot Response:**

    -   The chatbot will analyze your speech, classify your intent, and
        generate an appropriate response.

    -   The response will be both displayed on the screen and spoken
        aloud through your speakers.

**Additional Notes:**

-   You\'ll need to set up API keys for Google Speech-to-Text and
    Text-to-Speech services (refer to their documentation).

-   The pre-trained SVM model must be included in the project directory
    (or loaded dynamically).

-   The knowledge base for response generation should be well-defined
    and accessible to the chatbot.

-   Consider implementing error handling and logging for a more robust
    system.

**Further Development:**

-   Enhance the chatbot\'s capabilities with additional language models
    or deep learning techniques.

-   Integrate with external APIs or services to provide more dynamic
    responses.

-   Explore advanced NLP techniques for sentiment analysis or topic
    modeling.

-   Refine the user interface design and responsiveness.

-   Implement error handling and logging for a production-ready system.
