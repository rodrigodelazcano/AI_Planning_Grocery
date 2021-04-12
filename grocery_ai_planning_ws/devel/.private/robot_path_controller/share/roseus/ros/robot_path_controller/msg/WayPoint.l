;; Auto-generated. Do not edit!


(when (boundp 'robot_path_controller::WayPoint)
  (if (not (find-package "ROBOT_PATH_CONTROLLER"))
    (make-package "ROBOT_PATH_CONTROLLER"))
  (shadow 'WayPoint (find-package "ROBOT_PATH_CONTROLLER")))
(unless (find-package "ROBOT_PATH_CONTROLLER::WAYPOINT")
  (make-package "ROBOT_PATH_CONTROLLER::WAYPOINT"))

(in-package "ROS")
;;//! \htmlinclude WayPoint.msg.html


(defclass robot_path_controller::WayPoint
  :super ros::object
  :slots (_coord ))

(defmethod robot_path_controller::WayPoint
  (:init
   (&key
    ((:coord __coord) (make-array 2 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _coord __coord)
   self)
  (:coord
   (&optional __coord)
   (if __coord (setq _coord __coord)) _coord)
  (:serialization-length
   ()
   (+
    ;; float64[2] _coord
    (* 8    2)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64[2] _coord
     (dotimes (i 2)
       (sys::poke (elt _coord i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64[2] _coord
   (dotimes (i (length _coord))
     (setf (elt _coord i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     )
   ;;
   self)
  )

(setf (get robot_path_controller::WayPoint :md5sum-) "c8574176233959b6be47e3bfcfdaf4a6")
(setf (get robot_path_controller::WayPoint :datatype-) "robot_path_controller/WayPoint")
(setf (get robot_path_controller::WayPoint :definition-)
      "float64[2] coord
")



(provide :robot_path_controller/WayPoint "c8574176233959b6be47e3bfcfdaf4a6")


