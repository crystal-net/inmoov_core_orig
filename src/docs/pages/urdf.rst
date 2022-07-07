URDF Cheatsheet
==================





    Notes
      Joint Types
      There are three kinds of joints that move around in space. 
      Prismatic joint can only move along one dimension (in and out?)
      Planar joint can move around in a plane, or two dimensions. 
      Floating joints are unconstrained, and can move around in any of the three dimensions. These joints cannot be specified by just one number, and therefore aren’t included in this tutorial.

    
    rosparam load my_robot.urdf robot_description
      
    
    I want to just view a new URDF in rviz without my inmoov stuff
    
    roslaunch urdf_tutorial display.launch model:=urdf/easyjoint.urdf.xacro




Working with Joint State
------------------------
This allows us to send fake joint states using a slider GUI.

.. code:: xml

    <!-- send fake joint values -->
    <node name="joint_state_publisher" pkg="joint_state_publisher" type="joint_state_publisher">
        <param name="use_gui" value="true" />
    </node>





URDF Geometry Definition
------------------------

    Links
    
      origin rpy="0 1.57075 0" xyz="0 0 -0.3" 
      All mesurements are in relation to the parent
      rpy (roll / pitch / yaw) rotates the link (part) measured in radians?
      xyz sets the location at

      Regarding the joint definition, origin xyz="0 -0.22 0.25"
      It is defined in terms of the parents reference frame. So we are -0.22 meters in the y direction (to our left, but to the right relative to the axes) and 0.25 meters in the z direction (up).
      
      
      With respect to the **LINK** while looking at the front of the model.
      Changing these values is independant of the joint (the RGB crosshairs).
      Technically the link(part) can be outside the joint but will still move in reference to it.
      Parameters are measured in meters and radians?
      (x)(RED) a positive value moves the part forward (closer) from the horizon, negative moves the part back
      (y)(GREEN) a positive value moves right, a negative value moves the part left
      (z)(BLUE) a positive vlue moves up, a negative value moves the part down
      
      (r) horizon, negative moves the part back
      (p) moves the part left
      (y) part down
      
      With respect to the **JOINT** while looking at the front of the model
      (x)(RED) a positive value moves the part forward (closer) from the horizon, negative moves the part back
      (y)(GREEN) a positive value moves right, a negative value moves the part left
      (z)(BLUE) a positive vlue moves up, a negative value moves the part down
      