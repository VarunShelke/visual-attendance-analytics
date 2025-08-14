# Visual Attendance Analytics using Face Recognition (VAAFR)

A comprehensive automated attendance management system that uses computer vision and face recognition technology to track student attendance in real-time. The system provides a complete solution for educational institutions to manage attendance efficiently with detailed analytics and reporting capabilities.

## 📋 Project Description

The Visual Attendance Analytics using Face Recognition system is designed to automate the traditional attendance marking process in educational institutions. The system uses OpenCV for face detection and recognition, combined with a user-friendly GUI built with Tkinter. It maintains detailed attendance records in CSV format and provides comprehensive analytics through visual charts and reports.

### Key Features

- **Real-time Face Recognition**: Automated face detection and recognition using OpenCV and Haar Cascades
- **Intelligent Scheduling**: Time-based lecture scheduling with automatic subject detection
- **Comprehensive Analytics**: Detailed attendance reports with percentage calculations
- **Multi-user Interface**: Separate interfaces for administrators, teachers, and students
- **Data Visualization**: Graphical representation of attendance data using Matplotlib
- **Secure Authentication**: Password-protected admin access
- **CSV Data Management**: Persistent data storage with automatic updates
- **Subject-wise Tracking**: Individual tracking for multiple subjects (TOC, DBMS, SEPM, ISEE, CN, SDL)

## 🛠️ Technologies Used

### Core Technologies
- **Python 3.x**: Primary programming language
- **OpenCV (cv2)**: Computer vision library for face detection and recognition
- **Tkinter**: GUI framework for user interface
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing support
- **Matplotlib**: Data visualization and plotting

### Additional Libraries
- **Pillow (PIL)**: Image processing capabilities
- **Pickle**: Data serialization for model storage
- **DateTime**: Time-based functionality for scheduling

### Machine Learning Components
- **LBPH Face Recognizer**: Local Binary Pattern Histogram for face recognition
- **Haar Cascade Classifiers**: Pre-trained models for face detection
- **Custom Training Pipeline**: Automated model training from image datasets

## 📁 Project Structure

```
visual-attendance-analytics/
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
├── howtoexecute.txt            # Execution instructions
│
├── Core Application Files
├── test.py                     # Main application entry point
├── gui.py                      # Alternative GUI implementation
├── face_recognition.py         # Face recognition model training
├── face_detection.py           # Real-time face detection and recognition
│
├── Attendance Management
├── gotoat.py                   # Attendance routing based on day/time
├── atstud.py                   # Student attendance functions
├── day.py                      # Day-wise attendance management
├── atten.py                    # Student attendance display
├── sub.py                      # Subject-wise attendance reports
│
├── Data Files
├── TE2.csv                     # Main attendance database
├── trainner.yml                # Trained face recognition model
├── labels.pickle               # Face recognition labels
│
├── Resources
├── Haar/                       # Haar cascade classifiers
│   └── haarcascade_frontalcatface.xml
└── Images/                     # Student face image datasets
    ├── 305110/                 # Student ID folders
    ├── 305150/
    ├── 305159/
    ├── 305129/
    ├── 305184/
    ├── 305165/
    └── 305112/
```

## 🚀 How to Setup

### Prerequisites

Ensure you have Python 3.6 or higher installed on your system.

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/visual-attendance-analytics.git
cd visual-attendance-analytics
```

### Step 2: Install Required Dependencies

```bash
pip install opencv-python
pip install pandas
pip install numpy
pip install pillow
pip install matplotlib
pip install pickle-mixin
```

Or install from requirements file:
```bash
pip install -r requirements.txt
```

### Step 3: Prepare Student Images

1. Create folders in the `Images/` directory with student roll numbers as folder names
2. Add 50-100 clear face images of each student in their respective folders
3. Ensure images are in JPG or PNG format
4. Images should have good lighting and clear face visibility

### Step 4: Train the Face Recognition Model

```bash
python face_recognition.py
```

This will:
- Process all images in the Images directory
- Create face encodings for each student
- Generate `trainner.yml` (trained model) and `labels.pickle` (label mappings)

### Step 5: Setup Attendance Database

Ensure the `TE2.csv` file contains the correct student information with the following columns:
- Sr. No., PRN, Status, Roll No., Name
- Subject columns: TOC, DBMS, SEPM, ISEE, CN, SDL
- Lecture count columns: TOC_LEC, DBMS_LEC, etc.
- Percentage columns: TOC%, DBMS%, etc.
- Status columns: TOC_STAT, DBMS_STAT, etc.

### Step 6: Run the Application

```bash
python test.py
```

## 💻 Usage Instructions

### Administrator Login
1. **Username**: `gaurav`
2. **Password**: `imgaurav`
3. **Day**: Enter the current day (monday, tuesday, wednesday, thursday, friday)

### Main Features

#### 1. Student Login
- Enter student roll number to view individual attendance records
- Displays subject-wise attendance with visual charts
- Shows attendance percentages and total lectures attended

#### 2. Teacher Login
- Enter subject name to view class-wide attendance for that subject
- Displays comprehensive attendance reports for all students
- Provides subject-specific analytics

#### 3. Go For Attendance
- Activates the camera for real-time face recognition
- Automatically detects and recognizes student faces
- Marks attendance based on current day and time schedule
- Prevents duplicate attendance marking

### Time Schedule

The system follows a predefined lecture schedule:

**Monday**:
- 8:45-9:45: ISEE
- 9:45-10:45: TOC

**Tuesday**:
- 11:00-12:00: TOC
- 12:00-13:00: ISEE
- 14:00-15:00: SDL
- 15:00-16:00: DBMS
- 16:00-17:00: CN

**Wednesday**:
- 11:00-12:00: SEPM
- 12:00-13:00: DBMS
- 14:00-15:00: CN
- 15:00-16:00: TOC
- 16:00-17:00: ISEE

**Thursday**:
- 14:00-15:00: SEPM
- 15:00-16:00: DBMS
- 16:00-17:00: CN

**Friday**:
- 8:45-9:45: CN
- 9:45-10:45: SEPM
- 11:00-12:00: SDL
- 12:00-13:00: TOC

## 📊 Features in Detail

### Face Recognition System
- Uses LBPH (Local Binary Pattern Histogram) algorithm
- Confidence threshold of 55% for accurate recognition
- Real-time processing with OpenCV
- Automatic face detection using Haar Cascades

### Attendance Management
- Automatic attendance marking based on face recognition
- Time-based lecture detection
- Duplicate attendance prevention
- Real-time percentage calculations

### Data Analytics
- Subject-wise attendance tracking
- Individual student performance analysis
- Class-wide attendance reports
- Visual charts and graphs using Matplotlib
- Exportable attendance data

### Security Features
- Password-protected administrator access
- Secure face recognition with confidence thresholds
- Data integrity checks
- Audit trail for attendance modifications

## 🔧 Configuration

### Modifying Time Schedule
Edit the time slots in `gotoat.py`:
```python
a=datetime.time(8,45,0,0)  # Lecture start time
b=datetime.time(9,45,0,0)  # Lecture end time
```

### Adjusting Recognition Confidence
Modify the confidence threshold in `face_detection.py`:
```python
if conf>=55:  # Adjust this value (0-100)
```

### Adding New Subjects
1. Update the CSV structure in `TE2.csv`
2. Add corresponding functions in `atstud.py`
3. Update the scheduling logic in `gotoat.py`

## 🐛 Troubleshooting

### Common Issues

1. **Camera not working**:
   - Check if camera is connected and not used by other applications
   - Verify OpenCV installation: `python -c "import cv2; print(cv2.__version__)"`

2. **Face not recognized**:
   - Ensure sufficient training images (50+ per person)
   - Check lighting conditions during recognition
   - Verify model training completed successfully

3. **CSV file errors**:
   - Ensure CSV file is not open in other applications
   - Check file permissions
   - Verify CSV structure matches expected format

4. **Import errors**:
   - Install missing dependencies: `pip install [package-name]`
   - Check Python version compatibility

### Performance Optimization

- Use high-quality training images
- Ensure consistent lighting conditions
- Regular model retraining with new images
- Optimize camera resolution for better performance

## 📈 Future Enhancements

- **Database Integration**: MySQL/PostgreSQL support
- **Web Interface**: Flask/Django web application
- **Mobile App**: Android/iOS companion app
- **Cloud Storage**: AWS/Google Cloud integration
- **Advanced Analytics**: Machine learning insights
- **Multi-camera Support**: Multiple classroom monitoring
- **Facial Mask Detection**: COVID-19 compliance features
- **API Integration**: RESTful API for external systems

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **SHREE** - Initial development and core functionality
- **Contributors** - See [CONTRIBUTORS.md](CONTRIBUTORS.md) for the list of contributors

## 🙏 Acknowledgments

- OpenCV community for computer vision libraries
- Python community for excellent documentation
- Educational institutions for testing and feedback
- Open source contributors for various libraries used

## 📞 Support

For support and questions:
- Create an issue on GitHub
- Email: [your-email@example.com]
- Documentation: [Wiki](https://github.com/your-username/visual-attendance-analytics/wiki)

---

**Note**: This system is designed for educational purposes and should be used in compliance with privacy laws and institutional policies regarding biometric data collection and storage.
