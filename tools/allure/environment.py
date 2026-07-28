from config import settings
import platform
import sys

def create_allure_environment_file():
    # Create a list of items in the {key}={value} format
    items = [f"{key}={value}" for key, value in settings.model_dump().items()]

    # Add environment information
    items.append(f"os_info={platform.system()}, {platform.release()}")
    items.append(f"python_version={sys.version}")


    # Join all items into a single string separated by newlines
    properties = "\n".join(items)

    # Open the ./allure-results/environment.properties file for writing
    with open(settings.allure_results_dir.joinpath("environment.properties"), "w+") as file:
        file.write(properties)  # Write the environment variables to the file