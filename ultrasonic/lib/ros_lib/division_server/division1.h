#ifndef _ROS_SERVICE_division1_h
#define _ROS_SERVICE_division1_h
#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace division_server
{

static const char DIVISION1[] = "division_server/division1";

  class division1Request : public ros::Msg
  {
    public:
      typedef float _a_type;
      _a_type a;
      typedef float _b_type;
      _b_type b;

    division1Request():
      a(0),
      b(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const override
    {
      int offset = 0;
      offset += serializeAvrFloat64(outbuffer + offset, this->a);
      offset += serializeAvrFloat64(outbuffer + offset, this->b);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer) override
    {
      int offset = 0;
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->a));
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->b));
     return offset;
    }

    virtual const char * getType() override { return DIVISION1; };
    virtual const char * getMD5() override { return "6f4f9f1b571de73ae8592a1438fd23f3"; };

  };

  class division1Response : public ros::Msg
  {
    public:
      typedef float _result_type;
      _result_type result;

    division1Response():
      result(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const override
    {
      int offset = 0;
      offset += serializeAvrFloat64(outbuffer + offset, this->result);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer) override
    {
      int offset = 0;
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->result));
     return offset;
    }

    virtual const char * getType() override { return DIVISION1; };
    virtual const char * getMD5() override { return "254fb2d8c4e08eff5dc6a560ed51dd52"; };

  };

  class division1 {
    public:
    typedef division1Request Request;
    typedef division1Response Response;
  };

}
#endif
