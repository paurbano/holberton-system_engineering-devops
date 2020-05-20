# 0x18. Webstack monitoring

# General
* Why is monitoring needed
* What are the 2 main area of monitoring
* What are access logs for a web server (such as Nginx)
* What are error logs for a web server (such as Nginx)

## 0. Sign up for Datadog and install datadog-agent

## 1. Monitor some metrics
* Set up a monitor that checks the number of read requests issued to the device per second.
* Set up a monitor that checks the number of write requests issued to the device per second.

## 2. Create a dashboard
create a dashboard with different metrics displayed in order to get a few different visualizations.

* Create a new `dashboard`
* Add at least 4 `widgets` to your dashboard. They can be of any type and monitor whatever you’d like
* Create the answer file `2-setup_datadog` which has the `dashboard_id` on the first line. Note: in order to get the id of your dashboard, you may need to use `Datadog’s API`

