# Booking Bot 🏨🤖

A Python automation tool that scrapes hotel information from Booking.com using Selenium WebDriver. The bot searches for hotels based on your criteria and displays results in a formatted table sorted by price.

## ✨ Features

- 🔍 **Automated Hotel Search**: Searches Booking.com with your specified criteria
- 💱 **Currency Selection**: Automatically sets currency to USD
- 📊 **Smart Filtering**: Filters hotels by star rating (3, 4, and 5 stars)
- 📈 **Price Sorting**: Results automatically sorted by price (lowest first)
- 💻 **Interactive CLI**: Simple prompts for destination, dates, and guest count
- 📋 **Formatted Output**: Clean table display with hotel names, prices, and ratings
- 🕵️ **Stealth Mode**: Advanced anti-detection features to avoid bot blocking

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/davitty/booking-bot.git
   cd booking-bot
   ```

2. **Install dependencies**
   ```bash
   pip install selenium prettytable
   ```

3. **Setup ChromeDriver**
   - Download ChromeDriver from [here](https://chromedriver.chromium.org/)
   - Place it in `C:\SeleniumDrivers` (Windows) or update the path in `booking.py`

4. **Run the bot**
   ```bash
   python run.py
   ```

## 📋 Prerequisites

- **Python 3.7+**
- **Google Chrome** browser
- **ChromeDriver** (compatible with your Chrome version)

## 🛠 Installation

### Method 1: Manual ChromeDriver Setup
1. Download ChromeDriver matching your Chrome version
2. Create folder `C:\SeleniumDrivers` (Windows) or update path in code
3. Extract ChromeDriver to this folder
4. Install Python dependencies:
   ```bash
   pip install selenium prettytable
   ```

### Method 2: Using PATH
1. Add ChromeDriver to your system PATH
2. Install dependencies:
   ```bash
   pip install selenium prettytable
   ```

## 💡 Usage

1. **Run the script**:
   ```bash
   python run.py
   ```

2. **Enter your search criteria** when prompted:
   ```
   Where you want to go: Paris
   Check in Date: (yyyy/mm/dd) 2024/12/15
   Check Out Date: (yyyy/mm/dd) 2024/12/18
   How many people? : 2
   ```

3. **View Results**: The bot will display hotels in a formatted table

## 📊 Sample Output

```
+---------------------------+------------+-------+
|        Hotel Name         |   Price    | Score |
+---------------------------+------------+-------+
| Hotel Malte Opera         | US$89      | 8.2   |
| Hotel des Grands Boulevards| US$124     | 8.7   |
| Le Marais Hotel           | US$156     | 8.5   |
| ...                       | ...        | ...   |
+---------------------------+------------+-------+
```

## 📁 Project Structure

```
booking-bot/
├── run.py                    # Main execution script
├── booking/
│   ├── __init__.py          # Package initializer
│   ├── booking.py           # Main Booking class with automation logic
│   ├── booking_filtration.py# Filter application (star rating, price sorting)
│   ├── booking_report.py    # Data extraction and formatting
│   └── constants.py         # Configuration constants
└── README.md                # This documentation
```

## 🔧 Code Architecture

### Main Components

- **`run.py`**: Entry point with user input handling and error management
- **`Booking` class**: Core automation logic extending Chrome WebDriver
- **`BookingFiltration`**: Applies filters (star ratings, price sorting)
- **`BookingReport`**: Extracts and formats hotel data

### Key Features Implementation

- **Anti-Detection**: Incognito mode, custom user agent, automation flag removal
- **Smart Waiting**: WebDriverWait for reliable element interactions  
- **Robust Filtering**: Automatic 3-5 star filtering and price sorting
- **Data Extraction**: Clean parsing of hotel names, prices, and ratings

## ⚙ Configuration

You can customize the bot by modifying these files:

### `constants.py`
```python
BASE_URL = "https://www.booking.com/"
```

### `booking.py` - ChromeDriver Path
```python
def __init__(self, driver_path=r"C:\SeleniumDrivers"):
```

### `booking_filtration.py` - Star Rating Filter
```python
filters.apply_star_rating(3,4,5)  # Modify star ratings as needed
```

## 🐛 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| **ChromeDriver not found** | Ensure ChromeDriver is in `C:\SeleniumDrivers` or system PATH |
| **PATH error** | Follow the PATH setup instructions displayed in the error |
| **Element not found** | Booking.com layout may have changed - check selectors |
| **Bot detection** | The bot includes anti-detection measures, but delays may help |

### Error Messages

**ChromeDriver PATH Error**: The script provides specific instructions:
```
Windows: set PATH=%PATH%;C:path-to-your-folder
Linux: PATH=$PATH:/path/toyour/folder/
```

### Date Format
Use the exact format: `yyyy/mm/dd` (e.g., `2024/12/15`)

## 🎯 How It Works

1. **Initialization**: Launches Chrome with anti-detection settings
2. **Navigation**: Goes to Booking.com and handles popups
3. **Currency**: Sets currency to USD
4. **Search Setup**: Enters destination, dates, and guest count
5. **Filtering**: Applies 3-5 star filter and sorts by lowest price
6. **Data Extraction**: Scrapes hotel names, prices, and ratings
7. **Display**: Shows results in a formatted table using PrettyTable

## ⚖ Legal & Ethics

- ✅ **Educational Purpose**: This tool is for learning web automation
- ⚠ **Respect ToS**: Use responsibly and follow Booking.com's terms of service
- 🚦 **Rate Limiting**: Includes delays to avoid overloading servers
- 👤 **Personal Use**: Intended for individual, non-commercial use only

## 🤝 Contributing

Contributions are welcome! Areas for improvement:

- Add more filter options (price range, amenities)
- Implement headless mode option
- Add support for different currencies
- Improve error handling and recovery
- Add data export functionality

## 📦 Dependencies

- **selenium**: Web automation framework
- **prettytable**: Formatted table output
- **Chrome Browser**: Required for ChromeDriver

## 📝 Requirements.txt

Create a `requirements.txt` file:
```
selenium>=4.0.0
prettytable>=3.0.0
```

Install with:
```bash
pip install -r requirements.txt
```

## 📞 Support

- 🐛 **Issues**: [GitHub Issues](https://github.com/davitty/booking-bot/issues)
- 💬 **Questions**: Open an issue for help
- 🔧 **ChromeDriver Help**: [ChromeDriver Documentation](https://chromedriver.chromium.org/)

---

⭐ **If you find this project helpful, please give it a star!** ⭐

---

**Disclaimer**: This bot is for educational purposes only. Please use responsibly and in accordance with Booking.com's terms of service. The author is not responsible for any misuse of this tool.
