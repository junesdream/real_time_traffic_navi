# Real-Time Traffic-Based Navigation

This Python application provides real-time traffic-based navigation using the Google Maps Directions API. It dynamically adjusts the route based on current traffic conditions.

## Features:
- Fetches route information including distance, duration, and detailed directions.
- Takes traffic into account for more accurate travel time.
- Command-line interface for entering origin and destination.
- Secure API key management using environment variables.
- Includes Continuous Integration (CI) setup with GitHub Actions.
- 
## Requirements:
- Python 3.x
- Google Maps Directions API key

## Installation:

1. Clone the repository:
   ```bash
   git clone https://github.com/junesdream/real_time_traffic_navi
   ```

2. Navigate into the project directory:
   ```bash
   cd real_time_traffic_navi
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your API key:
   ```
   API_KEY=your_google_maps_api_key
   ```

5. Run the application:
   ```bash
   python main.py "Seoul, South Korea" "Busan, South Korea"
   ```
   Or for different locations:
   ```bash
   python main.py "New York, NY" "Boston, MA"
   ```
## Example Output
   ```bash
From: Seoul, South Korea
To: Busan, South Korea
Distance: 401 km
Duration with traffic: 3 hours 44 mins

Directions:
1. Walk to Toegyero 3-ga Hanok Village Korea House
2. Bus towards Incheon International Airport T2-3FL
3. Walk to Seoul Station
4. Train towards Busan
5. Walk to Busan Station
6. Subway towards Yangjeong
   ```

## Environment Variables
The API key is stored in a .env file and should never be uploaded to version control. Make sure the .env file is included in the .gitignore file as follows:
  ```bash
.env
__pycache__/
*.pyc
  ```

## Continuous Integration (CI)
The project includes a GitHub Actions CI workflow located in .github/workflows/ci.yml. This workflow is triggered on every push or pull request to the main branch. It automatically installs dependencies and runs tests using the following Python versions:
- Python 3.8 
- Python 3.9 
- Python 3.1
You can customize the tests by editing the ci.yml file.

## Contributing
We welcome contributions to this project! Please follow the steps below:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear and concise messages.
4. Push your changes to your fork.
5. Open a Pull Request and describe the changes you made.

## Code Style
- Follow Python’s PEP 8 guidelines for code formatting. 
- Write descriptive commit messages. 
- Include tests for any new features or bug fixes.

## Reporting Issues
If you find a bug or have an idea for a new feature, please open an issue on GitHub. Make sure to provide as much detail as possible.

## License:
This project is licensed under the MIT License. See the LICENSE.md file for more details.
