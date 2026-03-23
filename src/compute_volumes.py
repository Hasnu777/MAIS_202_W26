import os
import json
import torch

def compute_tumor_volume(tensor, threshold):
  """
  Compute tumor volume as number of voxels above threshold.
  """
  tumor_voxels = (tensor > threshold).sum().item()
  tumor_volume = float(tumor_voxels)
  return tumor_volume

def compute_patient_volumes(data_path, output_path):
  """
  Loop through all patients and compute tumor volumes.
  """
  volumes = {}
