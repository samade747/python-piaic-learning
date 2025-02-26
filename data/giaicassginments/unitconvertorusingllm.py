import streamlit as st
import openai
import json
from pint import UnitRegistry

# Set your OpenAI API key here
openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your actual OpenAI API key

# Initialize the pint unit registry which supports various unit types.
ureg = UnitRegistry()

def parse_conversion_query(query):
    """
    Uses OpenAI's GPT-3.5-turbo to extract conversion details from a natural language query.
    The query can involve units such as length, temperature, weight, time, area, and others.
    
    Expected JSON output:
    {
      "value": 10,
      "source": "km",
      "target": "mile"
    }
    """
    prompt = (
        "Extract the numeric value, the source unit, and the target unit from the following conversion query.\n"
        "The query may involve units such as length, temperature, weight, time, area, and others.\n"
        "Return the result as a JSON object with keys 'value', 'source', and 'target'.\n"
        "For example, if the input is 'Convert 10 km to miles', then return:\n"
        '{"value": 10, "source": "km", "target": "mile"}\n'
        f"Query: {query}"
    )
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant that extracts conversion details from queries."},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )
        text = response['choices'][0]['message']['content']
        data = json.loads(text)
        return data
    except Exception as e:
        return {"error": str(e)}

def convert_units(value, source_unit, target_unit):
    """
    Performs the unit conversion using the pint library.
    Returns the converted value (magnitude) or None if the conversion fails.
    """
    try:
        quantity = value * ureg(source_unit)
        converted = quantity.to(target_unit)
        return converted.magnitude
    except Exception as e:
        print(e)
        return None

def unit_converter_app():
    st.header("Smart Unit Converter")
    st.write(
        "Enter your conversion query below. You can convert various unit types such as:\n\n"
        "- **Length:** e.g., Convert 10 km to miles\n"
        "- **Temperature:** e.g., Convert 100°F to °C\n"
        "- **Weight:** e.g., Convert 5 kg to lb\n"
        "- **Time:** e.g., Convert 2 hours to minutes\n"
        "- **Area:** e.g., Convert 50 m² to ft²\n"
        "- **Others:** Many more supported by pint"
    )
    
    query = st.text_input("Conversion Query", "")
    
    if st.button("Convert") and query:
        with st.spinner("Processing your query..."):
            conversion_details = parse_conversion_query(query)
            
            if "error" in conversion_details:
                st.error(f"Error parsing query: {conversion_details['error']}")
            else:
                value = conversion_details.get("value")
                source_unit = conversion_details.get("source")
                target_unit = conversion_details.get("target")
                
                if value is None or source_unit is None or target_unit is None:
                    st.error("Could not extract conversion details. Please try a different query.")
                else:
                    try:
                        value = float(value)
                        result = convert_units(value, source_unit, target_unit)
                        if result is not None:
                            st.success(f"{value} {source_unit} = {result} {target_unit}")
                        else:
                            st.error("Conversion failed. Check if the provided units are valid or supported.")
                    except ValueError:
                        st.error("Invalid numeric value provided in the query.")

def about_page():
    st.header("About This App")
    st.write(
        "This Smart Unit Converter app is built using Python and Streamlit. It leverages OpenAI's GPT-3.5-turbo "
        "to parse natural language conversion queries and uses the 'pint' library for accurate unit conversions. "
        "The app supports conversions for various units including length, temperature, weight, time, area, and many others.\n\n"
        "Use the navigation bar on the left to switch between the Unit Converter and this About page."
    )

def main():
    # Create a responsive navigation bar using the Streamlit sidebar.
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Unit Converter", "About"])
    
    if page == "Unit Converter":
        unit_converter_app()
    elif page == "About":
        about_page()

if __name__ == "__main__":
    main()
