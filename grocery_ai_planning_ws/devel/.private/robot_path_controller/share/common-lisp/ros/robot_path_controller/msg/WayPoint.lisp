; Auto-generated. Do not edit!


(cl:in-package robot_path_controller-msg)


;//! \htmlinclude WayPoint.msg.html

(cl:defclass <WayPoint> (roslisp-msg-protocol:ros-message)
  ((coord
    :reader coord
    :initarg :coord
    :type (cl:vector cl:float)
   :initform (cl:make-array 2 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass WayPoint (<WayPoint>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <WayPoint>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'WayPoint)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robot_path_controller-msg:<WayPoint> is deprecated: use robot_path_controller-msg:WayPoint instead.")))

(cl:ensure-generic-function 'coord-val :lambda-list '(m))
(cl:defmethod coord-val ((m <WayPoint>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_path_controller-msg:coord-val is deprecated.  Use robot_path_controller-msg:coord instead.")
  (coord m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <WayPoint>) ostream)
  "Serializes a message object of type '<WayPoint>"
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'coord))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <WayPoint>) istream)
  "Deserializes a message object of type '<WayPoint>"
  (cl:setf (cl:slot-value msg 'coord) (cl:make-array 2))
  (cl:let ((vals (cl:slot-value msg 'coord)))
    (cl:dotimes (i 2)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<WayPoint>)))
  "Returns string type for a message object of type '<WayPoint>"
  "robot_path_controller/WayPoint")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'WayPoint)))
  "Returns string type for a message object of type 'WayPoint"
  "robot_path_controller/WayPoint")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<WayPoint>)))
  "Returns md5sum for a message object of type '<WayPoint>"
  "c8574176233959b6be47e3bfcfdaf4a6")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'WayPoint)))
  "Returns md5sum for a message object of type 'WayPoint"
  "c8574176233959b6be47e3bfcfdaf4a6")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<WayPoint>)))
  "Returns full string definition for message of type '<WayPoint>"
  (cl:format cl:nil "float64[2] coord~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'WayPoint)))
  "Returns full string definition for message of type 'WayPoint"
  (cl:format cl:nil "float64[2] coord~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <WayPoint>))
  (cl:+ 0
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'coord) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <WayPoint>))
  "Converts a ROS message object to a list"
  (cl:list 'WayPoint
    (cl:cons ':coord (coord msg))
))
