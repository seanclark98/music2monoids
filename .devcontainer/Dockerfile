FROM mcr.microsoft.com/devcontainers/miniconda:0-3

RUN conda create -n sage sage python=3.11 -c conda-forge -y
RUN touch ~/.bashrc
RUN conda init
RUN source ~/.bashrc
RUN conda activate sage
