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
     """Our website gets a facelift. Enjoy!.""", 'Javier Jardón')

item("""Glade 3.6.7 "Horizontally Oriented" released""", (2009, 6, 29),
     """See the <a href="http://mail.gnome.org/archives/gnome-announce-list/2009-June/msg00063.html">full announcement</a> for details.""", 'Tristan van Berkom')

item("Glade 3.6.0 released", (2009, 3, 16),
     """
    <p>Glade has seen a world of improvement since 3.4, if you dont know about it,
    then I should at least skim over the new features and control we offer over your interface.</p>

    <h1>Dual Project Formats</h1>
    <p>Now projects can be edited in libglade format and in GtkBuilder
    format, offering you a load of new features only available in
    GtkBuilder format (also removing access to deprecated widgets).</p>

    <p>Projects can be converted, the operation is undoable, and can
    result in data loss when some objects/widgets cant be ported to
    the target format (classic libglade format projects can always
    be converted to GtkBuilder format).

    <h1>Target Project Version</h1>
    <p>Glade now lets you target your GTK+ version for your project,
    giving you visual feedback and warnings about objects, properties
    and signals that you may be using that are not available in
    the targetted version of GTK+.</p>

    <p>Interestingly Glade 3.6 depends on GTK+ 2.14, but gives you access to GTK+
    properties from GTK+ 2.16 even if only running against 2.14.</p>

    <h1>Access to new objects</h1>
    <p>In GtkBuilder format, we have access to a whole new world of objects
    we've never seen before in Glade:</p>
    <ul>
    <li><h2>GtkAction:</h2>
    <p>Represent your UI frontend widget(s) by an Action, actions
    are a great abstraction for UI components and let you have multiple
    screen widgets that correspond to a single "action" who all conform
    to the said actions state.</p>

    <li><h2>GTK+ MVC Framework:</h2>
    <p>Now we give you access to GtkTreeView, GtkIconView, GtkComboBox (as a view),
    GtkListStore, GtkTreeStore in Glade.</p>
    <p>That pretty much says it all, I encourage
    you all to try it, define columns and data for your treemodel, define columns
    and renderers for your treeview, in an all in one treeview editor.</p>
    </li>
    <li><h2>GtkIconFactory:</h2>
    <p>Add your own stock id definitions using an icon factory, define graphics
    for different widget sizes and widget states.</p>
    </li>
    <li><h2>GtkSizeGroup:</h2>
    <p>Add widgets to logical groups that ensure all members have the same size.</p>
    </li>
    </ul>
    <h1>Sexy New Editors</h1>
    <p>With a new internal interface, we allow plugins to define editor layouts on a
    class level basis, now we have customized editors for GtkButton, GtkImage, GtkLabel,
    GtkEntry and many more (and they all have size to fit word wrapping property description texts in them).</p>

    <h1>The Python Plugin</h1>
    <p>This is finally worked out into a plugin, its been around for a while now but
    wasnt publicly/stably released to my knowlage, what it does is allow Glade to
    introspect and load your python classes properties and signals and add it to
    the palette automatically (with the use of a one or 2 liner user catalog),
    documentation coming, or ask Juan Pablo ;-)</p>

    <h1>Some Enhancements</h1>
    <ul>
    <li><p>Inspector lets you filter and search the project with an added entry (behaves like DevHelp's search entry but on the project).</p></li>
    <li><p>You can edit widgets inline with their editor in a dialog (Edit Separately in context menu), this editor window will stay on the same widget when selection changes).</p></li>
    </ul>
    """, 'Juan Pablo Ugarte')

#item("PyGobject 2.18.0 released", (2009, 5, 25),
#     """PyGobject 2.18.0 has been released, this is a stable release, the first of the 2.18.x series. As usual, it's sources can be fetched
#     <a href="http://ftp.gnome.org/pub/GNOME/sources/pygobject/2.18/pygobject-2.18.0.tar.bz2">here</a>.
#     Check out <a href="http://mail.gnome.org/archives/gnome-announce-list/2009-May/msg00065.html">the release announcement and full list of changes</a>.""", 'Gian Mario Tagliaretti')
