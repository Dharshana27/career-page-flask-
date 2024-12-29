{ pkgs }:

{
  deps = [
    pkgs.python310  # Python 3.10 package
    pkgs.python310Packages.flask  # Flask package
  ];
}
