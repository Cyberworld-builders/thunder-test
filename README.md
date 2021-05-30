# Here's what all i did

## Some libraries only run on the actual pi.
Obviously one of these is the RPi.GPIO because it connects with the pins on the pi.
You can debug some of this locally but for things like RPi.GPIO, you just have to run it on the pi.

## AudioPlayer gave me errors on the pi that i didn't get on my Ubuntu machine.
This command fixed it.
`sudo apt install python3-gst-1.0`
