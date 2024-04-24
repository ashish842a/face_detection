#!/bin/bash

cat <<EOF >README.md
# Face Detection Project

This project is a simple face detection application using OpenCV in Python. It captures video from a camera, detects faces in each frame, and attempts to recognize them using LBPH Face Recognizer.

## Installation

To run this project, you need to have Python installed on your system along with the necessary libraries. You can install the required libraries using pip:

\`\`\`bash
pip install opencv-contrib-python==4.9.0.80
\`\`\`

## Usage

1. Clone this repository to your local machine:

\`\`\`bash
git clone https://github.com/your_username/face-detection-project.git
\`\`\`

2. Navigate to the project directory:

\`\`\`bash
cd face-detection-project
\`\`\`

3. Run the Python script:

\`\`\`bash
python face_detection.py
\`\`\`

4. Press 'q' to quit the application.

## Project Structure

- \`face_detection.py\`: The main Python script for face detection.
- \`Trainer.yml\`: The trained model for face recognition.
- \`haarcascade_frontalface_default.xml\`: Haar cascade file for face detection.
- \`background.png\`: Background image for displaying the detected faces.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
EOF
