# Hearing Aid Finder Application

This project is a Python-based application designed to help users find and identify hearing aids based on their brand, family, model, and technology level using Airtable as the backend database.

---

## Features
- **Access Hearing Aid Data**: Fetch data from an Airtable database including brands, families, models, and technology levels of hearing aids.
- **Interactive Search**: Step-by-step guidance to select the hearing aid details (brand → family → model → technology level).
- **User-Friendly Output**: Displays the user's final hearing aid choice in a simple, readable format.

---

## Prerequisites
Before running the application, ensure you have:
- **Python 3.7+** installed.
- The following Python libraries installed:
  - `pyairtable`
  - `json`
- Access to an Airtable database with the following tables:
  - `Hearing Aids`
  - `Couplings`
  - `Electroacoustics`
  - `Fitting Ranges`
  - `Brands`
- An Airtable API key with access to the required tables.

---

## Setup Instructions
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/hearing-aid-finder.git
   cd hearing-aid-finder
   ```

2. **Install Required Dependencies**
   Use `pip` to install the dependencies:
   ```bash
   pip install pyairtable
   ```

3. **Set Your Airtable API Key and Base ID**
   - Replace the placeholders `api_key` and `base_id` in the script with your Airtable API key and base ID:
     ```python
     base_id = 'your_airtable_base_id'
     api_key = 'your_airtable_api_key'
     ```

4. **Run the Application**
   Execute the script:
   ```bash
   python main.py
   ```

---

## How to Use
1. Start the application.
2. Select a hearing aid **brand** from the provided list.
3. Choose a **family** from the available options.
4. Pick a **model** under the chosen family.
5. If applicable, select a **technology level** for the hearing aid.
6. View the final selection.

---

## Code Overview
- **Airtable Connection**: Uses the `pyairtable` library to fetch data from the Airtable API.
- **Functions**:
  - `find_all_families(brand)`: Retrieves all families for a given brand.
  - `find_all_models(family)`: Fetches all models for a specific family.
  - `find_all_tech_lvls(family, model)`: Retrieves all technology levels for a given family and model.
  - `find()`: Main function to guide the user through the selection process.
- **Error Handling**: Handles missing fields gracefully, ensuring a smooth user experience.

---

## Example Output
```plaintext
Hello, this is how you can find your hearing aid!

Hearing Aid Brands:
- Brand A
- Brand B

please select your brand, please type exactly as it is: Brand A

searching families...

Possible Families:
- Family 1
- Family 2

please select your family, please type exactly as it is: Family 1

searching models...

Possible Models:
- Model X
- Model Y

please select your model, please type exactly as it is: Model X

searching technology levels...

Possible Technology Levels:
- Level 1
- Level 2

please select your technology level, please type exactly as it is: Level 1

your hearing aid is: Brand A Family 1 Model X Level 1
```

---

## Future Enhancements
- Add more robust error handling and validation for user inputs.
- Extend the database to include more detailed specifications and features of hearing aids.
- Develop a GUI-based version for easier user interaction.
- Support for additional search criteria (e.g., price range, compatibility).

---

## Contributions
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

---

## Contact
For any questions or suggestions, feel free to contact [your-email@example.com](mailto:your-email@example.com).
