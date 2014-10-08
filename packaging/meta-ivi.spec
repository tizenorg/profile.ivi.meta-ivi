Summary:	IVI Meta Data
Name:		meta-ivi
Version:	013
Release:	0
BuildArch:  noarch
License:	GPL-2.0
Group:		Base/Configuration
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
%attr(644,-,-) %{_datadir}/package-groups/ivi/*.yaml
%{_datadir}/image-configurations/ivi/*.yaml
%{_datadir}/image-configurations/ivi/configs/*.yaml
%{_datadir}/image-configurations/ivi/partitions
%{_datadir}/image-configurations/ivi/scripts
