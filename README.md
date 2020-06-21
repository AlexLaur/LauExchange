# LauExchange

LauExchange is a simple exchange app based on websockets with PySide2 for a full integration in Maya or Nuke.
You can exchange your current selection with others people in your studio.
You can also extend this tool in other software by creating a new attachment module for your soft and by editing the launcher with the new software.

## Server Installation

1. From the `server` directory, install the `virtualenv` package:

   ```bash
   $ pip install virtualenv
   Collecting virtualenv
   Installing collected packages: virtualenv
   Successfully installed virtualenv-16.6.0
   ```

2. Create a virtual environment named `lauexchange`:

   ```bash
   $ virtualenv lauexchange
   Running virtualenv with interpreter /usr/bin/python2.7
   Installing setuptools, pip, wheel...
   done.
   ```

3. Activate the virtual environment:

   ```bash
   $ source lauexchange/bin/activate
   (lauexhange)
   $
   ```

   After activation, you should see `(lauexchange)` above your command prompt.

4. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.txt.

    ```bash
    $ pip install -r requirements.txt
    ```
5. Open shell and create the database.db:

   ```bash
    $ cd server/db
    $ sqlite3 database.db
    ```
6. Copy the content of commands.txt in the previous shell with sqlite3.

7. Run the server.py. Set the host and the port (by default: 127.0.0.1:1302)

    ```bash
    $ python server.py --host 127.0.0.1 --port 1302
    ```

## Usage for Maya

```python
from client import launcher
launcher.run_maya()
```

## Usage for Nuke

```python
from client import launcher
launcher.run_nuke()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
