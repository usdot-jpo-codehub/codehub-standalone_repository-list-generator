# README Outline:
* Project Description
* Prerequisites
* Usage
    * Business logic rules & info
    * To add/remove/edit a repository to/in the list
	* Building
	* Execution
	* Testing
* Additional Notes
* Version History and Retention
* License
* Contributions
* Contact Information
* Acknowledgements

# Project Description
This is a supporting repository for the [codehub-standalone](https://github.com/usdot-jpo-codehub/codehub-standalone) repository. It acts as a data transformation tool to manage the list of registered code repositories on ITS CodeHub. It reads a .csv file containing the details for all registered repositories, sorts the data by category, sorts the data within each category alphabetically, and generates a .json file, with repositories grouped by the categories.

# Prerequisites
Requires:
- NPM
  - [Install NPM](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
- Python 3 
  - ```npm install python3```
- Pandas
  - ```pip install pandas```
- A program to read and edit CSV file format:
  - Microsoft Excel - recommended for simplest editing
  - Visual Studio Code - recommended for users experienced with programming

# Usage
## Business logic rules & info:
   - It is expected that each repository will have one of each of: 
     - name
       - Example: ```codehub-standalone_repository-list-generator```
     - url
       - Example: ```https://github.com/usdot-jpo-codehub/codehub-standalone_repository-list-generator```
     - description (there currently is no limit, but it is recommended to stay under 1000 characters).
       - Example: ```This canary function is an early warning system that reports corrupt data. It listens to an SQS queue for notifications about new files in Amazon Web Services (AWS) Simple Storage Service (S3), and then validate that it meets certain field constraints.```
     - org (the GitHub organization, abbreviated using ```org```) 
       - Example: ```usdot-jpo-codehub```
     - category (only 1 category per repository is currently supported)
       - Example: ```Public Transportation```
   - The list of repositories is sorted alphabetically when the json is created.



## To add/remove/edit a repository to/in the list:
1. Open the CSV file ```input_repository_list.csv```
2. Do not modify the top row. The column names match the code in ```csv_to_json.py``` and the [code-repositories.html](https://github.com/usdot-jpo-codehub/codehub-standalone/blob/main/code/code-repositories.html) file in the [codehub-standalone](https://github.com/usdot-jpo-codehub/codehub-standalone) repository.
3. When adding a new repository, fill in each column. For the ```category``` column, you should choose ***one*** of the existing categories:
   
   * Commercial Vehicle Operations
   * Data Management
   * Maintenance and Construction 
   * Parking Management
   * Public Safety 
   * Public Transportation
   * Support
   * Sustainable Travel
   * Traffic Management
   * Traveler Information
   * Vehicle Safety
   * Weather
   * Other

These categories were chosen by ITS JPO. Additional categories may be added by putting the new category into the ```category``` column for the chosen repository. ***Each repository can only have one category.***

4. When done making changes to the CSV, save it over the existing ```input_repository_list.csv``` file.


## Building
No building required.
## Execution
1. In the folder containing both the ```input_repository_list.csv``` and ```csv_to_json.py``` files, run command
   ```python3 csv_to_json.py```
2. Verify the ```output_repository_list_codehub.json``` file is generated. Rename it to ```repository_list_codehub.json``` and replace the existing json file in the [codehub-standalone](https://github.com/usdot-jpo-codehub/codehub-standalone) repository at file location [/code/resources/data/repository_list_codehub.json](https://github.com/usdot-jpo-codehub/codehub-standalone/tree/main/code/resources/data/repository_list_codehub.json) with the updated file.
## Testing
Verify the same number of repositories found in the ```input_repository_list.csv``` file show up in the list of repositories on the [code-repositories.html](https://github.com/usdot-jpo-codehub/codehub-standalone/blob/main/code/code-repositories.html) page. The total number is calculated and displayed on the upper right portion of the page header.

# Additional Notes
```output_repository_list_codehub.json``` is included for reference. This fill will be overwritten when the ```python3 csv_to_json.py``` is run.
# Version History and Retention
**Status:** This project is in the release phase.

**Release Frequency:** This project is updated whenever ITS JPO has a new code repository to release.

**Retention:** **Retention:** This project will remain publicly accessible for a minimum of five years (until at least 07/28/2026).

# License
This project is licensed under the Apache 2.0 License, see [LICENSE](https://github.com/usdot-jpo-codehub/codehub-standalone_repository-list-generator/blob/master/LICENSE).

# Contributions
Please read [CONTRIBUTING.md](https://github.com/usdot-jpo-codehub/codehub-readme-template/blob/master/Contributing.MD) for details on our Code of Conduct, the process for submitting pull requests to us, and how contributions will be released.

# Contact Information
Contact Name: ITS JPO
Contact Information: data.itsjpo@dot.gov

# Acknowledgements
Thank you to the Department of Transportation for funding the development of this project.

## Citing this code
When you copy or adapt from this code, please include the original URL you copied the source code from and date of retrieval as a comment in your code.
