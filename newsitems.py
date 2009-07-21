# -*- encoding: utf-8
# Setup code, stay away
items = []
item = lambda *x: items.append(x)

# News items go here, most recent ones at top. Dates can be either
# strings or time(3) output.
#
# item("INSERT TITLE HERE",
#      (1901, 3, 1),
#      """
#      INSERT TEXT HERE
#      """,
#      "INSERT AUTHOR HERE")

# http://news.gmane.org/gmane.comp.gnome.gtk%2B.python/
item("New website design", (2009, 7, 20),
     """Our website gets a facelift. Enjoy!.""", 'Tristan van Berkom')

item("Glade 3.6.7 released", (2009, 6, 29),
     """This is a bugfix release. See full announcement for details.""", 'Tristan van Berkom')
#item("PyGobject 2.18.0 released", (2009, 5, 25),
#     """PyGobject 2.18.0 has been released, this is a stable release, the first of the 2.18.x series. As usual, it's sources can be fetched
#     <a href="http://ftp.gnome.org/pub/GNOME/sources/pygobject/2.18/pygobject-2.18.0.tar.bz2">here</a>.
#     Check out <a href="http://mail.gnome.org/archives/gnome-announce-list/2009-May/msg00065.html">the release announcement and full list of changes</a>.""", 'Gian Mario Tagliaretti')
