INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_FM_SWITCH FM_Switch)

FIND_PATH(
    FM_SWITCH_INCLUDE_DIRS
    NAMES FM_Switch/api.h
    HINTS $ENV{FM_SWITCH_DIR}/include
        ${PC_FM_SWITCH_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    FM_SWITCH_LIBRARIES
    NAMES gnuradio-FM_Switch
    HINTS $ENV{FM_SWITCH_DIR}/lib
        ${PC_FM_SWITCH_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(FM_SWITCH DEFAULT_MSG FM_SWITCH_LIBRARIES FM_SWITCH_INCLUDE_DIRS)
MARK_AS_ADVANCED(FM_SWITCH_LIBRARIES FM_SWITCH_INCLUDE_DIRS)

