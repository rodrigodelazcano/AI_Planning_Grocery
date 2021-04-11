// Generated by gencpp from file robot_path_controller/PathWayPoints.msg
// DO NOT EDIT!


#ifndef ROBOT_PATH_CONTROLLER_MESSAGE_PATHWAYPOINTS_H
#define ROBOT_PATH_CONTROLLER_MESSAGE_PATHWAYPOINTS_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace robot_path_controller
{
template <class ContainerAllocator>
struct PathWayPoints_
{
  typedef PathWayPoints_<ContainerAllocator> Type;

  PathWayPoints_()
    : coord()  {
      coord.assign(0.0);
  }
  PathWayPoints_(const ContainerAllocator& _alloc)
    : coord()  {
  (void)_alloc;
      coord.assign(0.0);
  }



   typedef boost::array<double, 2>  _coord_type;
  _coord_type coord;





  typedef boost::shared_ptr< ::robot_path_controller::PathWayPoints_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::robot_path_controller::PathWayPoints_<ContainerAllocator> const> ConstPtr;

}; // struct PathWayPoints_

typedef ::robot_path_controller::PathWayPoints_<std::allocator<void> > PathWayPoints;

typedef boost::shared_ptr< ::robot_path_controller::PathWayPoints > PathWayPointsPtr;
typedef boost::shared_ptr< ::robot_path_controller::PathWayPoints const> PathWayPointsConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::robot_path_controller::PathWayPoints_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::robot_path_controller::PathWayPoints_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::robot_path_controller::PathWayPoints_<ContainerAllocator1> & lhs, const ::robot_path_controller::PathWayPoints_<ContainerAllocator2> & rhs)
{
  return lhs.coord == rhs.coord;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::robot_path_controller::PathWayPoints_<ContainerAllocator1> & lhs, const ::robot_path_controller::PathWayPoints_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace robot_path_controller

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::robot_path_controller::PathWayPoints_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::robot_path_controller::PathWayPoints_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::robot_path_controller::PathWayPoints_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::robot_path_controller::PathWayPoints_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::robot_path_controller::PathWayPoints_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::robot_path_controller::PathWayPoints_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::robot_path_controller::PathWayPoints_<ContainerAllocator> >
{
  static const char* value()
  {
    return "c8574176233959b6be47e3bfcfdaf4a6";
  }

  static const char* value(const ::robot_path_controller::PathWayPoints_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xc8574176233959b6ULL;
  static const uint64_t static_value2 = 0xbe47e3bfcfdaf4a6ULL;
};

template<class ContainerAllocator>
struct DataType< ::robot_path_controller::PathWayPoints_<ContainerAllocator> >
{
  static const char* value()
  {
    return "robot_path_controller/PathWayPoints";
  }

  static const char* value(const ::robot_path_controller::PathWayPoints_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::robot_path_controller::PathWayPoints_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64[2] coord\n"
;
  }

  static const char* value(const ::robot_path_controller::PathWayPoints_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::robot_path_controller::PathWayPoints_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.coord);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct PathWayPoints_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::robot_path_controller::PathWayPoints_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::robot_path_controller::PathWayPoints_<ContainerAllocator>& v)
  {
    s << indent << "coord[]" << std::endl;
    for (size_t i = 0; i < v.coord.size(); ++i)
    {
      s << indent << "  coord[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.coord[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROBOT_PATH_CONTROLLER_MESSAGE_PATHWAYPOINTS_H
