{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=release-24.11";
  };

  outputs = { nixpkgs, ... }: let
    pkgs = nixpkgs.legacyPackages.x86_64-linux;
  in {
    packages.x86_64-linux.default = pkgs.callPackage ./nix/bapctools.nix {};
  };
}
