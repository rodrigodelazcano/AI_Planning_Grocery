// Auto-generated. Do not edit!

// (in-package robot_path_controller.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class WayPoint {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.coord = null;
    }
    else {
      if (initObj.hasOwnProperty('coord')) {
        this.coord = initObj.coord
      }
      else {
        this.coord = new Array(2).fill(0);
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type WayPoint
    // Check that the constant length array field [coord] has the right length
    if (obj.coord.length !== 2) {
      throw new Error('Unable to serialize array field coord - length must be 2')
    }
    // Serialize message field [coord]
    bufferOffset = _arraySerializer.float64(obj.coord, buffer, bufferOffset, 2);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type WayPoint
    let len;
    let data = new WayPoint(null);
    // Deserialize message field [coord]
    data.coord = _arrayDeserializer.float64(buffer, bufferOffset, 2)
    return data;
  }

  static getMessageSize(object) {
    return 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'robot_path_controller/WayPoint';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c8574176233959b6be47e3bfcfdaf4a6';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64[2] coord
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new WayPoint(null);
    if (msg.coord !== undefined) {
      resolved.coord = msg.coord;
    }
    else {
      resolved.coord = new Array(2).fill(0)
    }

    return resolved;
    }
};

module.exports = WayPoint;
