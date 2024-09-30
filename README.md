# Real-Time Traffic-Based Navigation

This Python application provides real-time traffic-based navigation using the Google Maps Directions API. It dynamically adjusts the route based on current traffic conditions.

## Features:
- Fetches route information including distance, duration, and detailed directions
- Takes traffic into account for more accurate travel time
- Command-line interface for entering origin and destination
- Environment variables for secure API key management

## Requirements:
- Python 3.x
- Google Maps Directions API key

## Installation:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/real_time_traffic_navi.git
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
   python main.py "New York, NY" "Boston, MA"
   ```

## License:
This project is licensed under the MIT License.
