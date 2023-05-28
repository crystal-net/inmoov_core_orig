ROS IDL
=================

ROS applications typically communicate through interfaces of one of three types: messages, services and actions. ROS 2 uses a simplified description language, the interface definition language (IDL), to describe these interfaces. This description makes it easy for ROS tools to automatically generate source code for the interface type in several target languages
More information is found here: https://docs.ros.org/en/rolling/Concepts/About-ROS-Interfaces.html


In this document we will describe the supported types.

   - msg: .msg files are simple text files that describe the fields of a ROS message.
   - srv: .srv files describe a service where a request is made and a response is required.
   - action: .action files describe actions which are long term goals to be reached and composed of three parts: a goal, a result, and feedback.




Messages (.msg)
-----------------


We will be using messages for telemetry and remote control.  We need to send data.  We don't care if it gets there (we hope it does) or how long, etc.

Therefore we will be creating the following messages types
   - Teleop
   - Sensor (image, imu, power)


 Table

+------+------------+-----------------------+-----------------+
| field | type & size | default value       | Description     |
+======+============+=======================+=================+
| twist |             | 0.2mm, 3walls       |                 |
+------+------------+-----------------------+-----------------+
|       |             | http://somesite.com |                 |
+------+------------+-----------------------+-----------------+
|       |             | http://somesite.com |                 |
+---- --+------------+----------------------+-----------------+
|       |             | http://somesite.com |                 |
+------+------------+-----------------------+-----------------+
|       |             | http://somesite.com |                 |
+------+------------+-----------------------+-----------------+






Services (.srv)

We will be using services for doing task where we need a result.
   - GPS (maybe?)















