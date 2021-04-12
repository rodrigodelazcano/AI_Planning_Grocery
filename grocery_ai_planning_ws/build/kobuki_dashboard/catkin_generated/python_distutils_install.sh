#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/rodri/AI_Planning_Grocery/grocery_ai_planning_ws/src/turtlebot_pkgs/kobuki_desktop/kobuki_dashboard"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/rodri/AI_Planning_Grocery/grocery_ai_planning_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/rodri/AI_Planning_Grocery/grocery_ai_planning_ws/install/lib/python2.7/dist-packages:/home/rodri/AI_Planning_Grocery/grocery_ai_planning_ws/build/kobuki_dashboard/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/rodri/AI_Planning_Grocery/grocery_ai_planning_ws/build/kobuki_dashboard" \
    "/usr/bin/python2" \
    "/home/rodri/AI_Planning_Grocery/grocery_ai_planning_ws/src/turtlebot_pkgs/kobuki_desktop/kobuki_dashboard/setup.py" \
     \
    build --build-base "/home/rodri/AI_Planning_Grocery/grocery_ai_planning_ws/build/kobuki_dashboard" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/rodri/AI_Planning_Grocery/grocery_ai_planning_ws/install" --install-scripts="/home/rodri/AI_Planning_Grocery/grocery_ai_planning_ws/install/bin"
