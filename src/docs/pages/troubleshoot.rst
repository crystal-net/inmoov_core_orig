Troubleshooting
==============
This is a list of all the modules currently under development for InMoov.

vscode
--------------

red squiggles
make sure package src.cpp file has cpp extension





inmoov_description
------------------
    URDF/Xacro 3D model description.





inmoov_gazebo
-------------
    components for Gazebo.  Currently unimplemented as I think we should use Ignition but still in early development.





inmoov_rviz
-----------
    Visualization using rViz2





inmoov_pubsub
-------------
    Publisher and subscriber nodes for topics.  Generic for now





inmoov_service
--------------
    This is where the msg services are stored



Multiple ST-Link boards
--------------
Multiple STLink, one for each Project in STM32CubeIDE
Trying to have multiple ST-Link connected at one time.

Not working like I hoped.

Anyone got it working? (Multiple projects each with own STLink, all connected at same time)

 

Using STM32CubeIDE v1.6.1

 

My results
 +++++++++

I try to set each project to a specific STLink Serial Number (I have 5 modules interconnected, and that list is growing), using:

Project > Right Click > Debug As > Debug Cofigurations... > Tab:Debugger
[+]ST-Link S/N > Scan > Select the correct one > Apply > Close
It works with one, but gets confused when I have more than one
I've written the serial number on each device by connecting one at a time and scanning for changes.

I've noticed that the first serial number listed seems to be incorrect, as it is often for an STLink I've disconnected. ****This may be a bug****
 

Suggestion
 +++++++++

ST-Link serial numbers should be:

Shown on the Virtual disk that opens when you connect the USB to the STLink (maybe in Details.txt)
Printed on the label (STLink/V3, STLink/Mini, etc.)
 


 Change MCUs
-----------

 Tutorial 5: Exporting current project configuration to a compatible MCU.
When List pinout compatible MCUs is selected from the Pinout menu, STM32CubeMX retrieves the list of the MCUs which are compatible with the current project configuration, and offers to export the current configuration to the newly selected compatible MCU.
This tutorial shows how to display the list of compatible MCUs and export your current project configuration to a compatible MCU:

1. Load an existing project, or create and save a new project.

2. Go to the Pinout menu and select List Pinout Compatible MCUs. The Pinout compatible window pops up. If needed, modify the search criteria and the filter options and restart the search process by clicking the Search button. The color shading and the Comments column indicate the level of matching:
– Exact match: the MCU is fully compatible with the current project.
– Partial match with hardware compatibility: the hardware compatibility can be ensured but some pin names could not be preserved. Hover the mouse over the desired MCU to display an explanatory tooltip.
– Partial match without hardware compatibility: not all signals can be assigned to the exact same pin location and a remapping will be required. Hover the mouse over the desired MCU to display an explanatory tooltip.

3. Then, select an MCU to import the current configuration to, and click OK, Import. The configuration is now available for the selected MCU.

4. To see the list of compatible MCUs at any time, select Outputs under the Window menu. To load the current configuration to another compatible MCU, double-click the list of compatible MCUs.

5. To remove some constraints on the search criteria, several solutions are possible:
– Select the Ignore Pinning Status checkbox to ignore pin status (locked pins).
– Select the Ignore Power Pins checkbox not to take into account the power pins.
– Select the Ignore System Pins not take into account the system pins. Hover the mouse over the checkbox to display a tooltip that lists the system pins available on the current MCU.

