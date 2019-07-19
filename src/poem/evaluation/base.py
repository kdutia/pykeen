# -*- coding: utf-8 -*-

"""Basic structure of a evaluator."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, Mapping

import numpy as np
import torch.nn as nn

from poem.models.base import BaseModule

__all__ = [
    'EvaluatorConfig',
    'Evaluator',
]


@dataclass
class EvaluatorConfig:
    config: Dict
    model: nn.Module
    entity_to_id: Dict[str, int]
    relation_to_id: Dict[str, int]
    training_triples: np.ndarray = None


class Evaluator(ABC):
    def __init__(
            self,
            entity_to_id: Mapping,
            relation_to_id: Mapping,
            model: nn.Module = None,
    ) -> None:
        self.model = model
        self.entity_to_id = entity_to_id
        self.relation_to_id = relation_to_id

    def set_model(self, model: BaseModule) -> None:
        """Set model that should be trained."""
        self.model = model

    @property
    def device(self):
        return self.model.device

    @abstractmethod
    def evaluate(self, triples: np.ndarray):
        pass
