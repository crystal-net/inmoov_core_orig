cmake_minimum_required(VERSION 3.8)
project(inmoov_publisher)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)

# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)


# The following block of BUILD_TESTING is only for testing and will compile fine without it.
# We will leave it as it doesn't cause any problems and is good to have.  We want to use this in the future.
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

# this is not the name of the node or the name of the package.  
# it is just of the executable and it can be different
add_executable(inmoov_publisher src/inmoov_publisher.cpp)

# next we link the dependencies (rclcpp) as noted in find_package(rclcpp REQUIRED)
ament_target_dependencies(inmoov_publisher rclcpp)


# Next we install the executable inside the workspace
install(TARGETS
  inmoov_publisher
  DESTINATION lib/${PROJECT_NAME}
)
ament_package()
