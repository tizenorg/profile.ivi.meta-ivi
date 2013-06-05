Summary:	IVI Meta Data
Name:		meta-ivi
Version:	001
Release:	1
License:	GPL-2.0
Group:		System/Base
URL:		http://www.tizen.org
Source:		%{name}-%{version}.tar.bz2

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
%{_datadir}/package-groups/ivi/*.yaml
%{_datadir}/image-configurations/ivi/*.yaml
%{_datadir}/image-configurations/ivi/configs/*.yaml
%{_datadir}/image-configurations/ivi/partitions/*
%{_datadir}/image-configurations/ivi/scripts/*
