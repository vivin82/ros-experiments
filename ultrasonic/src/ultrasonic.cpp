#include <ros.h>
#include <std_msgs/Float32.h>
#define trigPin 2
#define echoPin 4
long duration;
int distance;ros::NodeHandle fu;
std_msgs::Float32 range_msg;
ros::Publisher range_pub("/range", &range_msg);
void setup(){
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
    fu.initNode();
    fu.advertise(range_pub);
}
void loop() {
    digitalWrite(trigPin, LOW);
    delayMicroseconds(10000);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10000);
    digitalWrite(trigPin, HIGH);
    duration= pulseIn(echoPin, HIGH);
    distance= duration * 0.034 / 2;
    range_msg.data = distance;
    range_pub.publish(&range_msg);
    fu.spinOnce();
}

