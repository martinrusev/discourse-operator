#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging


from ops.charm import CharmBase, PebbleReadyEvent
from ops.framework import StoredState
from ops.main import main
from ops.model import ActiveStatus, ModelError
from ops.pebble import ServiceStatus, Layer


logger = logging.getLogger(__name__)

class DiscourseOperator(CharmBase):

    _stored = StoredState()

    def __init__(self, *args):
        super().__init__(*args)

        self.framework.observe(
            self.on.discourse_pebble_ready, self._on_discourse_pebble_ready
        )


    def _on_discourse_pebble_ready(self, event: PebbleReadyEvent) -> None:
        container = event.workload
        logger.info("_on_discourse_pebble_ready")

        # Check we can get a list of services back from the Pebble API
        if self._is_running(container, "discourse"):
            logger.info("discourse already started")
            return


        logger.info("_start_discourse")
        container.add_layer("discourse", self._discourse_layer(), combine=True)
        container.autostart()
        self.unit.status = ActiveStatus("discourse started")


    def _discourse_layer(self):
        layer = Layer(
            raw = {
            "summary": "discourse layer",
            "description": "discourse layer",
            "services": {
                "discourse": {
                    "override": "replace",
                    "summary": "discourse service",
                    "command": "nami start --foreground discourse",
                    "startup": "enabled",
                    "environment": []
                }
            },
        })

        return layer



    def _is_running(self, container, service):
        """Helper method to determine if a given service is running in a given container"""
        try:
            service = container.get_service(service)
        except ModelError:
            return False
        return service.current == ServiceStatus.ACTIVE


if __name__ == "__main__":
    main(DiscourseOperator)
