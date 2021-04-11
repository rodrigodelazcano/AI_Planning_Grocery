// Auto-generated. Do not edit!

// (in-package robot_path_controller.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let WayPoint = require('./WayPoint.js');

//-----------------------------------------------------------

class WayPointList {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.path = null;
    }
    else {
      if (initObj.hasOwnProperty('path')) {
        this.path = initObj.path
      }
      else {
        this.path = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type WayPointList
    // Serialize message field [path]
    // Serialize the length for message field [path]
    bufferOffset = _serializer.uint32(obj.path.length, buffer, bufferOffset);
    obj.path.forEach((val) => {
      bufferOffset = WayPoint.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type WayPointList
    let len;
    let data = new WayPointList(null);
    // Deserialize message field [path]
    // Deserialize array length for message field [path]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.path = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.path[i] = WayPoint.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 16 * object.path.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'robot_path_controller/WayPointList';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '6bc47b0184d2e472693eb2c6129282d1';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    WayPoint[] path
    ================================================================================
    MSG: robot_path_controller/WayPoint
    float64[2] coord
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new WayPointList(null);
    if (msg.path !== undefined) {
      resolved.path = new Array(msg.path.length);
      for (let i = 0; i < resolved.path.length; ++i) {
        resolved.path[i] = WayPoint.Resolve(msg.path[i]);
      }
    }
    else {
      resolved.path = []
    }

    return resolved;
    }
};

module.exports = WayPointList;
