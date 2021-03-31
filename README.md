# discourse-operator

## Description

This is the Discourse charm for Kubernetes using the Python Operator Framework.

## Usage


### Deploying

```
$ git clone https://github.com/martinrusev/discourse-operator
$ cd discourse-operator

$ sudo snap install charmcraft --beta
$ charmcraft build
Created 'discourse.charm'.


$ juju deploy ./discourse.charm --resource discourse-image=discourse:3.11.10

$ juju status
Model    Controller  Cloud/Region        Version  SLA          Timestamp
discourse  pebble      microk8s/localhost  2.9-rc7  unsupported  16:36:06+01:00

App      Version  Status  Scale  Charm      Store  Channel  Rev  OS      Address  Message
discourse         active      1  discourse  local             1  ubuntu           discourse started

Unit        Workload  Agent  Address       Ports  Message
discourse/0*  active    idle   10.1.243.208         discourse started
```

## Developing

Create and activate a virtualenv with the development requirements:

```
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements-dev.txt
```

## Testing

The Python operator framework includes a very nice harness for testing
operator behaviour without full deployment. Just `run_tests`:

```
./run_tests
```


## Roadmap

The discourse Charm is still a work in progress.

Here are some of the things coming soon:

  - [ ] Postgresql support
  - [ ] Config options
