Contents of README.txt:

This is a sample application using the framework described here:

    https://medium.com/@DerekFlynn/packaging-python-applications-239fafee18d4

If everything is set up correctly, you should just be able to type
"make" and get a app.pyz (a zip archive with the file extension .pyz
just to make it clear its a python zip).

Use unzip -l app.pyz to inspect it.

If you're following the guide, you should have a virtualenv set up
for each sample application bundle.  This lets you adjust the installed
packages on a bundle-by-bundle basis.

You will then have shell scripts that look like this:

--[ping.sh]--
#! /bin/sh

export PATH=/path/to/your/virtualenv/bin

exec python app.pyz ping "$@"
--

--[pong.sh]--
#! /bin/sh

export PATH=/path/to/your/virtualenv/bin

exec python app.pyz pong -l pong.log
--

Both of these invocations will run the __main__.pyc script in the
base directory as __main__ with the args above.  The __main__
then looks up what to run in the config.yml and runs that module
with the remaininig arguments from the command line.  This is
python magic -- python looks inside a zip archive for a __main__.pyc
to run.

So to run you just type:

$ sh ping.sh Hello world | sh pong.sh

