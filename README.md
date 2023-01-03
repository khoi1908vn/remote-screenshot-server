# remote-screenshot-server


## About The Project



This is the server used in a remote-screenshot project. With a console and a simple HTTP server, this can help you to remotely request for screenshots from a agent. 





### Built With

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)






<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may provide instructions for launching your project locally. Follow these simple example steps to set up a local copy.

### Installation
*Replit recommended*

1. Clone the repo
   ```sh
   git clone https://github.com/khoi1908vn/remote-screenshot-server.git
   ```
2. Install python libs:
   ```sh
   pip install -r requirements.txt
   ```
3. Go to `./databases/config.json` and fill your keys (any random strings you want)
3. Start ``main.py``
   ```sh
   python main.py
   ```
4. Open the server's console and fill your webhook:
   ```sh
   > update webhook <your discord webhook with https://>
   ```





<!-- USAGE EXAMPLES -->
## Usage

There are 2 main feature, `update` and `get`.

- `update` : Update the current `webhook` and `status` that the agent will get via `/get/`

- `get` : Get the current `webhook` and `status` that the agent will get via `/get/`


## Contributing

You can't contribute to this project.

## License

Private project, no license.