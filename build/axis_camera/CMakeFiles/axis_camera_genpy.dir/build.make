# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/pouya/catkin_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/pouya/catkin_ws/build

# Utility rule file for axis_camera_genpy.

# Include the progress variables for this target.
include axis_camera/CMakeFiles/axis_camera_genpy.dir/progress.make

axis_camera_genpy: axis_camera/CMakeFiles/axis_camera_genpy.dir/build.make

.PHONY : axis_camera_genpy

# Rule to build all files generated by this target.
axis_camera/CMakeFiles/axis_camera_genpy.dir/build: axis_camera_genpy

.PHONY : axis_camera/CMakeFiles/axis_camera_genpy.dir/build

axis_camera/CMakeFiles/axis_camera_genpy.dir/clean:
	cd /home/pouya/catkin_ws/build/axis_camera && $(CMAKE_COMMAND) -P CMakeFiles/axis_camera_genpy.dir/cmake_clean.cmake
.PHONY : axis_camera/CMakeFiles/axis_camera_genpy.dir/clean

axis_camera/CMakeFiles/axis_camera_genpy.dir/depend:
	cd /home/pouya/catkin_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/pouya/catkin_ws/src /home/pouya/catkin_ws/src/axis_camera /home/pouya/catkin_ws/build /home/pouya/catkin_ws/build/axis_camera /home/pouya/catkin_ws/build/axis_camera/CMakeFiles/axis_camera_genpy.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : axis_camera/CMakeFiles/axis_camera_genpy.dir/depend

