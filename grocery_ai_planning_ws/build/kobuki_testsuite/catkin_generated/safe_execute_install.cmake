execute_process(COMMAND "/home/rodri/AI_Planning_Grocery/grocery_ai_planning_ws/build/kobuki_testsuite/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/rodri/AI_Planning_Grocery/grocery_ai_planning_ws/build/kobuki_testsuite/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
