{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=release-24.11";
  };

  outputs = { self, nixpkgs }: let
    pkgs = nixpkgs.legacyPackages.x86_64-linux;
  in {
    packages.x86_64-linux.default = pkgs.callPackage ./nix/bapctools.nix {};
    devShells.x86_64-linux.default = pkgs.mkShellNoCC {
      packages = [
        self.outputs.packages.x86_64-linux.default
      ] ++ (with pkgs; [
        gnat
        python3
        ruff
      ]);
    };
  };
}
