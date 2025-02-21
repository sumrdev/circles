{
  python3,
  fetchFromGitHub,
  writeShellApplication,
  texliveMedium
}: let
  py = python3.withPackages (p: with p; [
    colorama
    pyyaml
    dateutil
    argcomplete
    ruamel-yaml
    matplotlib
    requests
    questionary
  ]);

  src = fetchFromGitHub {
    owner = "RagnarGrootKoerkamp";
    repo = "BAPCtools";
    rev = "c009609f83781b39221f79faebaf9aa2e2139e39";
    hash = "sha256-pXyZzgWSId81VZ1arJ4Ok8kM1khNOH0Uosa5Ai6vBgQ=";
  };
in writeShellApplication {
  name = "bt";

  runtimeInputs = [
    texliveMedium
  ];
  text = ''
    ${py}/bin/python3 ${src}/bin/tools.py "$@"
  '';
}
