# Mesos ServerDensity plugin
ServerDensity plugin for monitoring Mesos metrics

This plugin got created for a sole purpose of passing the metrics of Mesos nodes to [ServerDensity](www.serverdensity.com) for further monitoring and alerting. More information about the metrics exposed is available in [Mesos documentation](http://mesos.apache.org/documentation/latest/monitoring/).

## Configuration

Mesos nodes automatically expose the `/metrics/snapshot` HTTP endpoint and you just need to configure on which IP and port the server listens in a `Mesos` scope.

### Parameters

- `ip` - IP on which the server listens
- `port` - port on which the server listens

### Example

```
[Mesos]
ip: 10.0.0.1
port: 5050
```

## Recommended alerts

### Master
- `master/uptime_secs` - if below X for longer than X, the master is flapping
- `master/tasks_lost` - if rapidly increasing the cluster has problem
- `master/cpus_percent` - if > 0.9 the master is reaching the limit of available CPU
- `master/mem_percent` - if > 0.9 the master is reaching the limit of available memory
- `master/elected` - 0 if no master is elected

### Slave
- `slave/uptime_secs` - if below X for longer than X, the slave is flapping
- `slave/disk_percent` - if just continues rising the slave might run out of space, a threshold is recommended

## Additional plugins

Since the Mesos cluster relies on working ZooKeeper, the [ZooKeeper plugin](https://github.com/serverdensity/sd-agent-plugins/tree/master/ZooKeeper) is highly recommended for monitoring of the ZooKeeper cluster health.
