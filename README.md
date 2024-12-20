# Human Card Project Documentation

## Project Overview
The Human Card project is an advanced user registration and authentication system designed to provide secure and efficient identity verification. It integrates modern web technologies and hardware interfaces, such as webcam photo capturing, to enhance user onboarding experiences. The system includes features like:

- **Human Card Registration**: Collect and store user details.
- **Profile Picture Capture**: Direct webcam access for capturing a profile photo.
- **Secure Authentication**: Ensure data security and user privacy.

This document provides a comprehensive guide to the project's architecture, functionality, and implementation.

---

## Features
1. **User Registration**:
   - Fields: Name, Email, Password, Address, etc.
   - Django forms are used for validation and data handling.
2. **Human Card Integration**:
   - Additional form for unique `humanID` and other related details.
3. **Profile Photo Capture**:
   - Utilizes the device's webcam to capture user profile pictures.
   - Stores the photo as a base64-encoded string for seamless backend processing.
4. **Responsive Design**:
   - Optimized for desktops and mobile devices.
   - Clean, user-friendly interface.
5. **Security**:
   - CSRF protection for form submissions.
   - Django’s secure password handling.

---

## Technical Stack

### Frontend
- **HTML**: Provides the structural markup for the web pages.
- **CSS**: For styling and layout, ensuring a responsive design.
- **JavaScript**: Implements the webcam and photo capture functionality.

### Backend
- **Django Framework**:
  - Handles user data processing and storage.
  - Implements forms and authentication logic.

### Database
- **SQLite/MySQL** (configurable): Stores user and Human Card data.

---

## Key Components

### 1. Forms
#### UserForm
Handles standard user data, such as:
- Name
- Email
- Password
- Address

#### HumanCardForm
Additional form for Human Card-related fields, such as:
- humanID
- Unique attributes of the Human Card.

---

### 2. Webcam Integration
- **JavaScript**: Accesses the user’s webcam using `navigator.mediaDevices.getUserMedia`.
- **Canvas API**: Captures and processes the webcam image.
- **Base64 Encoding**: Stores the captured image for backend submission.

### Implementation Details
1. Access the webcam:
   ```javascript
   navigator.mediaDevices.getUserMedia({ video: true })
       .then(stream => {
           video.srcObject = stream;
       })
       .catch(err => {
           console.error("Error accessing webcam: ", err);
           alert("Webcam access is required for profile photo capture.");
       });
   ```
2. Capture the photo:
   ```javascript
   captureButton.addEventListener('click', () => {
       const context = canvas.getContext('2d');
       canvas.width = video.videoWidth;
       canvas.height = video.videoHeight;
       context.drawImage(video, 0, 0, canvas.width, canvas.height);
       const dataURL = canvas.toDataURL('image/png');
       profilePicInput.value = dataURL; // Store the base64 image in the hidden input
   });
   ```

---

### 3. Backend Processing
#### Models
- **User**: Stores user-specific information like name, email, and password.
- **HumanCard**: Stores `humanID` and associated details.

#### Views
- **Registration View**:
  - Handles form rendering and submission.
  - Processes profile photo capture data.

#### Middleware
- Ensures secure and validated data submission.

---

## Installation and Setup

### Prerequisites
- Python 3.8+
- Django 4.0+
- SQLite/MySQL database
- Modern web browser with webcam support

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/username/human-card-project.git
   ```

2. Navigate to the project directory:
   ```bash
   cd human-card-project
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000`.

---

## Testing
### Unit Tests
- Write tests for form validation, model creation, and view responses.
- Example:
  ```python
  from django.test import TestCase
  from .models import HumanCard

  class HumanCardModelTest(TestCase):
      def test_human_card_creation(self):
          human_card = HumanCard.objects.create(humanID="12345", ...)
          self.assertEqual(human_card.humanID, "12345")
  ```

### Manual Testing
- Test the webcam capture on various devices and browsers.
- Verify responsive design on mobile and desktop.

---

## Future Enhancements
1. **Third-Party API Integration**:
   - Use external APIs for `humanID` validation.
2. **Cloud Storage**:
   - Store profile pictures in cloud storage instead of base64 encoding.
3. **Multi-Language Support**:
   - Add localization for wider accessibility.
4. **AI-Based Photo Validation**:
   - Integrate AI to validate captured photos for clarity and compliance.

---

## Conclusion
The Human Card project is a robust platform for user registration and identity management. By integrating modern technologies like webcam access and responsive design, it provides a seamless and secure user experience. This documentation serves as a guide for understanding, implementing, and enhancing the project.

