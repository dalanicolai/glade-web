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

item("Glade 3.6.0 released", (2009, 3, 16),
     """<br>Glade has seen a world of improvement since 3.4, if you dont know about it, 
	  then I should at least skim over the new features and control we offer over your interface.
	  
	  <H3>Dual Project Formats</H3>
	  Now projects can be edited in libglade format and in GtkBuilder
	  format, offering you a load of new features only available in
	  GtkBuilder format (also removing access to deprecated widgets).
	  <br>
	    Projects can be converted, the operation is undoable, and can
	    result in data loss when some objects/widgets cant be ported to
	    the target format (classic libglade format projects can always
	    be converted to GtkBuilder format).

	    <H3>Target Project Version</H3>
	    Glade now lets you target your GTK+ version for your project,
	    giving you visual feedback and warnings about objects, properties
	    and signals that you may be using that are not available in
	    the targetted version of GTK+.
	  <br>
	    Interestingly Glade 3.6 depends on GTK+ 2.14, but gives you access to GTK+
	    properties from GTK+ 2.16 even if only running against 2.14.

	  <H3>Access to new objects</H3>
	  In GtkBuilder format, we have access to a whole new world of objects
	  we've never seen before in Glade:
	<ul>
     <LI> GtkAction: <br>
	   Represent your UI frontend widget(s) by an Action, actions
       are a great abstraction for UI components and let you have multiple
       screen widgets that correspond to a single "action" who all conform
       to the said actions state.

     <LI> GTK+ MVC Framework:<br>
       Now we give you access to GtkTreeView, GtkIconView, GtkComboBox (as a view),
       GtkListStore, GtkTreeStore in Glade.<br>That pretty much says it all, I encourage
       you all to try it, define columns and data for your treemodel, define columns
       and renderers for your treeview, in an all in one treeview editor.

     <LI> GtkIconFactory:<br>
       Add your own stock id definitions using an icon factory, define graphics
       for different widget sizes and widget states.

     <LI> GtkSizeGroup:<br>
       Add widgets to logical groups that ensure all members have the same size.
       </ul>
       <H3>Sexy New Editors</H3>
       With a new internal interface, we allow plugins to define editor layouts on a
       class level basis, now we have customized editors for GtkButton, GtkImage, GtkLabel,
       GtkEntry and many more (and they all have size to fit word wrapping property description texts in them).

       <H3>The Python Plugin</H3>
       This is finally worked out into a plugin, its been around for a while now but
       wasnt publicly/stably released to my knowlage, what it does is allow Glade to
       introspect and load your python classes properties and signals and add it to
       the palette automatically (with the use of a one or 2 liner user catalog),
       documentation coming, or ask Juan Pablo ;-)

       <H3>Some Enhancements</H3>
	<ul>
	  <LI> Inspector lets you filter and search the project with an added entry (behaves like DevHelp's search entry but on the project).
	  <LI> You can edit widgets inline with their editor in a dialog (Edit Separately in context menu), this editor window will stay on the same widget when selection changes).
	</ul>""", 'Juan Pablo Ugarte')

#item("PyGobject 2.18.0 released", (2009, 5, 25),
#     """PyGobject 2.18.0 has been released, this is a stable release, the first of the 2.18.x series. As usual, it's sources can be fetched
#     <a href="http://ftp.gnome.org/pub/GNOME/sources/pygobject/2.18/pygobject-2.18.0.tar.bz2">here</a>.
#     Check out <a href="http://mail.gnome.org/archives/gnome-announce-list/2009-May/msg00065.html">the release announcement and full list of changes</a>.""", 'Gian Mario Tagliaretti')
