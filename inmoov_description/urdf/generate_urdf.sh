rosrun xacro xacro --inorder -o inmoov_description.urdf inmoov_description.urdf.xacro
sleep 2
check_urdf inmoov_description.urdf
sleep 2
urdf_to_graphiz inmoov_description.urdf 
sleep 2
evince inmoov.pdf
