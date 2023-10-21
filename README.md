---

# Redis Database Key Mover

A Python script to move a specified number of keys (half of the keys) between two Redis databases.

## Table of Contents

- [Description](#description)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [License](#license)
- [Author](#author)

## Description

This Python script connects to a Redis server and allows you to move half of the keys from one Redis database to another. It is useful when you want to redistribute data between databases efficiently.

## Prerequisites

Before you can use this script, make sure you have the following prerequisites:

- Python 3.x installed
- The `redis-py` library. You can install it using pip: `pip install redis`

## Usage

1. Clone the repository or download the script to your local machine.

2. Ensure that you have Python 3.x and the `redis-py` library installed.

3. Modify the script if necessary to configure the Redis server's host and port. By default, it connects to `localhost` on port `6379`.

4. Run the script:

    ```bash
    python move_keys.py
    ```

5. Follow the prompts to enter the source and destination database numbers (0-15).

6. The script will retrieve all keys from the source database, select half of them, and move them to the destination database.

7. Optionally, you can choose to delete the keys from the source database.

8. The script will close the Redis connection when finished.

## License

This project is licensed under the [Do What The Fuck You Want To Public License (WTFPL)](LICENSE).

You can do what the fuck you want with this code.

## Author

- GitHub: [https://github.com/Rolladex](https://github.com/Rolladex)

---
