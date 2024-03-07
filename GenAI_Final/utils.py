import os
import yaml

def get_apikey():
    """
    Reads API key from a configuration file.
    
    This function opens a configuration file named "apikeys.yml", reads the API key for OpenAI
    
    Returns:
    api_key (str): The OpenAI API key, or None if not found.
    """
    
    # Dynamically construct the full path to the configuration file
    script_dir = os.path.dirname(os.path.realpath(__file__))  # Gets the directory where the script is located
    file_path = os.path.join(script_dir, "apikeys.yml")  # Constructs the path to the 'apikeys.yml' file
    
    with open(file_path, 'r') as yamlfile:
        loaded_yamlfile = yaml.safe_load(yamlfile)  # Load the YAML file
        
        if loaded_yamlfile is None:
            raise ValueError(f"The file {file_path} is empty or has an invalid format.")
        
        API_KEY = loaded_yamlfile.get('openai', {}).get('api_key', None)
        
        if API_KEY is None:
            raise ValueError("API key not found in the configuration file.")
        
    return API_KEY

if __name__ == "__main__":
    try:
        print("API_KEY:", get_apikey())
    except ValueError as e:
        print(e)
