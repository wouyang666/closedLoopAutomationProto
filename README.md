# EDI

   
![highlevel](uploads/highlevel.png)

The Event Driven Framework can be used as a general framework to enable Closed Loop Automation. Here we will KAFKA as the message bus. Applications such as Appformix, Healthbot can produce events(trigger alarms) onto the message bus. Those events can be consumed by Event Consumers, saved in Elasticsearch and queried by Remediation Applications to trigger remediation actions.
