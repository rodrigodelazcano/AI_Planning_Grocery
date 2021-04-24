;; Auto-generated. Do not edit!


(when (boundp 'robot_path_controller::Path)
  (if (not (find-package "ROBOT_PATH_CONTROLLER"))
    (make-package "ROBOT_PATH_CONTROLLER"))
  (shadow 'Path (find-package "ROBOT_PATH_CONTROLLER")))
(unless (find-package "ROBOT_PATH_CONTROLLER::PATH")
  (make-package "ROBOT_PATH_CONTROLLER::PATH"))
(unless (find-package "ROBOT_PATH_CONTROLLER::PATHREQUEST")
  (make-package "ROBOT_PATH_CONTROLLER::PATHREQUEST"))
(unless (find-package "ROBOT_PATH_CONTROLLER::PATHRESPONSE")
  (make-package "ROBOT_PATH_CONTROLLER::PATHRESPONSE"))

(in-package "ROS")





(defclass robot_path_controller::PathRequest
  :super ros::object
  :slots (_waypoints ))

(defmethod robot_path_controller::PathRequest
  (:init
   (&key
    ((:waypoints __waypoints) (let (r) (dotimes (i 0) (push (instance robot_path_controller::WayPoint :init) r)) r))
    )
   (send-super :init)
   (setq _waypoints __waypoints)
   self)
  (:waypoints
   (&rest __waypoints)
   (if (keywordp (car __waypoints))
       (send* _waypoints __waypoints)
     (progn
       (if __waypoints (setq _waypoints (car __waypoints)))
       _waypoints)))
  (:serialization-length
   ()
   (+
    ;; robot_path_controller/WayPoint[] _waypoints
    (apply #'+ (send-all _waypoints :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; robot_path_controller/WayPoint[] _waypoints
     (write-long (length _waypoints) s)
     (dolist (elem _waypoints)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; robot_path_controller/WayPoint[] _waypoints
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _waypoints (let (r) (dotimes (i n) (push (instance robot_path_controller::WayPoint :init) r)) r))
     (dolist (elem- _waypoints)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(defclass robot_path_controller::PathResponse
  :super ros::object
  :slots (_complete ))

(defmethod robot_path_controller::PathResponse
  (:init
   (&key
    ((:complete __complete) nil)
    )
   (send-super :init)
   (setq _complete __complete)
   self)
  (:complete
   (&optional __complete)
   (if __complete (setq _complete __complete)) _complete)
  (:serialization-length
   ()
   (+
    ;; bool _complete
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _complete
       (if _complete (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _complete
     (setq _complete (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass robot_path_controller::Path
  :super ros::object
  :slots ())

(setf (get robot_path_controller::Path :md5sum-) "4a214603f798dc39b94ac5b447e437b3")
(setf (get robot_path_controller::Path :datatype-) "robot_path_controller/Path")
(setf (get robot_path_controller::Path :request) robot_path_controller::PathRequest)
(setf (get robot_path_controller::Path :response) robot_path_controller::PathResponse)

(defmethod robot_path_controller::PathRequest
  (:response () (instance robot_path_controller::PathResponse :init)))

(setf (get robot_path_controller::PathRequest :md5sum-) "4a214603f798dc39b94ac5b447e437b3")
(setf (get robot_path_controller::PathRequest :datatype-) "robot_path_controller/PathRequest")
(setf (get robot_path_controller::PathRequest :definition-)
      "WayPoint[] waypoints

================================================================================
MSG: robot_path_controller/WayPoint
---
bool complete
")

(setf (get robot_path_controller::PathResponse :md5sum-) "4a214603f798dc39b94ac5b447e437b3")
(setf (get robot_path_controller::PathResponse :datatype-) "robot_path_controller/PathResponse")
(setf (get robot_path_controller::PathResponse :definition-)
      "WayPoint[] waypoints

================================================================================
MSG: robot_path_controller/WayPoint
---
bool complete
")



(provide :robot_path_controller/Path "4a214603f798dc39b94ac5b447e437b3")


