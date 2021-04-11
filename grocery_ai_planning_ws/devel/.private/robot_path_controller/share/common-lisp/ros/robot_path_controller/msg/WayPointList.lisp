; Auto-generated. Do not edit!


(cl:in-package robot_path_controller-msg)


;//! \htmlinclude WayPointList.msg.html

(cl:defclass <WayPointList> (roslisp-msg-protocol:ros-message)
  ((path
    :reader path
    :initarg :path
    :type (cl:vector robot_path_controller-msg:WayPoint)
   :initform (cl:make-array 0 :element-type 'robot_path_controller-msg:WayPoint :initial-element (cl:make-instance 'robot_path_controller-msg:WayPoint))))
)

(cl:defclass WayPointList (<WayPointList>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <WayPointList>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'WayPointList)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robot_path_controller-msg:<WayPointList> is deprecated: use robot_path_controller-msg:WayPointList instead.")))

(cl:ensure-generic-function 'path-val :lambda-list '(m))
(cl:defmethod path-val ((m <WayPointList>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_path_controller-msg:path-val is deprecated.  Use robot_path_controller-msg:path instead.")
  (path m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <WayPointList>) ostream)
  "Serializes a message object of type '<WayPointList>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'path))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'path))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <WayPointList>) istream)
  "Deserializes a message object of type '<WayPointList>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'path) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'path)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'robot_path_controller-msg:WayPoint))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<WayPointList>)))
  "Returns string type for a message object of type '<WayPointList>"
  "robot_path_controller/WayPointList")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'WayPointList)))
  "Returns string type for a message object of type 'WayPointList"
  "robot_path_controller/WayPointList")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<WayPointList>)))
  "Returns md5sum for a message object of type '<WayPointList>"
  "6bc47b0184d2e472693eb2c6129282d1")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'WayPointList)))
  "Returns md5sum for a message object of type 'WayPointList"
  "6bc47b0184d2e472693eb2c6129282d1")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<WayPointList>)))
  "Returns full string definition for message of type '<WayPointList>"
  (cl:format cl:nil "WayPoint[] path~%================================================================================~%MSG: robot_path_controller/WayPoint~%float64[2] coord~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'WayPointList)))
  "Returns full string definition for message of type 'WayPointList"
  (cl:format cl:nil "WayPoint[] path~%================================================================================~%MSG: robot_path_controller/WayPoint~%float64[2] coord~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <WayPointList>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'path) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <WayPointList>))
  "Converts a ROS message object to a list"
  (cl:list 'WayPointList
    (cl:cons ':path (path msg))
))
