# eVisitor Card
eVisitor Card digitizes the visitor check-in to the office premises. This solution sends the authorization code (QRCode) to visitor and when visitor visits the office he/she can show the code and this digital worker validates the visitor entry based on authorization code and if the visitor is authorized to enter in office digital worker takes the photo and sends the entry card to the visitor over email.  


# Prerequisites
1. Install Python (including pip) using the provided installation kit in the Prerequisites folder, Make sure "Add PythonXX to PATH" check box is checked while installing
2. Open cmd (Win+R) and type "python", If python version is displayed means python PATH is set properly skip step 3 in this case
3. Add the Python paths to your PATH system environment variable (You can find your PATH variable by going to My Computer > Properties > Advanced System Settings > Environment Variables > System Variables > Path). Click on Edit and add the following paths, replacing "YOUR_USERNAME" with your Windows username:
    - C:\Users\YOUR_USERNAME\AppData\Local\Programs\Python\Python36
    - C:\Users\YOUR_USERNAME\AppData\Local\Programs\Python\Python36\Scripts	
4. Run install.bat in the Prerequisites folder
5. Provide Python path (C:\Users\YOUR_USERNAME\AppData\Local\Programs\Python\Python36) in config.csv 

# Installation Steps
1. Install UIPath Studio
2. Open Main.xaml in UIPath Studio, goto Manage Packages and install dependences : UIPath.Form.Activities, UIPath.Python.Activities, UIPath.GSuite.Activities
3. Run the framework from the Main.xaml workflow inside UIPath Studio