{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=release-24.11";
    nixpkgs-problemtools.url = "github:thecolorman/nixpkgs?ref=add-problemtools";
  };

  outputs = { self, nixpkgs, nixpkgs-problemtools }: let
    pkgs = nixpkgs.legacyPackages.x86_64-linux;

    problemtools = nixpkgs-problemtools.legacyPackages.x86_64-linux.problemtools;
  in {
    packages.x86_64-linux.default = pkgs.callPackage ./nix/bapctools.nix {};
    devShells.x86_64-linux.default = pkgs.mkShellNoCC {
      packages = [
        self.outputs.packages.x86_64-linux.default
      ] ++ (with pkgs; [
        gnat
        python3
        ruff
        texliveMedium
        pypy3
      ]) ++ [
        problemtools
      ];
    };
  };
}
