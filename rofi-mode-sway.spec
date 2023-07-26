%global srcname rofi-mode-sway

Name:       yaws
Version:    0.0.1
Release:    1%{?dist}
Summary:    Yet Another Window Switcher for Rofi+Sway
License:    GPLv3+
URL: https://github.com/ludwigd/%{srcname}
# Sources can be obtained by
# git clone https://github.com/ludwigd/rofi-mode-sway
# cd rofi-mode-sway
# tito build --tgz
Source0: %{name}-%{version}.tar.gz

BuildArch: noarch

Requires: bash
Requires: findutils
Requires: jq
Requires: rofi
Requires: sway

Obsoletes: rofi-mode-sway < %{version}-%{release}
Provides: rofi-mode-sway = %{version}-%{release}

%description
A Rofi mode for switching windows under Sway implemented using Rofi's scripting interface.

%prep
%autosetup

%build
# nothing to build

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 755 ./yaws %{buildroot}%{_bindir}/yaws

%files
%license LICENSE
%{_bindir}/yaws

%changelog
* Wed Jul 26 2023 Damian Ludwig 0.0.1-1
- rename to yaws (yet another window switcher)

* Fri Jul 21 2023 Damian Ludwig 0.0.1-1
- new package built with tito

