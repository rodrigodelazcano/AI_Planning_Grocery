;; Auto-generated. Do not edit!


(when (boundp 'robot_path_controller::WayPointList)
  (if (not (find-package "ROBOT_PATH_CONTROLLER"))
    (make-package "ROBOT_PATH_CONTROLLER"))
  (shadow 'WayPointList (find-package "ROBOT_PATH_CONTROLLER")))
(unless (find-package "ROBOT_PATH_CONTROLLER::WAYPOINTLIST")
  (make-package "ROBOT_PATH_CONTROLLER::WAYPOINTLIST"))

(in-package "ROS")
;;//! \htmlinclude WayPointList.msg.html


(defclass robot_path_controller::WayPointList
  :super ros::object
  :slots (_path ))

(defmethod robot_path_controller::WayPointList
  (:init
   (&key
    ((:path __path) (let (r) (dotimes (i 0) (push (instance robot_path_controller::WayPoint :init) r)) r))
    )
   (send-super :init)
   (setq _path __path)
   self)
  (:path
   (&rest __path)
   (if (keywordp (car __path))
       (send* _path __path)
     (progn
       (if __path (setq _path (car __path)))
       _path)))
  (:serialization-length
   ()
   (+
    ;; robot_path_controller/WayPoint[] _path
    (apply #'+ (send-all _path :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; robot_path_controller/WayPoint[] _path
     (write-long (length _path) s)
     (dolist (elem _path)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; robot_path_controller/WayPoint[] _path
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _path (let (r) (dotimes (i n) (push (instance robot_path_controller::WayPoint :init) r)) r))
     (dolist (elem- _path)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get robot_path_controller::WayPointList :md5sum-) "6bc47b0184d2e472693eb2c6129282d1")
(setf (get robot_path_controller::WayPointList :datatype-) "robot_path_controller/WayPointList")
(setf (get robot_path_controller::WayPointList :definition-)
      "WayPoint[] path
================================================================================
MSG: robot_path_controller/WayPoint
float64[2] coord
")



(provide :robot_path_controller/WayPointList "6bc47b0184d2e472693eb2c6129282d1")


