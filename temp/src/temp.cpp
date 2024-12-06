#include <ros.h>
#include <Arduino.h>
#include <DHT.h>
#include <DHT_U.h>
#include <sensor_msgs/Temperature.h>
#include <sensor_msgs/RelativeHumidity.h>

#define DHTPIN 2     
#define DHTTYPE DHT22 

DHT tempsense(DHTPIN, DHTTYPE);
ros::NodeHandle fu;

sensor_msgs::Temperature temp_msg;
sensor_msgs::RelativeHumidity humidity_msg;
ros::Publisher temp_pub("temperature", &temp_msg);
ros::Publisher humidity_pub("humidity", &humidity_msg);

void setup() {
  Serial.begin(9600);
  
  tempsense.begin();
  
  fu.initNode();
  
  fu.advertise(temp_pub);
  fu.advertise(humidity_pub);
}

void loop() {    

  temp_msg.temperature=tempsense.readTemperature();
  temp_msg.header.stamp=fu.now();
  temp_msg.header.frame_id="DHT 22";

  humidity_msg.relative_humidity=tempsense.readHumidity();
  humidity_msg.header.frame_id="DHT 22";
  humidity_msg.header.stamp=fu.now();


  temp_pub.publish(&temp_msg);
  humidity_pub.publish(&humidity_msg);

  fu.spinOnce();
}
