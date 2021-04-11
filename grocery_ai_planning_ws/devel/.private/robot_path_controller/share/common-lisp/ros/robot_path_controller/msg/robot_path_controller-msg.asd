
(cl:in-package :asdf)

(defsystem "robot_path_controller-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "WayPoint" :depends-on ("_package_WayPoint"))
    (:file "_package_WayPoint" :depends-on ("_package"))
    (:file "WayPointList" :depends-on ("_package_WayPointList"))
    (:file "_package_WayPointList" :depends-on ("_package"))
  ))