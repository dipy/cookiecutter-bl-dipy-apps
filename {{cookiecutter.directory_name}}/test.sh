#!/bin/bash
singularity exec -e docker://brainlife/dipy:{{cookiecutter.dipy_version}} {{ cookiecutter.cli_name }} -h
