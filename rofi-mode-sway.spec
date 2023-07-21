%global srcname rofi-mode-sway

Name:       rofi-mode-sway
Version:    0.0.1
Release:    1%{?dist}
Summary:    Switch windows under Sway using Rofi
License:    GPLv3+
URL: https://github.com/ludwigd/%{srcname}
# Sources can be obtained by
# git clone https://github.com/ludwigd/rofi-mode-sway
# cd rofi-mode-sway
# tito build --tgz
Source0: %{name}-%{version}.tar.gz

BuildArch: noarch

Requires: findutils
Requires: jq
Requires: rofi
Requires: sway

%description
A Rofi mode for switching windows under Sway implemented using Rofi's scripting interface.

%prep
%autosetup

%build
# nothing to build

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 755 ./rofi-mode-sway.sh %{buildroot}%{_bindir}/rofi-mode-sway.sh

%files
%license LICENSE
%{_bindir}/rofi-mode-sway.sh

%changelog
* Fri Jul 21 2023 Damian Ludwig 0.0.1-1
- new package built with tito

