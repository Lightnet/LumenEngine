#!python
import os

#--------
# Config files
#--------
IMGUI_PATH = 'imgui'
#--------
# folder dir and output folder or file
#--------

projectname = 'LumenEngine'				#holds the project name
projectpackage = 'main'						#holds the project folder
SRC_PATH = 'src'
builddir = '.' + os.sep + SRC_PATH + os.sep + projectpackage  			#holds the build directory for this project

#-------
#---- SFML ----
#SFML_LIBS = 'SFML-2.4.2\\lib'
#SFML_LIBS = 'C:\\sfml-build\\lib\\Release'
#SFML_BIN = 'SFML-2.4.2\\bin\\'

#--include files
include_packages = []
#include_packages.append('api\\glfw\\include')

include_packages.append('api\\imgui')
include_packages.append('api\\stb')
include_packages.append('api\\glad\\include')
include_packages.append('api\\glfw\\include')

include_packages.append('src\\renderer')

include_packages.append('api\\glm')

include_packages.append('src\\cuda')
include_packages.append('src\\resources')
include_packages.append('src\\camera')

#include_packages.append('SFML-2.4.2\\include')
#include_packages.append(SRC_PATH + os.sep + 'imgui')

#--engine node packages
core_packages = []

#--lib
lib_packages = []
lib_packages.append('imgui')
lib_packages.append('stb')
#lib_packages.append('glad')
#lib_packages.append('glfw')
#lib_packages.append('opengl32')

dll_packages = []
#--release
#dll_packages.append('sfml-audio-2')
#dll_packages.append('sfml-graphics-2')
#dll_packages.append('sfml-network-2')
#dll_packages.append('sfml-system-2')
#dll_packages.append('sfml-window-2')

#--add list
lib_packages += core_packages
include_packages +=core_packages

lib_files = []
#lib_files.append("SFML-2.4.2\\lib\\sfml-graphics-s.lib")
#lib_files.append(SFML_LIBS + "\\sfml-graphics.lib")
#lib_files.append(SFML_LIBS + "\\sfml-audio.lib")
#lib_files.append(SFML_LIBS + "\\sfml-network.lib")
#lib_files.append(SFML_LIBS + "\\sfml-system.lib")
#lib_files.append(SFML_LIBS + "\\sfml-window.lib")
