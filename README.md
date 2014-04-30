A docker container to use as a [fleet sidekick](http://coreos.com/docs/launching-containers/launching/launching-containers-fleet/#run-a-simple-sidekick) on CoreOS. Update DNS records when a unit is moved or started on the cluster.

## Configuration

| Parameter | Description |
|-----------|-------------|
| identity  | Username or other identifier for the provider |
| secret    | API key, password or other secret for the provider |
| domain    | Domain that contains the record, ending in a trailing period. `robszumski.com.` |
| record    | Name of the record to be created or updated. `www` |
| value     | Value of the record |
| type      | Record type. Defaults to `A`. |
| provider  | DNS provider to be configured with libcloud. Defaults to `route53`. |

## Run Manually
```
$ docker run index.robszumski.com:5000/dns --identity 'XXXX' --secret 'XXXX' --domain 'robszumski.com.' --record 'test' --value '1.2.3.4'
Creating record for test.robszumski.com. with value 1.2.3.4
```

## Example Unit File
```
[Unit]
Description=DNS Sidekick for Test

[Service]
EnvironmentFile=/etc/environment
ExecStart=/bin/bash -c '/usr/bin/docker start -a test1 || /usr/bin/docker run -rm -name test1 index.robszumski.com:5000/dns --identity "XXXX" --secret "XXXX" --domain "robszumski.com." --record "test" --value "$COREOS_PUBLIC_IPV4" 

[X-Fleet]
X-ConditionMachineOf=test.1.service
```
