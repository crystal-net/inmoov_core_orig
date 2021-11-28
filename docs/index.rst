.. inmoov_ros2 documentation master file, created by
   sphinx-quickstart on Fri Nov 26 20:01:56 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.




=================
InMoov on Robot Operating System 2!
=================
-------------------------
Embodiment Of Our Robot Overlords
-------------------------





Subheading
----------

The basic syntax is not that different from Markdown, but it also
has many more powerful features that Markdown doesn't have. We aren't
taking advantage of those yet though.

- Bullet points
- Are intuitive
- And simple too



.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
* InMoov Telemetry: http://www.crystal-net.org


"""""""""""""""""
Document Title
"""""""""""""""""
...........
Subtitle
...........

.. contents:: Overview
   :depth: 3

===================
Section 1
===================

Text can be *italicized* or **bolded**  as well as ``monospaced``.
You can \*escape certain\* special characters.

----------------------
Subsection 1 (Level 2)
----------------------

Some section 2 text

Sub-subsection 1 (level 3)
--------------------------

Some more text.

=========
Examples
=========

--------
Comments
--------

.. This is a comment
   Special notes that are not shown but might come out as HTML comments

------
Images
------

Add an image with:

.. image:: screenshots/file.png
   :height: 100
   :width: 200
   :alt: alternate text

You can inline an image or other directive with the |customsub| command.

.. |customsub| image:: image/image.png
              :alt: (missing image text)

-----
Lists
-----

- Bullet are made like this
- Point levels must be consistent
    * Sub-bullets
        + Sub-sub-bullets
- Lists

Term
    Definition for term
Term2
    Definition for term 2

:List of Things:
    item1 - these are 'field lists' not bulleted lists
    item2
    item 3

:Something: single item
:Someitem: single item

-----------------
Preformatted text
-----------------

A code example prefix must always end with double colon like it's presenting something::

    Anything indented is part of the preformatted block
   Until
  It gets back to
 Allll the way left

Now we're out of the preformatted block.

------------
Code blocks
------------

There are three equivalents: ``code``, ``sourcecode``, and ``code-block``.

.. code:: python

   import os
   print(help(os))

.. code:: C

   if (x=1, 1, 1) 

.. sourcecode::

  # Equivalent

.. code-block::

  # Equivalent

-----
Links
-----

Web addresses by themselves will auto link, like this: https://www.devdungeon.com

You can also inline custom links: `Google search engine <https://www.google.com>`_

This is a simple link_ to Google with the link defined separately.

.. _link: https://www.google.com

This is a link to the `Python website`_.

.. _Python website: http://www.python.org/

This is a link back to `Section 1`_. You can link based off of the heading name
within a document.

---------
Footnotes
---------

Footnote Reference [1]_

.. [1] This is footnote number one that would go at the bottom of the document.

Or autonumbered [#]

.. [#] This automatically becomes second, based on the 1 already existing.

-----------------
Lines/Transitions
-----------------

Any 4+ repeated characters with blank lines surrounding it becomes an hr line, like this.

====================================

------
Bill of Materials
------

+-------+-----+----------------------------+
| Screw | Qty | Link to suggested supplier |
+=======+=====+============================+
| M2    | 42  | 2                          |
+-------+-----+----------------------------+
| M3    | 23  | http://somesite.com        |
+-------+-----+----------------------------+
| M4    | 23  | http://somesite.com        |
+-------+-----+----------------------------+
| M5    | 23  | http://somesite.com        |
+-------+-----+----------------------------+
| M6    | 23  | http://somesite.com        |
+-------+-----+----------------------------+







Preserving line breaks
----------------------

Normally you can break the line in the middle of a paragraph and it will
ignore the newline. If you want to preserve the newlines, use the ``|`` prefix
on the lines. For example:

| These lines will
| break exactly
| where we told them to.



Finally About The Project
============

I started this project thinking that I wanted to learn 3D printing and I also dreamed of having my own robot.
I searched around on the internet for inspiration and came across Gael Langevins creationg at http://inmoov.fr .

I immediately fell in love with the idea and started building starting with 3D printing the models and discovering
that it is not a perfect out of the box result.  There was alot of frustration and wasted plastic trying to get the prints
I wanted.  I had the impression that people were getting these beautiful prints and that just wasn't the case.  Youtube camera 
magic hides alot of flaws.

Then I started with the electronics.  I am good with a solder iron.  and know the basic circuits and math that goes with it.  Not an issue.
While I knew the basics, I didn't know anything about microcontrollers or embedded C programming.
I understand coding at the fundamental levels but never mastered any single language.  So I got me an Arduino and started tinkering.
Luckily the InMoov project also used Arduinos for its servo control so I figured I was off to the races.  I had a blinky light and some servos attached.

The robot control software being used with InMoov was from myrobotlab.org.  It is an amazing project.  Very modular and capable but I just felt like it wasn't quite right for me.
I had alot of troubles getting it to work and it seamed overly complex.  But I used it as it was what I knew.

Around the same time I also happened to be introduced to the STM32 ecosystem and again I was amazed and bewildered.  This new microcontroller was so much more
powerfull than the arduinos and not much more expensive.  I decided the long game was to switch to one of these boards.

Back to the software.  I soon discovered ROS.  Not sure from where exactly.  I think i just kept reading mention of it on and off.  It seamed like a big complicated system using C which I didn't know well.
I didn't want to learn yet another thing so I stayed away from it but something told me that it was the right thing for me.  Then I started learning of other robots and projects that used ROS and did a little reading.  Again I was sold.

I felt I needed a web site.  I don't want to host my own.  I didn't want to just post a bunch of crap on Facebook.  Its not for me.  I wanted something professional and functional.  No ads.  No invasion of privacy.  Likes/dislikes. No pushing for subscribers.  Just good clean information.

So this leads me here on ReadTheDocs.  It is all of that.  I don't have to host a website of me own.  I don't need to do a bunch of web programming and UX design etc.
I simply write my documentation in VsCode and submit a git push and voila.  
I will be hosting a web site http://inmoov.crystal-net.org for some non-documentation related information such as robot telemetry, odometry and control or anything that doens't belong in a documentation site.

This docs site is the colmnination of much love and frustration.


I want to build something amazing and I hope you will all join me.

