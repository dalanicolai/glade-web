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

item("""Glade 3.7.1 released""", (2010, 3, 10),
     """
    <p>An exciting start to the 3.7 series is released.</p>
    <p>Some highlights in this release:</p>
    <ul>
    <li>Added notebook tabs to navigate through projects.</li>
    <li>Option to hide toolbar/statusbar.</li>
    <li>Now Glade uses GtkToolPalette for its palette.</li>
    <li>Signal Editor greatly improved</li>
    </ul>
    <p>See the <a href="http://mail.gnome.org/archives/gnome-announce-list/2010-May/msg00025.html">full announcement</a> for more details.</p>
     """, 'Tristan Van Berkom')

item("""Glade 3.7.0 released""", (2010, 3, 10),
     """See the <a href="http://mail.gnome.org/archives/gnome-announce-list/2010-March/msg00030.html">full announcement</a> for details.""", 'Tristan Van Berkom')

item("New website design", (2009, 7, 20),
     """Our website gets a facelift. Enjoy!.""", 'Javier Jardón')

item("""Glade 3.6.7 "Horizontally Oriented" released""", (2009, 6, 29),
     """See the <a href="http://mail.gnome.org/archives/gnome-announce-list/2009-June/msg00063.html">full announcement</a> for details.""", 'Tristan Van Berkom')

item("Glade 3.6.0 released", (2009, 3, 16),
     """
    <p>This is a major release and Glade has seen a world of improvement since 3.4. See the <a href="http://lists.ximian.com/pipermail/glade-users/2009-March/004244.html">full announcement</a> for details.</p>

    <p>Some feature highlights for this version are:</p>
    <ul>
    <li>Support for the old libglade and the new <strong>GtkBuilder format</strong>.</li>
    <li><strong>Target a specific GTK+ version</strong> and only the relevant objects, signals and properties will be avaliable.</li>
    <li><strong>New GTK+ objects avaliable</strong> thanks to GtkBuilder:
        <ul>
        <li>GtkAction</li>
        <li>Gtk+'s MVC elements like GtkTreeView, GtkIconView, GtkComboBox, GtkListStore or GtkTreeStore, allowing to define within Glade all the column, cellrenderer or model elements and connect them to have a working treeview, all that using a specialized editor.</li>
        <li>GtkIconFactory</li>
        <li>GtkSizeGroup</li>
        </ul>
    </li>
    <li><strong>Custom editors</strong> for GtkButton, GtkImage, GtkLabel, GtkEntry and many more.</li>
    <li><strong>Python plugin</strong></li>
    </ul>
    """, 'Juan Pablo Ugarte')

#item("PyGobject 2.18.0 released", (2009, 5, 25),
#     """PyGobject 2.18.0 has been released, this is a stable release, the first of the 2.18.x series. As usual, it's sources can be fetched
#     <a href="http://ftp.gnome.org/pub/GNOME/sources/pygobject/2.18/pygobject-2.18.0.tar.bz2">here</a>.
#     Check out <a href="http://mail.gnome.org/archives/gnome-announce-list/2009-May/msg00065.html">the release announcement and full list of changes</a>.""", 'Gian Mario Tagliaretti')
