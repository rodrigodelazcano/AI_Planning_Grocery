
(cl:in-package :asdf)

(defsystem "robot_path_controller-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :robot_path_controller-msg
)
  :components ((:file "_package")
    (:file "Path" :depends-on ("_package_Path"))
    (:file "_package_Path" :depends-on ("_package"))
  ))