{ pkgs ? import <nixpkgs> {} }:

(pkgs.buildFHSUserEnv {
  name = "python3-numpy-shell";
  targetPkgs = pkgs: with pkgs; [
		gcc
		zlib
  ];
  runScript = "zsh";
}).env
