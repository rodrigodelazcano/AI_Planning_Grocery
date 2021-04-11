; Auto-generated. Do not edit!


(cl:in-package robot_path_controller-srv)


;//! \htmlinclude Path-request.msg.html

(cl:defclass <Path-request> (roslisp-msg-protocol:ros-message)
  ((waypoints
    :reader waypoints
    :initarg :waypoints
    :type (cl:vector robot_path_controller-msg:WayPoint)
   :initform (cl:make-array 0 :element-type 'robot_path_controller-msg:WayPoint :initial-element (cl:make-instance 'robot_path_controller-msg:WayPoint))))
)

(cl:defclass Path-request (<Path-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Path-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Path-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robot_path_controller-srv:<Path-request> is deprecated: use robot_path_controller-srv:Path-request instead.")))

(cl:ensure-generic-function 'waypoints-val :lambda-list '(m))
(cl:defmethod waypoints-val ((m <Path-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_path_controller-srv:waypoints-val is deprecated.  Use robot_path_controller-srv:waypoints instead.")
  (waypoints m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Path-request>) ostream)
  "Serializes a message object of type '<Path-request>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'waypoints))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'waypoints))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Path-request>) istream)
  "Deserializes a message object of type '<Path-request>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'waypoints) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'waypoints)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'robot_path_controller-msg:WayPoint))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Path-request>)))
  "Returns string type for a service object of type '<Path-request>"
  "robot_path_controller/PathRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Path-request)))
  "Returns string type for a service object of type 'Path-request"
  "robot_path_controller/PathRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Path-request>)))
  "Returns md5sum for a message object of type '<Path-request>"
  "4a214603f798dc39b94ac5b447e437b3")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Path-request)))
  "Returns md5sum for a message object of type 'Path-request"
  "4a214603f798dc39b94ac5b447e437b3")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Path-request>)))
  "Returns full string definition for message of type '<Path-request>"
  (cl:format cl:nil "WayPoint[] waypoints~%~%================================================================================~%MSG: robot_path_controller/WayPoint~%float64[2] coord~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Path-request)))
  "Returns full string definition for message of type 'Path-request"
  (cl:format cl:nil "WayPoint[] waypoints~%~%================================================================================~%MSG: robot_path_controller/WayPoint~%float64[2] coord~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Path-request>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'waypoints) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Path-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Path-request
    (cl:cons ':waypoints (waypoints msg))
))
;//! \htmlinclude Path-response.msg.html

(cl:defclass <Path-response> (roslisp-msg-protocol:ros-message)
  ((complete
    :reader complete
    :initarg :complete
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass Path-response (<Path-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Path-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Path-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robot_path_controller-srv:<Path-response> is deprecated: use robot_path_controller-srv:Path-response instead.")))

(cl:ensure-generic-function 'complete-val :lambda-list '(m))
(cl:defmethod complete-val ((m <Path-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_path_controller-srv:complete-val is deprecated.  Use robot_path_controller-srv:complete instead.")
  (complete m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Path-response>) ostream)
  "Serializes a message object of type '<Path-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'complete) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Path-response>) istream)
  "Deserializes a message object of type '<Path-response>"
    (cl:setf (cl:slot-value msg 'complete) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Path-response>)))
  "Returns string type for a service object of type '<Path-response>"
  "robot_path_controller/PathResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Path-response)))
  "Returns string type for a service object of type 'Path-response"
  "robot_path_controller/PathResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Path-response>)))
  "Returns md5sum for a message object of type '<Path-response>"
  "4a214603f798dc39b94ac5b447e437b3")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Path-response)))
  "Returns md5sum for a message object of type 'Path-response"
  "4a214603f798dc39b94ac5b447e437b3")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Path-response>)))
  "Returns full string definition for message of type '<Path-response>"
  (cl:format cl:nil "bool complete~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Path-response)))
  "Returns full string definition for message of type 'Path-response"
  (cl:format cl:nil "bool complete~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Path-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Path-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Path-response
    (cl:cons ':complete (complete msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Path)))
  'Path-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Path)))
  'Path-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Path)))
  "Returns string type for a service object of type '<Path>"
  "robot_path_controller/Path")