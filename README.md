
1. Core Functionalities
/start Command**: Welcomes users, introduces the bot, and mentions available commands.
/cmds Command**: Lists all available commands in the bot, providing a clear overview of what users can do.
/reset Command**: Restart the bot during runtime.

2. Generating and Cleaning BINs/Credit Cards
/gbin Command**: Generates random BINs. It ensures BINs are well-formatted and limits requests to avoid excessive API usage.
/gen Command**: Generates valid credit card numbers using a given BIN, including expiry date and CVV, while validating them with the Luhn algorithm.
/clean Command**: Processes text files containing credit card data and reformats them into the standard cc|mm|yy|cvv format.
BIN Lookup**: Fetches detailed information about BIN numbers, like country, scheme, and bank.

3. File Utilities
/merge Command**: Allows multiple .txt files to be uploaded for merging.
/split Command**: Splits an uploaded .txt file into equal parts based on user input.
/aflt Command**: Filters email:password format pairs from uploaded .txt files.

4. Proxies and IP Tools
/px Command**: Validates proxy availability and retrieves its IP information.
/ip Command**: Fetches details about an IP address, including location, organization, and security flags like VPN/Proxy/TOR indicators.

5. Crunchyroll Checker
/crunchy and /mcrunchy Commands**: Checks Crunchyroll account credentials (email:password) for validity and subscription status. Results are stored temporarily and retrievable via a unique secret code (/gethits).
Provides detailed stats about total, good, premium, and bad accounts using inline keyboards to display progress.

6. Advanced Media Tools
/ai Command**: Sends queries to an AI image generation API and returns the generated image.
/img Command**: Searches and retrieves up to 5 images using Google’s Custom Search API.
/data Command**: Fetches detailed information about a person (using Wikipedia or Google Search) alongside an image.
/search Command**: Performs Google search for user queries or fetches Wikipedia summaries for provided terms.

7. User Interaction and Custom Features
Inline keyboard buttons dynamically show stats or custom actions for users during operations.
Stop functionality using /stop: Stops ongoing processes and clears temporary data for the user.
Validation and error-handling mechanisms ensure proper user input and provide meaningful responses in case of missteps.
