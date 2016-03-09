%define profile ivi

Summary:	Tizen IVI Package Groups and Image Configurations
Name:		meta-ivi
Version:	016
Release:	1
BuildArch:  noarch
License:	GPL-2.0
Group:		Base/Configuration
URL:		http://www.tizen.org
Source:		%{name}-%{version}.tar.bz2

%description
Tizen IVI Package Groups and Image Configurations

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
%{_datadir}/image-configurations/ivi/scripts
%{_datadir}/image-configurations/ivi/partitions
