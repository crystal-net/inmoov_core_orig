URDF / Xacro file structure

robots/  |        <!-- This directory defines the top level definition files.  We can have multiple definitions without changing other components-->
         --> inmoov.urdf.xacro
urdf/               <!-- This directory contains the individual component, linkages, config files to be included in the top level file-->


```inmoov.urdf.xacro
    graph TD;
        inmoov.urdf --> config.urdf
        
```