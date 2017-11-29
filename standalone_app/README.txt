Contents of README.txt:

This is a sample application using the framework described here:

    http:////

If everything is set up correctly, you should just be able to type
"make" and get a app.pyz (a zip archive with the file
extension .pyz just to make it clear its a python zip).

Use unzip -l app.pyz to inspect it.

If you're following the guide, you should have a virtualenv set up
for each sample application bundle.  This lets you adjust the installed
packages on a bundle-by-bundle basis.

You will then have a shell script that look like this:

--[hello.sh]--
#! /bin/sh

export PATH=/path/to/your/virtualenv/bin

exec python app.pyz
--

So to run you just type:

$ sh hello.sh
>> Hello world <<

