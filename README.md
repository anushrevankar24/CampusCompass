
# Campus Compass

The Campus Compass project aims to create a web-based navigation system for university campuses, allowing users to input their current and final destinations to find the shortest path. The system utilizes Python, FastAPI, and Folium maps to create an interactive navigation experience.

## Features
- **User Interface:** Provides a user-friendly interface allowing users to input their current and final destinations within the campus.
- **Shortest Path Calculation:** Utilizes Dijkstra's algorithm to calculate the shortest path between specified locations.
- **Map Visualization:** Integrates Folium maps to display the calculated shortest path visually on an interactive map.


## Application Usage
Open your browser and navigate to http://127.0.0.1:8000/ to access the Campus Compass.
Input the current and final destination within the campus.
Click on the "Find Path" button to generate and view the shortest path on the interactive map.

## File Descriptions
**main.py**: Contains the main code for the FastAPI application.
**coordinates_2.xlsx**: Excel file storing campus layout data.
**templates/index.html**: HTML file for the user interface.
**static/background.jpg**: Image used in the interface.

## Technologies Used
Python\
FastAPI\
Pandas\
Folium

## Folder Structure:

CampusCompass/\
├── main.py\
├── coordinates.xlsx\
├── templates/\
│   └── index.html\
├── static/\
│   └── background.jpg


## Local Setup Instructions
1. **Clone this repository**.

2. **Environment Setup:**
   - Ensure Python is installed on your system.
   - Create a virtual environment using:
     ```
     python -m venv campus_compass_env
     ```
   - Activate the virtual environment:
     - For Windows:
       ```
       campus_compass_env\Scripts\activate
       ```
     - For macOS/Linux:
       ```
       source campus_compass_env/bin/activate
       ```

2. **Install Dependencies:**

   - Install required packages using the provided requirements.txt file:
     ```
     pip install -r requirements.txt
     ```
3. **Running the Application:**

To start the Campus Compass application locally, follow these steps:

1. Ensure the virtual environment is activated.

2. Run the following command in the terminal of your preferred IDE (VSCode, for example) to start the FastAPI server:

    ```
    uvicorn main:app --reload 
    ```

3. Access the application through a web browser at `http://localhost:8000/`.

This command initializes the FastAPI server, enabling access to the Campus Compass functionalities. Any changes made to the code will trigger an automatic reload, ensuring seamless development and testing.

## Contributors
- [Anush Revankar](https://github.com/anushrevankar24) -221AI009

## Contributing

We welcome contributions from the community to enhance the Campus Compass project. Here's how you can contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/awesome-contribution`).
3. Make your changes and ensure the code follows the project's coding conventions.
4. Test your changes thoroughly.
5. Commit your changes (`git commit -am 'Add some feature'`).
6. Push to the branch (`git push origin feature/awesome-contribution`).
7. Create a new Pull Request.

Please ensure your Pull Request description clearly describes the changes made and any associated issues.

### Code Style

Before submitting a Pull Request, make sure your code follows the project's coding standards. We adhere to the following guidelines:
- Indentation: [Spaces / Tabs]
- Variable naming: [camelCase / snake_case]
- etc.

### Bug Reports and Feature Requests

If you encounter any bugs or have suggestions for new features, please open an issue in the GitHub repository.

### Contact

If you have any questions or need further clarifications, feel free to contact the maintainers or contributors.


Your contributions are highly appreciated!

## License
This project is licensed under [License Name]. For more details, see the [LICENSE](./LICENSE) file.


  


