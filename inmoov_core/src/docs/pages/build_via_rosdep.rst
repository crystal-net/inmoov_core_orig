How to build the InMoov environment via rosdep 
=================

A ROS package must specify its dependencies in the package.xml file. Simply because that is the information being used to e.g. release a package with bloom into a Debian package.

With that information available you can then use rosdep to install the dependencies according to the platform you are on. On Ubuntu it should be Debian packages (otherwise you wouldn't be able to create a Debian package of your package). On other platforms rosdep will use pip.

colconexplicitly does not target to install any dependencies for you (see https://colcon.readthedocs.io/en/rele...). It leaves this part to other tools (like rosdep).

link
add a comment
1
answered Sep 30 '19

tfoote gravatar image
tfoote
56996 ●120 ●511 ●504 http://www.ros.org/
It's strongly recommended to use system dependencies declared in the package.xml file and then standard tools like rosdep can both check and resolve them.

colcon is a build tool. We have specifically separated build and install stages for cleaner separation of concerns as well as to avoid side effects that might have security implications.

A standard practice is to:

Download a set of packages into a workspace (using a rosinstall file or repos file and vcstool)
Install all dependencies of that workspace (Using rosdep. It will error if anything is unresolved that you might need to maually resolve.)
Run your build(with colcon)










Code block description

.. code-block:: console

   Line one of code code-block
   Line two


two empty lines ends the code block




Level 3
_________





 Table

+------+------------+---------------------+
| Part | Print Time | Printer Settings    |
+======+============+=====================+
| M2   | 42         | 0.2mm, 3walls       |
+------+------------+---------------------+
| M3   | 23         | http://somesite.com |
+------+------------+---------------------+
| M4   | 23         | http://somesite.com |
+------+------------+---------------------+
| M5   | 23         | http://somesite.com |
+------+------------+---------------------+
| M6   | 23         | http://somesite.com |
+------+------------+---------------------+



