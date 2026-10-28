#ifndef _ROS_SERVICE_unit_cnvr_h
#define _ROS_SERVICE_unit_cnvr_h
#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace unit_conversion
{

static const char UNIT_CNVR[] = "unit_conversion/unit_cnvr";

  class unit_cnvrRequest : public ros::Msg
  {
    public:
      typedef float _cm_type;
      _cm_type cm;

    unit_cnvrRequest():
      cm(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const override
    {
      int offset = 0;
      offset += serializeAvrFloat64(outbuffer + offset, this->cm);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer) override
    {
      int offset = 0;
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->cm));
     return offset;
    }

    virtual const char * getType() override { return UNIT_CNVR; };
    virtual const char * getMD5() override { return "81b619183432c1df6a1a5e1eb343d28b"; };

  };

  class unit_cnvrResponse : public ros::Msg
  {
    public:
      typedef float _mm_type;
      _mm_type mm;

    unit_cnvrResponse():
      mm(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const override
    {
      int offset = 0;
      offset += serializeAvrFloat64(outbuffer + offset, this->mm);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer) override
    {
      int offset = 0;
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->mm));
     return offset;
    }

    virtual const char * getType() override { return UNIT_CNVR; };
    virtual const char * getMD5() override { return "05471b6a792bbbd1e192b9f7c87cd27b"; };

  };

  class unit_cnvr {
    public:
    typedef unit_cnvrRequest Request;
    typedef unit_cnvrResponse Response;
  };

}
#endif
