Summary:	IVI Meta Data
Name:		meta-ivi
Version:	001
Release:	1
BuildArch:  noarch
License:	GPL-2.0
Group:		Base/Configuration
URL:		http://www.tizen.org
Source:		%{name}-%{version}.tar.bz2
BuildRequires: meta-common

%description
IVI Meta Data.
Includes patterns and image configurations for IVI images.

%prep
%setup -q

%build
make

%install
%make_install


%files
%attr(644,-,-) %{_datadir}/package-groups/ivi/*.yaml
%attr(644,-,-) %{_datadir}/image-configurations/ivi/*.yaml
%attr(644,-,-) %{_datadir}/image-configurations/ivi/configs/*.yaml
%attr(644,-,-) %{_datadir}/image-configurations/ivi/partitions/*
%attr(644,-,-) %{_datadir}/image-configurations/ivi/scripts/*
