# Docker compose playground

Basically a little project to play with docker compose

## Features:

### Running unit tests via docker compose

So far chosen way is to run a `.sh` script which will run some docker commands.
Those commands will run a `compose` test file with some test parameters and iso to the normal `compose` file to actually run the app.
This way it set up all images needed from scratch, run whatever command it must run inside the previously started images and shut down the all thing.

For more detaisl see `test.sh` file and `compose-test.yaml`
