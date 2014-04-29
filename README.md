A docker container to use as a [fleet sidekick](http://coreos.com/docs/launching-containers/launching/launching-containers-fleet/#run-a-simple-sidekick) on CoreOS. Update DNS records when a unit is moved or started on the cluster.

```
$ docker run index.robszumski.com:5000/dns --identity 'XXXX' --secret 'XXXX' --domain 'robszumski.com.' --record 'test' --value '1.2.3.4'
Creating record for test.robszumski.com. with value 1.2.3.4
```
