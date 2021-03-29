
"use strict";

let DockInfraRed = require('./DockInfraRed.js');
let MotorPower = require('./MotorPower.js');
let ExternalPower = require('./ExternalPower.js');
let VersionInfo = require('./VersionInfo.js');
let ControllerInfo = require('./ControllerInfo.js');
let DigitalOutput = require('./DigitalOutput.js');
let RobotStateEvent = require('./RobotStateEvent.js');
let BumperEvent = require('./BumperEvent.js');
let SensorState = require('./SensorState.js');
let Sound = require('./Sound.js');
let WheelDropEvent = require('./WheelDropEvent.js');
let DigitalInputEvent = require('./DigitalInputEvent.js');
let Led = require('./Led.js');
let CliffEvent = require('./CliffEvent.js');
let KeyboardInput = require('./KeyboardInput.js');
let ScanAngle = require('./ScanAngle.js');
let ButtonEvent = require('./ButtonEvent.js');
let PowerSystemEvent = require('./PowerSystemEvent.js');
let AutoDockingGoal = require('./AutoDockingGoal.js');
let AutoDockingFeedback = require('./AutoDockingFeedback.js');
let AutoDockingResult = require('./AutoDockingResult.js');
let AutoDockingActionGoal = require('./AutoDockingActionGoal.js');
let AutoDockingActionResult = require('./AutoDockingActionResult.js');
let AutoDockingActionFeedback = require('./AutoDockingActionFeedback.js');
let AutoDockingAction = require('./AutoDockingAction.js');

module.exports = {
  DockInfraRed: DockInfraRed,
  MotorPower: MotorPower,
  ExternalPower: ExternalPower,
  VersionInfo: VersionInfo,
  ControllerInfo: ControllerInfo,
  DigitalOutput: DigitalOutput,
  RobotStateEvent: RobotStateEvent,
  BumperEvent: BumperEvent,
  SensorState: SensorState,
  Sound: Sound,
  WheelDropEvent: WheelDropEvent,
  DigitalInputEvent: DigitalInputEvent,
  Led: Led,
  CliffEvent: CliffEvent,
  KeyboardInput: KeyboardInput,
  ScanAngle: ScanAngle,
  ButtonEvent: ButtonEvent,
  PowerSystemEvent: PowerSystemEvent,
  AutoDockingGoal: AutoDockingGoal,
  AutoDockingFeedback: AutoDockingFeedback,
  AutoDockingResult: AutoDockingResult,
  AutoDockingActionGoal: AutoDockingActionGoal,
  AutoDockingActionResult: AutoDockingActionResult,
  AutoDockingActionFeedback: AutoDockingActionFeedback,
  AutoDockingAction: AutoDockingAction,
};
