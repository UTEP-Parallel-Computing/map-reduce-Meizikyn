{ pkgs ? import <nixpkgs> {} }:

(pkgs.buildFHSUserEnv {
  name = "python3-numpy-shell";
  targetPkgs = pkgs: with pkgs; [
		gcc
    openmpi
		zlib
  ];
  runScript = "zsh";
}).env
